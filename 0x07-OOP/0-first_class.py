#!/usr/bin/python3
Class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} th dog eats".format(self.name))

    def bark(self):
        print("{} th dog barks".format(self.name))


def main():
    keka = Dog("Keka", 50, 36)

    keka.eat()

main()
