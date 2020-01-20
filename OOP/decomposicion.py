#!/usr/bin/python3

#Decomposicion
"""
partir un problema en problemas mas pequenos

Las clases permiten crear mayores abstracciones en forma de componentes

Cada clase se encarga de una parte del problema
y el programa se vuelve mas facil de mantener
"""

"""
Comenzaremos a modelar un auto movil para resolver el problema en piezas
"""

class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        #atributos privados, __motor va a ser un metodo privado
        self.__estado = 'en_reposo'
        #este metodo inicializa la clase motor y le pasa un numero de cilindros
        self.__motor = Motor(cilindros=4)

    def acelerar(self, tipo='depacio'):
        if tipo == 'rapido':
            self.__motor.inyecta_gasolina(10)
        else:
            self.__motor.inyecta_gasolina(3)

        self.__estado = 'en_movimiento'
        print(self.__estado)
        self.__motor.estado_temp()

#Esta clase s inicializada a tra vez del attr __motor en la classe Automovil
class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self.__temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        self.__tiempo_duracion =  Tiempo(cantidad)
        self.__temperatura = self.__tiempo_duracion.calculo_tiempo(cantidad) / 2

    def estado_temp(self):
        if self.__temperatura < 30:
            print("La temperatura del motor es buena")
        elif self.__temperatura > 50:
            print("La temperatura del motor es alta como la velocidad")

#esta clae defne tempos de duracion encedido del automovil
class Tiempo:
    def __init__(self, cantidad_gasolina):
        self.cantidad_gasolina = cantidad_gasolina
        self.__calculo_tiempo = cantidad_gasolina * 18
        
    def calculo_tiempo(self, cantidad):
        if cantidad == 3:
            print("Duracion aproximada: {:d} minutos".format(self.__calculo_tiempo))
        elif cantidad == 10:
            print("Duracion aproximada: {:d} minutos:".format(self.__calculo_tiempo))
        return (self.__calculo_tiempo)
