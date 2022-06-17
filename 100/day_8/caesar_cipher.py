#the caesar cipher project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function for encoding or decoding given text
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""

  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    if char not in alphabet:
      end_text += char
      continue
    
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

def main():
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #bringing shift value to the range of 26 alphabets 
    #in case shift value is greater than 25
    shift=shift%26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

end = True
while end:
    main()
    again=input("Do you want to continue? 'Yes' or 'No'?\n").lower().strip()
    if again=="no":
        break