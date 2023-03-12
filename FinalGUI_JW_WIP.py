"""  FinalGUI_JW_WIP.py

Johnny Wilder 03/06/23 
   A python GUI application for the final project that uses tkinter 
   and has multiple buttons, labels, user entry, as well as callback fxns
   and has second window functionality with image display in both windows.
"""
# Importing tkinter module
import tkinter as tk
from tkinter import * #imports all from tkinter to make ease of access calling
from tkinter import messagebox #import messagebox function from tkinter library

root = tk.Tk() 
root.title("My Application") # Creating main application window
root.geometry("1350x700")

image = tk.PhotoImage(file="image.png")#Creating an image and adding it to the main window
image_label = tk.Label(root, image=image)
image_label.image = image
image_label.pack()

labelframe= LabelFrame(root, text= "Hello All!", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "Purple",width= 1340, height= 400) #Creating a frame for the main window
labelframe.pack(expand= True, fill= BOTH)

label = tk.Label(labelframe, text="Welcome to my application!", font= ('Century 12 bold'), fg="Black", bg="Purple" ) # Creating a label and adding it to the main window
label.pack()

def validate_input(): # Defining a function to validate user input
    user_input = entry.get() #This function validates the user input in the entry box.
    
    if not user_input.isdigit(): # Checking if the user entered a number
        messagebox.showerror("Error", "Please enter a number!")
        return
    
    if not user_input: # Checking if the user entered a non-empty value
        messagebox.showerror("Error", "Please enter a value!")
        return

    user_input = int(user_input)  # Converting the user input to an integer
    messagebox.showinfo("User Input", f"You entered {user_input}.") # Displaying the user input

def open_second_window(): # Defining a function to open the second window
    second_window = tk.Toplevel(root) # This function opens the second window of the application.
    second_window.title("Second Window")  # Creating the second window

    label = tk.Label(second_window, text="This is the Calculator window!", font= ('Century 12 bold'), fg="Black", bg="Purple" )  # Creating a label and adding it to the second window
    label.pack()

    image = tk.PhotoImage(file="welcome2.png")  # Creating a welcome image and adding it to the second window
    image_label = tk.Label(second_window, image=image)
    image_label.image = image
    image_label.pack()

    class Calculator(tk.Frame):
        def __init__(self, master=None): #defining the calculator
            super().__init__(master)
            self.master = master
            self.master.title("Calculator")
            self.master.configure(bg='Purple')
            self.pack()
            self.create_widgets()

        def button_click(self, value): #adds button click fxn for the calculator
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + str(value))

        def calculate(self): #calculating insertion for the calculator
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        def clear_display(self):
            self.display.delete(0, tk.END)

        def create_widgets(self):
            self.display = tk.Entry(self, width=30, font=('Arial', 20), bg='White', fg='black')
            self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
            #adds button functions and numbers
            self.button_1 = tk.Button(self, text='1', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('1'))
            self.button_2 = tk.Button(self, text='2', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('2'))
            self.button_3 = tk.Button(self, text='3', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('3'))
            self.button_4 = tk.Button(self, text='4', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('4'))
            self.button_5 = tk.Button(self, text='5', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('5'))
            self.button_6 = tk.Button(self, text='6', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('6'))
            self.button_7 = tk.Button(self, text='7', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('7'))
            self.button_8 = tk.Button(self, text='8', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('8'))
            self.button_9 = tk.Button(self, text='9', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('9'))
            self.button_0 = tk.Button(self, text='0', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('0'))
            #adds calculator arithmetic fxns to widgets 
            self.button_add = tk.Button(self, text='+', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('+'))
            self.button_subtract = tk.Button(self, text='-', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('-'))
            self.button_multiply = tk.Button(self, text='*', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('*'))
            self.button_divide = tk.Button(self, text='/', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=lambda:self.button_click('/'))
            self.button_equals = tk.Button(self, text='=', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=self.calculate)
            self.button_clear = tk.Button(self, text='Clr', font=('Arial', 16), bg='White', fg='black', padx=10, pady=10, command=self.clear_display)
            #adds button locations for the calculator
            self.button_1.grid(row=1, column=0)
            self.button_2.grid(row=1, column=1)
            self.button_3.grid(row=1, column=2)
            self.button_4.grid(row=2, column=0)
            self.button_5.grid(row=2, column=1)
            self.button_6.grid(row=2, column=2)
            self.button_7.grid(row=3, column=0)
            self.button_8.grid(row=3, column=1)
            self.button_9.grid(row=3, column=2)
            self.button_0.grid(row=4, column=1)

            self.button_add.grid(row=1, column=3)
            self.button_subtract.grid(row=2, column=3)
            self.button_multiply.grid(row=3, column=3)
            self.button_divide.grid(row=4, column=3)
            self.button_equals.grid(row=4, column=2)
            self.button_clear.grid(row=4, column=0)
    GUI = Calculator(second_window)

    def display_message(): # Defining a function to display a message box
        messagebox.showinfo("Message Box", "Hello, World!")  # This function displays a message box with a custom message.

    button = tk.Button(second_window, text="Click me!", command=display_message) # Creating a button and adding it to the second window
    button.pack()

    
    def close_second_window(): # Defining a function to close the second window
        second_window.destroy() # This function closes the second window of the application.
    
    exit_button = tk.Button(second_window, text="Exit", command=close_second_window) # Creating an exit button and adding it to the second window
    exit_button.pack()

label = tk.Label(labelframe, text="Please enter a number value to validate input:", font= ('Century 12 bold'), fg="Black", bg="Purple" )
label.pack(padx=5, pady=5)
entry = tk.Entry(labelframe) # Creating an entry box and adding it to the main window
entry.pack()

validate_button = tk.Button(labelframe, text="Validate", command=validate_input) # Creating a button to validate user input
validate_button.pack(padx=5, pady=5)

label = tk.Label(labelframe, text="Click button below to go to Calculator", font= ('Century 12 bold'), fg="Black", bg="Purple" )# adds label for calculator window direction
label.pack(padx=5, pady=5)

open_second_window_button = tk.Button(labelframe, text="Go to Calculator", command=open_second_window) # Creating a button to open the second window
open_second_window_button.pack(padx=10, pady=5)

def exit_application(): # Defining a function to exit the application
    root.destroy() # This function exits the application.

exit # Creating an exit button and adding it to the main window

root.mainloop() #running the program