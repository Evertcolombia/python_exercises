#!/usr/bin/python

# x will always be the 1st value received and you only will
# deak with addition

# Recieved the strng and split the string into variables
def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()

    # Convert the strings into int elements
    num1, num2 = int(num1), int(num2)

    # Convert the resulto into a string and join it to the string "X = "
    return  "x = " + str(num1 - num2)


# print()
print(solve_eq("x + = 9"))
