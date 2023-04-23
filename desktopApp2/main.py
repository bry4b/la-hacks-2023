import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import filedialog
from PIL import ImageTk, Image
import gui as g
import os
import subprocess

class App:
    def __init__(self):
        # Create a window
        self.root = tk.Tk()
        self.root.geometry("550x550")
        self.root.title("My App")

        self.gui = None

        # Set the theme
        self.root.iconphoto(True, tk.PhotoImage(file=os.getcwd()+'\\logo.png'))
        self.style = ThemedStyle(self.root)
        self.style.set_theme("adapta")

        # Create a main frame for the start screen
        main_image = Image.open('logo.png')
        newimage = (600, 600)
        new_logo = main_image.resize(newimage)
        newlogo = ImageTk.PhotoImage(new_logo)
        self.main_frame = tk.Frame(self.root, width = newlogo.width(), height = newlogo.height(), bg="white")
        self.background_label = tk.Label(self.main_frame, image=newlogo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Add a "Start" button to the bottom
        self.start_button = tk.Button(self.main_frame, text="Start", font=("Arial Bold", 16), relief="solid", borderwidth=2, width=20, height = 1, command=self.button_clicked)
        #start_button.pack(side=tk.LEFT, pady=200)
        self.start_button.place(relx=0.995, rely=0.995, anchor="se")
        # start_button.grid(row=0, column=0, padx=10, pady=10)


        # Add a "Settings" button to the bottom left corner
        self.settings_button = tk.Button(self.main_frame, text="Settings", font=("Arial Bold", 16), relief="solid", borderwidth=2, width=20, height = 1, command=lambda: self.show_settings())
        #, highlightthickness=1, borderwidth=3, highlightcolor="purple")
        #settings_button.pack(side=tk.RIGHT, padx=20, pady=200)
        # settings_button.grid(row=0, column=1, padx=10, pady=10)
        self.settings_button.place(relx=0.005, rely=0.995, anchor="sw")

        # Start the main event loop
        self.root.mainloop()

    def backToMain(self):
        self.main_frame.pack()
        self.settings_frame.pack_forget()
    
    def button_clicked(self):
        self.root.withdraw()
        gui = g.GUI(self)
        gui.set_mood(self.mood_selected.get())
    
    def show_settings(self):
        # Create a new frame for the settings screen
        self.settings_frame = tk.Frame(self.root, bg="white")
        self.settings_frame.pack(fill=tk.BOTH, expand=True)

        # Add some widgets to the settings screen
        self.settings_label = tk.Label(self.settings_frame, text="Settings", font=("Arial Bold", 24), width=12, bg="#192a3a", fg="#ffffff")
        self.settings_label.place(relx=0.5,rely=0.1,anchor="center")

        # Add a "Back" button to the settings screen
        back_button = tk.Button(self.settings_frame, text="Back", font=("Arial", 12), width=12)
        back_button.place(relx=0.5,rely=0.95,anchor="center")

        self.moods=[None, "Happy", "Joyful", "Serious", "Sad", "Upset", "Frustrated"]
        self.mood_selected = tk.StringVar(self.root)
        self.mood_selected.set("Select a mood")
        moodMenu = tk.OptionMenu(self.settings_frame, self.mood_selected, *self.moods, command=lambda: self.button_clicked())
        moodMenu.place(relx=0.5, rely=0.5, anchor="center")
        if self.mood_selected is not None:
            print("AYYYY " + str(self.mood_selected.get()))
            
        back_button.configure(command=lambda: self.backToMain())
        # Hide the original frame
        self.main_frame.pack_forget()
     
        

    # Function to be called when the button is clicked
    

    def show(self):
        self.root.deiconify()
        
if __name__ == '__main__':
    app = App()

    