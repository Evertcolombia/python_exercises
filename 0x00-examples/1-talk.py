#!/usr/bin/python3
name = ''  #creating a variable
while True:
    print('Who are you?')
    name = input()  #Taking input from user & storing it in name variable
    if name == 'joe':
        print('hello, joe what is the password? (it is a plant)')
        password = input()  #Taking input from user & storing it in password variable
        if password == 'weed':
            print (password)
            break
        else:
            continue
    else:
        print('Im fine. Who are you?')
        continue

print('Access successful')
