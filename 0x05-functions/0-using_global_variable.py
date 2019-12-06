#!/usr/bin/python

# Global Variable
gbl_name = "Sally"

# Declare the function to change global variable into this
def change_name():
    
    # Reference the global variable to use it in the function
    global gbl_name

    # change global variable vlaue
    gbl_name = "Sammy"


change_name()

print(gbl_name)

