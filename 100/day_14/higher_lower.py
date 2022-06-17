#the higher lower game project

from art import logo, vs
from game_data import data
import random

#randomly generating a subject to be used in the game
def generate_subject(dataset):
  return random.choice(dataset)

#presenting the user with the subjects to be compared
def print_for_user(A, B):
  print("Compare A:", A['name'], ", a", A['description'], ", from", A['country'])
  print("---for testing purposes--- follower count =", A['follower_count'] )
  print(vs)
  print("Against B:", B['name'], ", a", B['description'], ", from", B['country'])
  print("---for testing purposes--- follower count =", B['follower_count'] )

#comparing follower count and evaluating the choice of user
def compare_subjects(guess, A, B):
  if A['follower_count'] > B['follower_count']:
    return guess == 'A'
  else:
    return guess == 'B'
  
def main():
  print(logo)
  print("Welcome to higher or lower!")
  score=0
  no_repeats = [] #list keeping track of subjects to not be repeated

  a = generate_subject(data)
  no_repeats.append(a)
  
  result = True
  while result:
    b = generate_subject([i for i in data if i not in no_repeats])
    #ensuring that new subjects selected are not repeated in the game
    no_repeats.append(b)
    
    print_for_user(a, b)
    a_or_b = input("Who has more followers? A or B?\n").upper().strip()

    result = compare_subjects(a_or_b, a, b)

    # print(logo)
    print("----------------------------------------------------")
    if result: #if the user's choice is correct
      score+=1
      print(f"Correct! Your score is {score}")
      a = b #subject B becomes subject A for the next round
      # continue
    else: #if the user's choice is incorrect
      print(f"Sorry, that was incorrect, your final score is {score}")


#allowing the user to play again
ended = False
while not ended:
  main()
  
  again = input("Do you want to play again? Type 'y' or 'n' : ")
  if again == 'n':
    break
  elif again == 'y':
    continue
  