#!/usr/bin/python

# Ask for a string
orig_string = input("Convert to Acronym : ")

# Convert the string to uppercae
orig_stringt = orig_string.upper()

# Convert the string in a list
list_of_words = orig_string.split()

# Cycle through the list
for word in list_of_words:

    # Get the 1st letter of the word and eliminate the newlinw
    print(word[0], end="")

# Add a new line
print()
