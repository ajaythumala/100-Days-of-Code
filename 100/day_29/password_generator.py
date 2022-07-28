#the password generator project

#required modules
from random import choice, shuffle

#function for generating a character
def generate(lst,num):
    for _ in range(num):
        password.append(choice(char[lst]))

#character sets
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#stored in another list for referencing easily via index
char=[letters,numbers,symbols]       

#user greeting and input
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#creating list for password characters
password=[]

#generating password characters in order
def generate_pwd():
    global password
    password = []
    generate(0,4)
    generate(1,4)
    generate(2,4)

    #shuffling the order of the list
    shuffle(password)

    #joining elements of the password list into a string
    pwd=""
    for ch in password:
        pwd+=ch

    
    #printing final password string
    # print(pwd)
    return pwd



