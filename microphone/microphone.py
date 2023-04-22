import argparse
import tempfile
import queue
import sys
import os
import glob

import keyboard
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

# Credit @mgeier
def get_user_recording():
    q = queue.Queue()
    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())
    try:
        filename = 'testsound'
        device_info = sd.query_devices(None,'input')
        # soundfile expects an int, sounddevice provides a float:
        samplerate = int(device_info['default_samplerate'])
        filename = tempfile.mktemp(prefix=filename,
                                        suffix='.wav', dir='')
        # Make sure the file is opened before recording anything:
        
        with sf.SoundFile(filename, mode='x', samplerate=samplerate, channels=1) as file:
            keyboard.wait("space")
            with sd.InputStream(samplerate=samplerate,
                                channels=1, callback=callback):
                print('Began recording!')
                while keyboard.is_pressed("space"):
                    file.write(q.get())
                print('Done recording!')

    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(filename))
        exit(0)
    return file.name
    

# Remove past sound files
# import os, glob
#for f in glob.glob("testsound*"):
#    os.remove(f)