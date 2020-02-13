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
if mo:
    print("Phone number found: " + mo.group())


####################################################################

# Groups method returns a tuple of the groups ext in the match object

#also you can use parentesses to separate the patter yo look by groups
phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

# Create a match object or almost try
match_object = phoneRegex.search('This is my number 131-444-1511.')

# test if the 'mo' is true and set the groups in diffrent variables
# ussing difrent assignement
if match_objects:
    areaCode, mainNumber =  match_objects.groups()

    print(areCode)
    print(mainNumber)


  
#################################################################
#also yo cans use parentsss as part of a group  use the follow expression (\(content\))
phoneRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')

#creat match object
mo = phoneRegex.search('My number is : (131) 444-1511.')

#assign the groups to diffrennt variabls if they exits
if mo:

    areaCode, mainNumber = mo.groups
    print(areaCode)
    print(mainNumber)

    #see all the groups
    print(mo.groups)



#it works on the python console
