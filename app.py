""" Interactive English Dictionarity"""

# Importing the standard library JSON
# Importing the standard library difflib and SequenceMatcher
# Importing the standard library get_close_matches
# Importing sys to end the script
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import sys

# Loading the json data file
data = json.load(open("data.json"))
# Function to return the definition of the word

while True:
    def translate(w):
        w = w.lower()  # Converts the given word to lower case
        if w in data:  # If the given word exists in the data
            return data[w]  # Shows the definition of the word
        elif w.title() in data:  # If the lower word(converted to title) exists on data
            return data[w.title()]  # Shows the definition of the Title word
        elif w.upper() in data:  # If the lower word(converted to upper) exists on data
            # Show to definition of the upper word if exists
            return data[w.upper()]

        elif len(get_close_matches(w, data.keys())) > 0:  # If exists more any words on the list
            yn = input(
                f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes or N if no: ")  # Ask to give definition of the correct word
            if yn == "y":  # If user inputs "Y"
                # Return the definition of the word
                return data[get_close_matches(w, data.keys())[0]]
            elif yn == "n":
                return "The word doesn't exists"
            else:
                return "We didn't understand your entry"
        else:
            return "The word doesn't exists"

    # User input to return the word
    word = input("Enter word: ")
    if word == "exit_program":
        sys.exit()
    else:
        pass
    # The output is the function of the given word
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
