#the tip calculator project

#user greeting
print("Welcome to the tip calculator program.")
print("I shall help you calculate the total amount and the split - inclusive of the tip %")

#user input
bill=float(input("What was the total bill? $"))
tip_p=int(input("How much tip would you like to give? 10, 12, or 15? "))
n_split=int(input("How many people to split the bill? (Enter '1' if there's no split): "))

#calculation
final_amount=round((bill*(1+(tip_p/100)))/n_split,2)

#user output
print("Here's amount you owe - {:.2f}".format(final_amount))