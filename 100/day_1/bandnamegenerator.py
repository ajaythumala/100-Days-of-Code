#the band-name generator project.

#user greeting
print("Welcome to the band name generator!")
print("Please answer the prompts below to receive an amazing band name!")
print("Yes, an amazing band name :)")

#user input
name=input("---Please enter - the name of your uncle or aunty: ").title()
feeling=input("---Please enter - an emotion that drives your music: ").lower()

#band name output
band_name=f"{name} is feeling {feeling}"

#output for the user
print(f"The name of your band could be,\n   {band_name}")