from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# importing data
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    data = pandas.read_csv("./data/french_words.csv")
data_dictionary = {}
words_to_learn = []
for i in data.index:
    data_dictionary[data['French'][i]] = data['English'][i]
    words_to_learn.append(data["French"][i])

# tk window
window = Tk()
window.title("Flashcard App")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

#------------------------------------ variables and functions ------------------------------------#
front_img = PhotoImage(file = "./images/card_front.png")
back_img = PhotoImage(file = "./images/card_back.png")
images = [front_img, back_img]
word_index = None
isFront = True

def right():
    if isFront:
        return
    words_to_learn.pop(word_index)
    switch()

def wrong():
    if isFront:
        return
    switch()

def new_word():
    global word_index
    rand_index = randint(0, len(words_to_learn) - 1)
    word_index = rand_index
    word = words_to_learn[rand_index]
    return word

def next_question():
    canvas.itemconfig(language_text, text = "French", fill = "black")
    canvas.itemconfig(word_text, text = new_word(), fill = "black")

def answer():
    canvas.itemconfig(language_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, text = data_dictionary[words_to_learn[word_index]], fill = "white")

def switch():
    global isFront

    canvas.itemconfig(canvas_img, image = images[isFront])
    if not isFront:
        next_question()
        isFront = True
        window.after(3000, switch)
    else:
        answer()
        isFront = False

#-------------------------------------------------------------------------------------------------#

#------------------------------------ canvas ------------------------------------#
canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 263, image = front_img)

#canvas text
language_text = canvas.create_text(400, 150, text = "", fill = "black", font = (FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text = "", fill = "black", font = (FONT_NAME, 40, "bold"))
canvas.grid(row = 0, column = 0,columnspan = 2) #placing canvas and elements
#--------------------------------------------------------------------------------#

#------------------------------------ buttons ------------------------------------#
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image = right_image, highlightthickness = 0, bg = BACKGROUND_COLOR, borderwidth = 0, command = right)
right_button.grid(row = 1, column = 0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness = 0, bg = BACKGROUND_COLOR, borderwidth = 0, command = wrong)
wrong_button.grid(row = 1, column = 1)
#--------------------------------------------------------------------------------#

#-------------------------------------initial code-------------------------------#
canvas.itemconfig(language_text, text = "French", fill = "black")
canvas.itemconfig(word_text, text = new_word(), fill = "black")
window.after(3000, switch)

window.mainloop()
#--------------------------------------------------------------------------------#

#------------------------------saving progress------------------------------#
to_learn_dic = {
    "French" : words_to_learn,
    "English" : [data_dictionary[i] for i in words_to_learn]
}

to_learn = pandas.DataFrame.from_dict(to_learn_dic)
to_learn.to_csv("./data/words_to_learn.csv")
#---------------------------------------------------------------------------#