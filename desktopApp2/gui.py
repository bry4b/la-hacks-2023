# Import module
import tkinter as tk
import tkinter.ttk as ttk
import keyboard
import microphone
import time

# Create object
root = tk.Tk()
style = ttk.Style(root)
root.tk.call('source', 'azure dark/azure dark.tcl')
style.theme_use('azure')
 # Create transparent window
#root.attributes("-alpha", 0.0)
root.config(bg = '#add123')

#Create a transparent window
root.wm_attributes('-transparentcolor','#add123')

# Create button with light grey background
button = tk.Button(root, text="Unpressed", font=("Arial Bold", 16), bg="#D3D3D3", fg="#000000")
button.place(relx=0.95, rely=0.85, anchor=tk.SE)

# Define function to handle button click event
def toggle_button():
    if button["text"] == "Unpressed":
        button.configure(text="Pressed", bg="#D3D3D3")
    else:
        button.configure(text="Unpressed", bg="#D3D3D3")

# Bind button click event to function
button.configure(command=toggle_button)
# c = Canvas(root)
# c.pack(side=BOTTOM, anchor=SE)
# c.create_image(relx=.7, rely=.7, img)
# c.create_text(relx=.7, rely=.7, "VIEW")

# Create label with opaque text
label = tk.Label(root, text="VIEW", font=("Arial Bold", 25), fg="#000000")
label.place(relx=0.95, rely=0.95, anchor=tk.SE)
# Adjust size
root.attributes('-fullscreen',True)
root.attributes('-topmost',True)

running = True
record = microphone.Recorder()
isRecording = False

def stop_running():
    root.destroy()
    running = False

def toggle_rec():
    global isRecording
    global record
    if isRecording:
        print('Stopped')
        record.stop_recording('output.wav')
        record = microphone.Recorder()
        isRecording = False
    else:
        print('Recording')
        record.start_recording()
        isRecording = True

keyboard.add_hotkey('esc', lambda: stop_running())
keyboard.add_hotkey('b', lambda: toggle_rec())

# Execute tkinter
root.mainloop()


# while running:
#     event = keyboard.read_event()
#     if event.event_type == keyboard.KEY_DOWN and event.name == 'b':
#         if not isRecording:
#             isRecording = True
#             button.configure(text="Recording", bg="#D3D3D3")
#             record.start_recording()

#         else: 
#             isRecording = False
#             button.configure(text="Stopped", bg="#D3D3D3")
#             record.stop_recording("audio.wav")