import random

#ASCII ART
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#function for displaying choices
def printer(d,p):
  if d==0:
    print(p,"Chose rock")
    print(rock)
  elif d==1:
    print(p,"Chose paper")
    print(paper)
  elif d==2:
    print(p,"Chose scissors")
    print(scissors)
  else:
    print("Invalid Choice")

#choices 
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice=random.randint(0,2)

print("\n")

#displaying player choices 
printer(choice,"You")
printer(pc_choice,"Computer")

#game logic
if choice > pc_choice:
  print("You Win!")
elif choice==0 and pc_choice==2:
  print("You Win!")
elif choice==pc_choice:
  print("That's a draw")
else:
  print("You lose :(")


