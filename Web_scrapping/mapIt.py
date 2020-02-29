#!/usr/bin/python3

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:

    adress = ''.join(sys.argv[1:])
    print(adress)

else:
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)
