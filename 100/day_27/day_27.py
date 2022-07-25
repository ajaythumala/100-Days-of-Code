# import tkinter
from tkinter import *

def button_clicked():
    # print("I got clicked")
    new_text = input.get()
    print(new_text)
    my_label.config(text = new_text)

window = Tk()
window.title("Hello Window")
window.minsize(width = 500, height = 300)
# window.config(padx = 100, pady = 200) #padding

# creating components to put in the window

# Label
my_label = Label(text = "Hello Label", font = ("Verdana", 24, "bold"))
my_label["text"] = "New Hello Label"
my_label.config(text = "New Hello Label")
#specifiy how label is layed out
# my_label.pack(side = "left")
# my_label.pack()
# my_label.place(x = 50, y = 110)
my_label.grid(column = 0, row = 0)
my_label.config(padx = 50, pady = 50)

# Buttons
button = Button(text = "Hello Button", command = button_clicked)
# button.pack()
button.grid(column = 1, row = 1)

# Entry ss
input = Entry(width = 10)
# input.pack()
input.grid(column = 3, row = 2)

new_button = Button(text = "New Button")
new_button.grid(column = 2, row = 0)





window.mainloop()

# Notes:
# **kw
'''
advanced arguments:
**args
1. arg = ... => default value is assigned.

def add(*args):
    print(sum(args))
add(1, 2, 3, 4)

**kwargs
def calculate(**kwargs):
    print(kwargs)
calculate(add = 3, multiply = 5)

You can initialize an object of a class
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make = "Ford", model = "GT")
'''