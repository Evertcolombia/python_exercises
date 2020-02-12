#!/usr/bin/python3

def isPhoneNumber(text):

    # Verificate that the phone has 12 digist counting '-'
    if len(text) != 12:
        return False

    # travere the fisrt 3 and ask if not is decimal the content in text[i] return false
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    # if the separator is not a '-' return false
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    #if pass the tests return true
    return True

