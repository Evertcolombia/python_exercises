#!/usr/bin/python

#user enter the calculation: num1 'operator' num2
#5 * 6 = 30

# Store the user input of  2 numbers an the operator
num1, operator, num2 = input('Enter calculation: ').split()

# Convert the strings  into integers
num1 = int(num1)
num2 = int(num2)

# if operator = '+' then we need to provide output based on addition
# Print the result
if operator == "+":
    print('{} + {} = {}'.format(num1, num2, num1+num2))
elif operator == "-":
    print('{} - {} = {}'.format(num1, num2, num1-num2))
elif operator == "*":
    print('{} * {} = {}'.format(num1, num2, num1*num2))
elif operator == "/":
    print('{} / {} = {}'.format(num1, num2, num1/num2))
else:
    print("invalid operation: ")
    print()
    print("User either + - * or / next time")


