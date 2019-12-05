#!/usr/bin/python


#How tall is the three: 5

#                   (4 spaces)    #
#                   (3 spaces)   ###
#                   (2 spaces)  #####
#                   (1 spaces) #######
#                   (0 spaces)#########
#                   (4 spaces)    #

# Use 1 while loop 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 spacee : 7 hashes
# 0 spaces : 9 hashes

#need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height -1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and the 1 hash

# Get the numbers of rows for the tree
tree_height = input("How tall is the tree")

# Convert into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one has to start that will be incremented
hashes = 1

# Save stump spaces till later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while tree_height != 0:

#print the spaces
    for i in range(spaces):
        print(" ", end = '')

# Print the hashes
    for i in range(hashes)
        print('#', end='')

# Newline after each row is printed
    print()

# That spaces is decremented by 1 each time
    spaces -= 1

# That hashes is incremented by 2 each time
    hashes += 2

# Decrement tree height each time to jum out the loop
    tree_height -= 1

# Print the spaces before stump and then the hash

fori in range(stump_spaces):
        print(' ', end='')

print("#")
