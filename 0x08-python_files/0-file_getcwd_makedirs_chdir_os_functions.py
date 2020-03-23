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
