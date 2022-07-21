from turtle import Screen, Turtle
import pandas
from states import States_Screen

states_data = pandas.read_csv("50_states.csv") 
states_set = set(states_data["state"]) 
image = "blank_states_img.gif"
screen = Screen()
screen.addshape(image)
turtle = Turtle(shape = image)
states_screen = States_Screen()
num_states = states_data["state"].size
guessed_states = set()

correctly_guessed = 0
while correctly_guessed != num_states:
    answer = screen.textinput(title = "Guess a state.", prompt = "What's another state name")
    answer = str(answer).title()
    if answer in states_set:
        correctly_guessed += 1
        guessed_states.add(answer)
        pos = states_data[states_data.state == answer]
        states_screen.update_screen(answer, (int(pos.x), int(pos.y)) )
    elif answer == "Exit":
        missed_states = [state for state in states_data["state"] if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break





