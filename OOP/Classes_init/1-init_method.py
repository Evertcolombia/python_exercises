#!/usr/bin/python3
class Person:
    #define the init method iw will indicata what
    #to do  in each instance when are created
    def __init__(self, name):
        self.name = name #object self now contains a name variable

    def say_hi(self): #method using the self oneb for each instance
        print("Hello, my name is", self.name)


p = Person('Evert')
p.say_hi()
