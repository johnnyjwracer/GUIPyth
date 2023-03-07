
import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.master.configure(bg='purple')
        self.pack()
        self.create_widgets()

    def button_click(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(value))

    def calculate(self):
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
        self.display = tk.Entry(self, width=30, font=('Arial', 20), bg='white', fg='black')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        #adds button functions and numbers
        self.button_1 = tk.Button(self, text='1', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('1'))
        self.button_2 = tk.Button(self, text='2', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('2'))
        self.button_3 = tk.Button(self, text='3', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('3'))
        self.button_4 = tk.Button(self, text='4', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('4'))
        self.button_5 = tk.Button(self, text='5', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('5'))
        self.button_6 = tk.Button(self, text='6', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('6'))
        self.button_7 = tk.Button(self, text='7', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('7'))
        self.button_8 = tk.Button(self, text='8', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('8'))
        self.button_9 = tk.Button(self, text='9', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('9'))
        self.button_0 = tk.Button(self, text='0', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('0'))
        #adds calculator arithmetic fxns to widgets 
        self.button_add = tk.Button(self, text='+', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('+'))
        self.button_subtract = tk.Button(self, text='-', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('-'))
        self.button_multiply = tk.Button(self, text='*', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('*'))
        self.button_divide = tk.Button(self, text='/', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=lambda:self.button_click('/'))
        self.button_equals = tk.Button(self, text='=', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=self.calculate)
        self.button_clear = tk.Button(self, text='Clr', font=('Arial', 16), bg='white', fg='black', padx=10, pady=10, command=self.clear_display)
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

root = tk.Tk()
GUI = Calculator(root)
root.mainloop()