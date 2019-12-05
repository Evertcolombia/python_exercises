#!/usr/bin/python

heart_height = 10
tmp_height = 10
spaces = 4
tmp_spaces = 4
stump_spaces = 4
hashes = 1

while heart_height != 0:

    if heart_height >= (tmp_height / 2) + 1:

        for i in range(spaces):
            print(" ", end='')
        for i in range(hashes):
            print('#', end='')
        if heart_height < tmp_height:
            print("#", end='')
        else:
            print(" ")
        for i in range(hashes):
            print('#', end='')
        for i in range(spaces):
            print(" ", end='')
        print()
        hashes += 1
        spaces -= 1
        heart_height -= 1,

    elif heart_height <= (temp_height / 2) and (heart_height > 1):
        
        hashes -= 1
        spaces += 1

        for i in range(spaces):
            print(" ", end='')
        for i in  range(hashes):
            print("#", end='')
        print("#", end='')
        
        for i in  range(hashes):
            print("#", end='')
        for i in range(spaces):
            print(" ", end='')
        print()
        heart_heigth -= 1

    else:
        for i in range(tmp_spaces + 1):
            print(" ", end='')
            print("#")

        heart_height -= 1
