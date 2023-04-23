# Import module
import tkinter as tk
from tkinter.filedialog import asksaveasfile
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import keyboard
import sys
import time
import os
sys.path.insert(1, ".\src")
import microphone
import pipline as pp #heheheha
import speechtotext as sp
import summarizetext as st
        
class GUI:
    def __init__(self, app):
        # Create object
        self.root = tk.Toplevel()
        style = ttk.Style(self.root)
        self.root.config(bg = '#add123')

        #Create a transparent window
        self.root.wm_attributes('-transparentcolor','#add123')

        # Create label with opaque text
        self.label = tk.Label(self.root, text="VIEW", font=("Arial Bold", 18), height=1, width=6, bg="#192a3a", fg="#ffffff")
        self.label.place(relx=1, rely=0.9328, anchor=tk.SE)
        # Adjust size
        self.root.attributes('-fullscreen',True)
        self.root.attributes('-topmost',True)

        self.bulletButton = tk.Button(self.root, text="Bullet Record", font=("Calibri", 12), height=1, width=12, bg="#d1d5db", fg = "#000000")
        self.bulletButton.place(relx=.928, rely=.933, anchor=tk.SE)
        self.imageButton = tk.Button(self.root, text="Image Record", font=("Calibri", 12), height=1, width=12, bg="#d1d5db", fg = "#000000")
        self.imageButton.place(relx=.845, rely=.933, anchor=tk.SE)

        self.saveBulletButton = tk.Button(self.root, text="Save Bullet", font=("Calibri", 12), height=1, width=12, bg="#d1d5db", fg = "#000000")
        self.saveBulletButton.place(relx=1-.928, rely=.933, anchor=tk.SE)

        self.exitButton = tk.Button(self.root, text="[X]", font=("Calibri", 10), bg="#d30000", fg = "#ffffff")
        self.exitButton.place(relx=1, rely=0, anchor=tk.NE)

        self.running = True
        self.bulletRecord = microphone.Recorder()
        self.imageRecord = microphone.Recorder()
        self.isBulletRecording = False
        self.isImageRecording = False

        self.bulletButton.configure(command=self.toggle_bullet_rec)
        self.imageButton.configure(command=self.toggle_image_rec)
        self.exitButton.configure(command=self.stop_running)
        self.saveBulletButton.configure(command=self.save_bullets)

        keyboard.add_hotkey('ctrl+q', lambda: self.stop_running())
        keyboard.add_hotkey('b', lambda: self.toggle_bullet_rec())
        keyboard.add_hotkey('i', lambda: self.toggle_image_rec())

        self.app = app
        
        # Execute tkinter
        self.root.mainloop()
    
    def stop_running(self):
        self.root.destroy()
        self.running = False
        self.app.show()
    
    def save_bullets(self):
        f = asksaveasfile(initialfile = 'Untitled.txt',
            defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        with open('bullet.txt', 'r') as b:
            if f is not None:
                f.write(b.read())


    def toggle_bullet_rec(self):
        if self.isBulletRecording:
            print('Bullet Recording Stopped')
            self.bulletRecord.stop_recording('bulletOutput.wav')

            transcript = sp.get_transcript('bulletOutput.wav', bullet=True)
            transcript = st.generate_bullet_point(transcript)

            with open('bullet.txt', 'a') as f:
                f.write(transcript)
                f.write('\n')

            self.bulletRecord = microphone.Recorder()
            self.isBulletRecording = False
            self.bulletButton.configure(bg="#d1d5db")
        elif not self.isImageRecording:
            print('Bullet Recording')
            self.bulletRecord.start_recording()
            self.isBulletRecording = True
            self.bulletButton.configure(bg="#ff3200")


    def toggle_image_rec(self):
        if self.isImageRecording:
            print('Image Recording Stopped')
            self.imageRecord.stop_recording('imageOutput.wav')
            self.imageRecord = microphone.Recorder()
            self.isImageRecording = False
            self.imageButton.configure(bg="#d1d5db")
            removeMessage = tk.Label(self.root, text="Press enter to remove.", font=("Calibri", 12), borderwidth=1, relief="solid", bg="#192a3a", fg="#ffffff")
            try:
                pp.generate_image_from_text('imageOutput.wav', 'imageOutput.png')         
                img = ImageTk.PhotoImage(Image.open("imageOutput.png").resize((600,600)))
                imageOut = tk.Label(self.root, image=img)
                imageOut.photo = img
                imageOut.place(relx=0.5, rely=0.45, anchor="center")
                def delete_image_popups():
                    imageOut.destroy()
                    removeMessage.destroy()
            except Exception as ex:
                message = "We are sorry but your request could not be completed at this time due to the following error: \n" + str(ex)
                errorMessage = tk.Label(self.root, text=message, font=("Calibri", 14), borderwidth=2, relief="solid", padx=10, pady=10, bg="#192a3a", fg="#ffffff")
                errorMessage.place(relx=0.5, rely=0.45, anchor="center")
                def delete_image_popups():
                    errorMessage.destroy()
                    removeMessage.destroy()
            removeMessage = tk.Label(self.root, text="Press enter to remove.", font=("Calibri", 10), padx=5, pady=5, bg="#192a3a", fg="#ffffff")
            removeMessage.place(relx=0.5, rely=0.9, anchor="center")
            keyboard.add_hotkey('enter', lambda: delete_image_popups())
        elif not self.isBulletRecording:
            print('Image Recording')

            self.imageRecord = microphone.Recorder()
            self.imageRecord.start_recording()
            self.isImageRecording = True
            self.imageButton.configure(bg="#ff3200")
