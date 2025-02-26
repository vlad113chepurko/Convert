import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Converter")
root.geometry("400x400")

class Convert:
    def __init__(self, value):
        self.value = value

    def logic(self):
        for widget in root.winfo_children():
            widget.destroy()

        label_1 = Label(root, text="You can convert the value to other types")
        label_1.pack()

        label_2 = Label(root, text="Choose the type you want to convert to: ")
        label_2.pack()

        label_3 = Label(root, text="1. Binary")
        label_3.pack()
        label_4 = Label(root, text="2. Octal")
        label_4.pack()
        label_5 = Label(root, text="3. Hexadecimal")
        label_5.pack()

        choise = Entry(root, width=50)
        choise.pack()

        submit = Button(root, text="Submit", command=lambda: self.choise_user(int(choise.get())))
        submit.pack()

    def choise_user(self, choise):
        result_label = Label(root, text="")
        result_label.pack()

        if choise == 1:
            result = self.convert_to_binary()
            result_label.config(text=f"Binary: {result}")
        elif choise == 2:
            result = self.convert_to_octal()
            result_label.config(text=f"Octal: {result}")
        elif choise == 3:
            result = self.convert_to_hexadecimal()
            result_label.config(text=f"Hexadecimal: {result}")
        else:
            result_label.config(text="Invalid")

    def convert_to_binary(self):
        return bin(self.value)

    def convert_to_octal(self):
        return oct(self.value)

    def convert_to_hexadecimal(self):
        return hex(self.value)

def command_convert():
    value = int(input.get()) 
    convert = Convert(value)
    convert.logic()

value = 0
label_enter_value = Label(root, text="Enter the value you want to convert: ")
label_enter_value.pack()

button_light_theme = Button(root, text="Light Theme", command=lambda: root.configure(bg="white"))
button_light_theme.pack()

button_dark_theme = Button(root, text="Dark Theme", command=lambda: root.configure(bg="#3d3d3d"))
button_dark_theme.pack()

input = Entry(root, width=50)
input.pack()

submit = Button(root, text="Submit", command=command_convert)
submit.pack()

root.mainloop()