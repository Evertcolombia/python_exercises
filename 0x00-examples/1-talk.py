#!/usr/bin/python3
name = ''
while True:
    print('Who are you?')
    name = input()
    if name == 'joe':
        print('hello, joe what is the password? (it is a plant)')
        password = input()
        if password == 'weed':
            print (password)
            break
        else:
            continue
    else:
        print('Im fine. Who are you?')
        continue

print('Access successful')
