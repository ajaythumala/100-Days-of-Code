import pandas
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

dic = {row.letter:row.code for (index, row) in nato_data.iterrows()}

word = input("Enter a word : ").upper()
print([dic[letter] for letter in word])

