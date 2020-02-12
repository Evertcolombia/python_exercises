#!/usr/bin/python3

isPhoneNumber = __import__('look_for_phone').isPhoneNumber
message = "Call me at 415-555-1011 is my office"

for i in range(len(message)):
    chunk = message[i:i+12]

    if isPhoneNumber(chunk):
        print('Phone Number found: ' + chunk)
print('done')

