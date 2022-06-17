
#the hangman project

import random
from hangman_resources import stages, logo, word_list

#function to evaluate character guess
def guess_eval(char):
    global display, chosen_word, word_length, lives

    #Check guessed letter
    if char in display:
        print(f"\nYou've already guessed {char}")
    elif char in chosen_word:
        for position in range(word_length):
            letter=chosen_word[position]
            if letter == char:
                display[position] = letter
    else:
      lives-=1
      print(f"\n{char} is not in the word")


print(logo)

#setting no. of lives
lives = 6

#choosing a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(stages[lives])

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#starting the game
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: \n").lower()

    guess_eval(guess)

    #Joining all the elements in the list and turn it into a String.
    print(stages[lives])
    joined=f"{' '.join(display)}\n"
    print(joined)

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win!!:)")
    elif lives==0:
        end_of_game = True
        print("You Lose. :(")


    
    