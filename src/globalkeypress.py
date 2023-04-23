from tkinter import *
import keyboard

root = Tk()

def key_press(event):
    key = event.char
    print(f"'{key}' is pressed")
root.geometry("800x400")
root.attributes('-alpha',0.5)

keyboard.add_hotkey('esc', lambda: root.destroy())
root.mainloop()