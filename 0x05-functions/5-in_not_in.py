#!/usr/bin/python3

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name')

name = input()

if name not in myPets:
    print('I dont have a  pet named ' + name)
else:
    print(name + ' Is my pet')
