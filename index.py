import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Converter")
root.geometry("400x400")

root.configure(bg="white")

class Convert:
    def __init__(self, value):
        self.value = value

    def logic(self):
        for widget in root.winfo_children():
            widget.destroy()

        label_1 = Label(root, text="You can convert the value to other types")
        label_1.pack()

        listbox = Listbox(root)
        listbox.pack()

        list = ['Binary', 'Octal', 'Hexadecimal']
        for item in list:
            listbox.insert(END, item)

        button_for_listbox = Button(root, text="Submit", command=lambda: self.convert(listbox.get(listbox.curselection()))) 
        button_for_listbox.pack()
    def convert(self, value):
        if value == "Binary":
            label = Label(root, text=self.convert_to_binary())
            label.pack()
        elif value == "Octal":
            label = Label(root, text=self.convert_to_octal())
            label.pack()
        elif value == "Hexadecimal":
            label = Label(root, text=self.convert_to_hexadecimal())
            label.pack()

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

button_light_theme = Button(root, text="Light Theme", bg='pink', command=lambda: root.configure(bg="white"))
button_light_theme.pack()

button_dark_theme = Button(root, text="Dark Theme", bg='pink', command=lambda: root.configure(bg="#3d3d3d"))
button_dark_theme.pack()

label_enter_value = Label(root, text="Enter the value you want to convert: ", font=("Arial", 12))
label_enter_value.pack()


input = Entry(root, width=50)
input.pack()

submit = Button(root, text="Submit", command=command_convert)
submit.pack()

root.mainloop()