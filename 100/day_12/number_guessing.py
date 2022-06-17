#the number guessing game project

import random

#number of lives remaining
def lives_remaining():
  global lives
  print(f"---You have {lives} attempts remaining to guess the number---")

#setting lives based on difficulty
def set_lives(difficulty):
  global lives
  if difficulty=="easy":
    lives=10
    return 1
  elif difficulty=="hard":
    lives=5
    return 1
  else:
    print("---Please enter valid input---")
    return 0

#function to reduce lives
def reduce_lives():
  global lives
  lives-=1

#function to evaluate guess
global key
def evaluate(guess):
  # print(key)
  if guess<key:
    print("---Too low---")
  elif guess>key:
    print("---Too high---")
  else:
    print(f"---You got it! {guess} is correct!---")
    return 1

#game code
def play_game():
  print("---Welcome to the number guessing game!---")
  print("---I'm thinking of a number between 1 and 100---\n")
  
  incorrect=0
  while(incorrect==0):
    easy_or_hard=input("Please choose a difficulty. Enter 'easy' or 'hard': ")
    incorrect=set_lives(easy_or_hard)
    
  while(lives>0):
    lives_remaining()
    
    #take input
    guess_num=int(input("\nMake a guess: "))
    #evaluate input
    eval=evaluate(guess_num)
    #break if input matches
    if eval==1:
      break
    #reduce lives for making a guess
    reduce_lives()

#main code
while(1>0):
  lives=0
  key=random.randint(1,100)
  print("** For testing purposes, the key is",key,"**")
  play_game()

  invalid=0
  while(invalid==0):
    again=input("\nDo you want to play again? Enter 'y' or 'n': ")
    if again=="y":
      print("----------------------\n\n")
      break
    elif again=="n":
      quit()
    else:
      print("---Please enter valid input---")

