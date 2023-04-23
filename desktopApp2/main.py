import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import filedialog
from PIL import ImageTk, Image
import subprocess

# Function to be called when the button is clicked
def button_clicked():
    # Run the selected Python script using the subprocess module
    file_path = "/Users/arshnoor-private/la-hacks-2023/src/pipline.py"
    subprocess.run(["python", file_path])

def show_settings():
    # Create a new frame for the settings screen
    settings_frame = tk.Frame(root, bg="white")
    settings_frame.pack(fill=tk.BOTH, expand=True)

    # Add some widgets to the settings screen
    settings_label = tk.Label(settings_frame, text="Settings Screen", font=("TkDefaultFont", 24))
    settings_label.pack(pady=20)

    # Add a "Back" button to the settings screen
    back_button = tk.Button(settings_frame, text="Back", command=lambda: settings_frame.pack_forget())
    back_button.pack(side=tk.BOTTOM, pady=20)

    # Hide the original frame
    main_frame.pack_forget()

# Create a window
root = tk.Tk()
root.geometry("550x550")
root.title("My App")

# Set the theme
style = ThemedStyle(root)
style.set_theme("adapta")

# Create a main frame for the start screen
# main_image = tk.PhotoImage(file="logo.png")
main_image = Image.open('logo.png')
newimage = (600, 600)
new_logo = main_image.resize(newimage)
newlogo = ImageTk.PhotoImage(new_logo)
main_frame = tk.Frame(root, width = newlogo.width(), height = newlogo.height(), bg="white")
background_label = tk.Label(main_frame, image=newlogo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
main_frame.pack(fill=tk.BOTH, expand=True)

# Add a logo to the center
# logo_image = tk.PhotoImage(file="logo.png")
# logo_image = logo_image.subsample(4)
# logo_label = tk.Label(main_frame, image=logo_image)

# logo_label.pack(pady=20)

# Add a "Start" button to the bottom
start_button = tk.Button(main_frame, text="Start", command=button_clicked)
#start_button.pack(side=tk.LEFT, pady=200)
start_button.pack( anchor="e", side="bottom")
# start_button.grid(row=0, column=0, padx=10, pady=10)


# Add a "Settings" button to the bottom right corner
settings_button = tk.Button(main_frame, text="Settings", command=show_settings)
#, highlightthickness=1, borderwidth=3, highlightcolor="purple")
#settings_button.pack(side=tk.RIGHT, padx=20, pady=200)
# settings_button.grid(row=0, column=1, padx=10, pady=10)
settings_button.pack( anchor="w", side="bottom")



#start_button.pack(side="bottom", padx=10, pady=10)
#settings_button.pack(side="bottom", padx=10, pady=10)
# main_frame.grid_rowconfigure(2, weight=1)

# Align the buttons to the bottom of the frame
# start_button.grid(row=2, column=1, sticky="S", padx=10, pady=10); settings_button.grid(row=2, column=2, sticky="S", padx=20, pady=10)

# Start the main event loop
root.mainloop()