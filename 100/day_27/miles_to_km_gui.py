from tkinter import *


window = Tk()
window.title("Miles to KM GUI")
window.minsize(200, 100)
window.config(padx = 50, pady = 50)

# What we need:
'''
1. text field to get input
2. label text to display result
3. button to trigger computation
4. label text to specify units or describe meaning of action.
5. set elements by grid
5. program trigger, computation and display of result.
'''

# 1.
miles = Entry(width = 10)
miles.grid(column = 1, row = 0)


# 2.
result = Label(text = "result", font = ("Verdana", 14, "bold"), pady = 30)
result.grid(column = 1, row = 1)

# 5.
def calculate():
    try:
        miles_val = float(miles.get())
    except:
        result.config(text = "Invalid Value")
        return
    result.config(text = f"{miles_val * 1.60934}")



# 3.
button = Button(text = "Calculate", command = calculate)
button.grid(column = 1, row = 2)

# 4. 
equal_to = Label(text = "equal to", font = ("Verdana", 14), padx = 20)
equal_to.grid(column = 0, row = 1)

miles_unit = Label(text = "miles", font = ("Verdana", 14), padx = 30)
miles_unit.grid(column = 2, row = 0)

km_unit = Label(text = "km", font = ("Verdana", 14))
km_unit.grid(column = 2, row = 1)

window.mainloop()