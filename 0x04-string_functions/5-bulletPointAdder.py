#!/usr/bin/python3
# Add bulet point to the strar of  ech line of a test copy from the browser

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for line in range(len(lines)):
    lines[line] = '* {}'.format(lines[line])

text = '\n'.join(lines)
pyperclip.copy(text)
