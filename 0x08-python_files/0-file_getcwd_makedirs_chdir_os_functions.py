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

# change the current directory
os.chdir('/home/fantasma/Desktop/my-project')

#Create A folder from code
os.makedirs('/home/fantasma/Desktop/my-project/Web_scrapping/proof')
os.makedirs('/home/fantasma/Desktop/my-project/Web_scrapping/proof2/other')
