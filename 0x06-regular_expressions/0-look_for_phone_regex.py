#!/usr/bin/python3

#import regex library
# regex : are descriptions for a pattern of text

import re

# Create a regex object
PhoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# looking for a match using the regex object
mo = PhoneNumberRegex.match('This is my number 415-555-1151.')
# If there a re a match object use group() method to get the
# text that is match from the matchin string
final = mo.group()

print("Phone number found: " + final)

#it works on the python console
