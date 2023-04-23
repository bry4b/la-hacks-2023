import threading
import queue
import pyaudio
import wave

class Recorder:
    def __init__(self):
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1
        self.fs = 44100  # Record at 44100 samples per second
        self.frames = []  # Initialize an empty list to store audio frames
        self.recording = False
        self.q = queue.Queue()
        self.thread = threading.Thread(target=self.record_audio, daemon=True)

    def start_recording(self):
        self.recording = True
        self.thread.start()

    def stop_recording(self, output_file):
        self.recording = False
        self.thread.join()
        self.save_audio(output_file)

    def record_audio(self):
        p = pyaudio.PyAudio()  # Create an interface to the default audio device

        stream = p.open(format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True)

        while self.recording:
            data = stream.read(self.chunk)
            self.q.put(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def save_audio(self, output_file):
        p = pyaudio.PyAudio()
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        while not self.q.empty():
            data = self.q.get()
            self.frames.append(data)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        p.terminate()
        
