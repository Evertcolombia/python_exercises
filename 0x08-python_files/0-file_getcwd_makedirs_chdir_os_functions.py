#!/usr/bin/python3

import os

# Print the current working directory
current_working_directory = os.getcwd()
print(current_working_directory)
print()

# Create paths recursive
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for file in myFiles:
    print(os.path.join('/home/fantasma/Desktop/my-project/Web_scrapping', file))
print()

totalsize = 0
for el in os.listdir(os.getcwd()):
    try:
        print('file {} - size: {}'.format(el, os.path.getsize(el)))
        totalsize = totalsize + os.path.getsize(el)
    except:
        pass

print(totalsize)
# change the current directory
os.chdir('/home/fantasma/Desktop/my-project')

#Create A folder from code
try:
    os.makedirs('/home/fantasma/Desktop/my-projectproof')
    os.makedirs('/home/fantasma/Desktop/my-project/proof2/other')
except:
    print('Folder name is yet create')
    pass

# Know the abosulte path from a position
z = os.path.abspath('.')
print(z)
# know if a paht is an absolute path
a = os.path.isabs('.')
print(a)
b = os.path.isabs('/home/fantasma/Desktop/my-project/python_exercises/0x08-python_files')
print(b)

# know the absolute path and ask if is exist
c = os.path.isabs(os.path.abspath('.'))
print(c)

#Use the Shelve module so save variables in binary files in a program

import shelve

shelfFile = shelve.open('mydata')
cats = ['zophie', 'nana', 'pooka']
shelfFile['cats'] = cats
shelfFile.close()

print('now you have a mydata binary file')
print('reopening the file')

shelfFile = shelve.open('mydata')
type(shelfFile)

print('see the bnary File content')
for cat in shelfFile['cats']:
    print('cat name {}'.format(cat))

shelfFile.close()


#saving variables with the pprint.pformat() function

#this part do a program that prints all the key values in a dictionary
#that are stored in number for the total that each one appears i the message
#
import pprint

message = 'It was a bright cold day in April, and the  clocks were striking thirteen.'

charCount = {}

for character in message:
    charCount.setdefault(character, 0) #if not a value set it at 0
    charCount[character] = charCount[character] + 1

# pprint() will pretty print the key and values of a dictionary
pprint.pprint(charCount)


cats = [{'name': 'Zohpie', 'desc': 'chubby'}, {'name': 'pooka', 'desc': 'fluffy'}]

pprint.pformat(cats)

current = os.path.join(os.getcwd(), 'mycats.py')
with open(current, 'w', encoding='utf-8') as f:
    print('saving cats')
    f.write('cats = ' + pprint.pformat(cats) + '\n')


