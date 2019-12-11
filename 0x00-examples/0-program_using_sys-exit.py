#!/usr/bin/python3
import sys

while True:
    print('type exit to exit')
    response = input()
    if response == 'exit':
            print('correct exit')
            #call the sys module to exit the program
            sys.exit()
    print('You tiped ' + response + '.')
