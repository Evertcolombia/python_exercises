#!/usr/bin/python

# Problem : Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter miles 5
# 5 miles equals 8.04 kilometers

# Ask the user to input miles and assign it to the miles variable
miles = input('Enter Miles: ')

# Convert from string to integer
miles = int(miles)

# Perform calculation by multiplying 1.60934 time miles
kilometers = miles * 1.60934

# Print result using format()
print('{} miles equals {} kilometers'.format(miles, kilometers))
