#!/usr/bin/python

# We'll provide different output based on age
# 1 - 18 -> Important
# 21, 50 > 65 -> Important
# All others -> Not important

# Receive age and store in age
age = eval(input("Enter age: "))

# and : If both are trure returns true
# or : if either condition is true then true
# not : convert a true codition into a false

# if age is both greater than or equal to 1 and less  or equal to 18
if (age >= 1) and (age <= 18):
    print("Important birthday")

# if age  is 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65 and then convert true to false and vice versa
elif not(age < 65):
    print("Important Birthday")

# Else not important
else:
    print("Not important Birthday")
