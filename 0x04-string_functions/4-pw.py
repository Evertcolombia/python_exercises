#!/usr/bin/python3
# An nsecure password locker program

from sys import argv, exit
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMjux',
        'blog': 'VmAl3ls5wtt42dtre4',
        'lugagge': '12345'}

if len(argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    exit()

account = argv[1] # account name

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for {} copied to clipboard is {}'.format(account,
        pyperclip.paste()))

else:
    print('There is not an account named: {}'.format(account))


