import random
import string

while True:

    print("Welcome to Collins's password picker!")

    adjectives = ["slow", "quick", "fat", "insane", "generous", "Inteligent", "quiet", "lovely", "Charming", "cool", "touchy", "smelly", "opportunity"]

    nouns = ["goat", "pineapple", "tea", "monkey", "sandy", "bag", "he", "dinasour", "hyiena", "rollercoaster", "cassava", "bulb", "lover", "spider"]

    colours = ["blue", "black", "white", "red", "yellow", "indigo", "neon", "green", "silver", "shinny"]

    adjective = random.choice(adjectives)

    noun = random.choice(nouns)

    number = random. randrange(0, 99)

    colour = random.choice(colours)

    speacial_character = random.choice(string.punctuation) 

    passwords = adjective + noun + str(number) + colour + speacial_character

    print(f"Your new password is: {passwords}")

    response = input("Would you like another password?  Yes/No  ")
    if response.lower()  == "no":
        break
