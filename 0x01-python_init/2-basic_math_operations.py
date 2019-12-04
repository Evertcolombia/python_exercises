#!/usr/bin/python

# Ask the user to input 2 values and store them in variables num1 num2
num1, num2 = input('Enter 2  numbers: ').split()


# Convert the strins into regular numbers Integer
num1 = int(num1)
num2 = int(num2)


# Add the values entered ans store  in sum
sume = num1 + num2


# Substract and store difference
difference = num1 - num2


# Multyply The values and store in product
multyply = num1 * num2


# Divide the values and store in quotient
divide = num1 / num2


# Use modulus on the values to find the reminder
modulus = num1 % num2


# Print the results
print("{} + {} = {}".format(num1, num2, sume))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, multyply))
print("{} / {} = {}".format(num1, num2, divide))
print("{} % {} = {}".format(num1, num2, modulus))

