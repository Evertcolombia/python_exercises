#!/usr/bin/python

# Receive the message to encrypt and the number of characters to shift
message = input("Enter your Message : ")
key = int(input("How many charactter should we shift (1-26) "))

# Prepare the secret message
secret_message = ""

# cycle through each character in the message
for char in message:

    # If it isn't a letter then keep it as is
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():

            # If bigger then Z Substract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26

        # Do the same for lower case
        else:
            if char_code > ord('z'):
                char_code -= 26

            if char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        secret_message += chr(char_code)
        
    # If not a letter leave character as is
    else:
        secret_message += char

print("Encrypted : ", secret_message)

# To decrypt the only thing that changes is the sign of the key
key = -key

orig_message = ""

    # The same as about

# cycle through each character in the message
for char in secret_message:

    # If it isn't a letter then keep it as is
    if char.isalpha():

        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key

        # If uppercase then compare to uppercase unicodes
        if char.isupper():

            # If bigger then Z Substract 26
            if char_code > ord('Z'):
                char_code -= 26

            # If smaller than A add 26
            if char_code < ord('A'):
                char_code += 26

        # Do the same for lower case
        else:
            if char_code > ord('z'):
                char_code -= 26

            if char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        orig_message += chr(char_code)

    # If not a letter leave character as is
    else:
        orig_message += char

print("Decrypted : ", orig_message)
