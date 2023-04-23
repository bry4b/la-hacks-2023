# Import module
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import keyboard
import sys
import time
sys.path.insert(1, ".\src")
import microphone
import pipline as pp #heheheha


# Create object
root = tk.Tk()
style = ttk.Style(root)
# root.tk.call('source', 'azure.tcl')
# style.theme_use('azure')
 # Create transparent window
#root.attributes("-alpha", 0.0)
root.config(bg = '#add123')

#Create a transparent window
root.wm_attributes('-transparentcolor','#add123')

# Create label with opaque text
label = tk.Label(root, text="VIEW", font=("Arial Bold", 18), height=1, width=6, bg="#192a3a", fg="#ffffff")
label.place(relx=1, rely=0.9328, anchor=tk.SE)
# Adjust size
root.attributes('-fullscreen',True)
root.attributes('-topmost',True)

bulletButton = tk.Button(root, text="Bullet Record", font=("Calibri", 12), height=1, width=12, bg="#d1d5db", fg = "#000000")
bulletButton.place(relx=.928, rely=.933, anchor=tk.SE)
imageButton = tk.Button(root, text="Image Record", font=("Calibri", 12), height=1, width=12, bg="#d1d5db", fg = "#000000")
imageButton.place(relx=.845, rely=.933, anchor=tk.SE)

running = True
bulletRecord = microphone.Recorder()
imageRecord = microphone.Recorder()
isBulletRecording = False
isImageRecording = False

def stop_running():
    root.destroy()
    running = False

def toggle_bullet_rec():
    global isBulletRecording
    global bulletRecord
    if isBulletRecording:
        print('Bullet Recording Stopped')
        bulletRecord.stop_recording('bulletOutput.wav')
        bulletRecord = microphone.Recorder()
        isBulletRecording = False
        bulletButton.configure(bg="#d1d5db")
    else:
        print('Bullet Recording')
        bulletRecord.start_recording()
        isBulletRecording = True
        bulletButton.configure(bg="#ff3200")


def toggle_image_rec():
    global isImageRecording
    global imageRecord
    global imageOut
    if isImageRecording:
        print('Image Recording Stopped')
        imageRecord.stop_recording('imageOutput.wav')
        imageRecord = microphone.Recorder()
        isImageRecording = False
        imageButton.configure(bg="#d1d5db")
        try:
            pp.generate_image_from_text('imageOutput.wav', 'imageOutput.png')         
            img = ImageTk.PhotoImage(Image.open("imageOutput.png").resize((600,600)))
            imageOut = tk.Label(root, image=img)
            imageOut.photo = img
            imageOut.place(relx=0.5, rely=0.45, anchor="center")
        except Exception as ex:
            message = "We are sorry but your request could not be completed at this time due to the following error: \n" + str(ex)
            errorMessage = tk.Label(root, text=message, font=("Calibri", 14), borderwidth=2, relief="solid", padx=10, pady=10, bg="#192a3a", fg="#ffffff")
            errorMessage.place(relx=0.5, rely=0.45, anchor="center")
        

    else:
        print('Image Recording')
        imageRecord.start_recording()
        isImageRecording = True
        imageButton.configure(bg="#ff3200")
        
        

bulletButton.configure(command=toggle_bullet_rec)
imageButton.configure(command=toggle_image_rec)

keyboard.add_hotkey('esc', lambda: stop_running())
keyboard.add_hotkey('b', lambda: toggle_bullet_rec())
keyboard.add_hotkey('i', lambda: toggle_image_rec())


# Execute tkinter
root.mainloop()
