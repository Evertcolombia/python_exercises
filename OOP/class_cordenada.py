#!/usr/bin/python3
class Coordenada:
    #constructor method for each instance
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #public method for the instance, recives it self, and other
    #instance as arguments
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff) ** 0.5

if __name__ == '__main__':
    coord_1 = Coordenada(18, 34)
    coord_2 = Coordenada(23, 56)
    

    print(coord_1.distancia(coord_2))

    #isinstance show true if is an instance of the class Coordenada
    print(isinstance(coord_2, Coordenada))

    print(isinstance(3, Coordenada))
