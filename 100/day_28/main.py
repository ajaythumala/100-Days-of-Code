from curses import start_color
from tkinter import *

from numpy import greater
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text = "t i m e r")
    check_label.config(text = "")
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    # global work_reps
    reps += 1

    work_sec = int(WORK_MIN * 60)
    short_sec = int(SHORT_BREAK_MIN * 60)
    long_sec = int(LONG_BREAK_MIN * 60)

    if(reps % 8 == 0):
        count_down(long_sec)
        label.config(text = "Long Break")
    elif(reps % 2 == 0):
        count_down(short_sec)
        label.config(text = "Short Break")
    else:
        count_down(work_sec)
        label.config(text = "Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # 03:35
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        global timer
        canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        start_timer()
        check_label.config(text = "✓" * (reps//2))
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(102, 136, text = "00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(column = 1, row = 1)

label = Label(text="T i m e r", bg = YELLOW, fg = "black",font = ("Tw Cen MT", 24), pady = 10)
label.grid(row = 0, column = 1)

start_button = Button(text="Start", command = start_timer)
reset_button = Button(text="Reset", command = reset_timer)
start_button.grid(row = 2, column = 0)
reset_button.grid(row = 2, column = 2)

check_label = Label(text="", bg = YELLOW, fg = "green",font = ("Tw Cen MT", 24))
check_label.grid(row = 3, column = 1)




window.mainloop()