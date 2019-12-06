#!/usr/bin/python

rand_string = "     This is an important string     "

# Cut all the false spaces or characters from the left
rand_string = rand_string.lstrip()
print(rand_string)

# Cut all the false spaces or characters from the right
rand_string = rand_string.rstrip()
print(rand_string)

# Cut all the false spaces or characters from the both sides
rand_string = rand_string.strip()
print(rand_string)

# Capitalize. uppercase, lowercase
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

# Print elements from a list

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

# Create a list from an array and print each element
a_list_2 = rand_string.split()
for i in a_list_2:
        print(i)

# Count of specific characters of a string
print("How many is : ", rand_string.count("is"))

# index of a index of a strng
print("Where is string : ", rand_string.find("string"))

# Replace a index from a string
print(rand_string.replace("an ", "a kind of "))
