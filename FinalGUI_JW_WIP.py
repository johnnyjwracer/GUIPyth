"""  FinalGUI_JW_WIP.py

Johnny Wilder 03/06/23 
   A python GUI application for the final project that uses tkinter 
   and has multiple buttons, labels, user entry, as well as callback fxns
   and has second window functionality with image display in both windows.
   Work in Progress
"""
# Importing tkinter module
import tkinter as tk
from tkinter import messagebox #import messagebox function from tkinter library

root = tk.Tk() 
root.title("My Application") # Creating main application window

label = tk.Label(root, text="Welcome to my application!") # Creating a label and adding it to the main window
label.pack()

image = tk.PhotoImage(file="image.png")#Creating an image and adding it to the main window
image_label = tk.Label(root, image=image)
image_label.image = image
image_label.pack()

def exit_application(): # Defining a function to exit the application
    root.destroy() # This function exits the application.

exit # Creating an exit button and adding it to the main window

root.mainloop()