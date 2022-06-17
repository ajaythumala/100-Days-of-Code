print('''
*******************************************************************************
88                                                                       88  
88                                              ,d                       88  
88                                              88                       88  
88,dPPYba,  ,adPPYYba, 88       88 8b,dPPYba, MM88MMM ,adPPYba,  ,adPPYb,88  
88P'    "8a ""     `Y8 88       88 88P'   `"8a  88   a8P_____88 a8"    `Y88  
88       88 ,adPPPPP88 88       88 88       88  88   8PP""""""" 8b       88  
88       88 88,    ,88 "8a,   ,a88 88       88  88,  "8b,   ,aa "8a,   ,d88  
88       88 `"8bbdP"Y8  `"YbbdP'Y8 88       88  "Y888 `"Ybbd8"'  `"8bbdP"Y8  
                                                                             
*******************************************************************************
''')


again=None

while(again!=0):
  print("Welcome to The Scary Haunted House")
  print("Your mission is to survive.\nGood Luck\n\n\n") 
  print("You can type in lowercase, no problem. Yo boi using the lower() function innit.")

  

  partner=(input("Choose your partner :\nPavan - Ajay - Vishal - Abhinav\n\n\n")).lower()

  if partner=="pavan":
    print("\n\nThe door closes behind you\nPavan stabs you in the back\nYou are dead.\n   The End")
  elif partner=="ajay":
    print("\n\nYou kill yourself\n   The End")
  elif partner=="abhinav":
    print("\n\nAbhinav is scared\nSo you both don't enter the house.\nYou survive.\nCongratulations! :)")
  elif partner=="vishal":
    print("\n\nGood choice\nOkay, open the door in front of you.")
    # open=(input("Choose\n'Open' or 'No'?\n\n\n")).lower()
    i=0
    while(i==0):
      open=(input("\n\nChoose\n'Open' or 'No'?\n\n\n")).lower()
      if open=="open":
        print("\n*jumpscare*\nHey guys! This is HolyFrenchFry\n")
        print("You are dead\n   The End")
        break
        
      else:
        #print("You have ruined the game. Poda.\n   The End.")
        print("\n\nJust open the door man")
        continue
        
  else:
    print("\n\nEnter the name correctly please :) \n\n\n")
    continue
  ag=(input("\n\n\nDo you want to play again? Yes or No? ")).lower()
  if ag=="yes":
    continue
  else:
    break

print("\n\n\nThank you playing The Scary Haunted House. Goodbye :)")