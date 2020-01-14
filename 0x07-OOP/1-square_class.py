#!/usr/bin/python3
# ---------- GETTERS & SETTERS ----------
# Getters and Setters are used to protect our objects
# from assigning bad fields or for providing improved
# output

class Square: 
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is the getter
    @property
    def height(self):
        print("Retrieving string")

        #put a __ before this private fiel
        return self.__height

    # This is the setter
    @height.setter
    def height(self, value):
        # Protect the heignt from receiving a bad value
        if value.isdigit():

            #put a __ before this private field
            self.__height = value
        else:
            print("Please only enter number for height")

    @property
    def width(self):
        print("Retrieving string")
        return self.__width

    # This is the setter
    @width.setter
    def width(self, value):
        # Protect the heignt from receiving a bad value
        if value.isdigit():

            #put a __ before this private field
            self.__width = value
        else:
            print("Please only enter number for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)



def main():
    aSquare = Square()

    height = input("Enter height : ")
    width = input("Enter width : ")

    aSquare.height = height
    aSquare.width = width

    print("Height : ", aSquare.height)
    print("width : ", aSquare.width)

    print("The area is:" aSquare.getArea())


main()
