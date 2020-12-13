#!/usr/bin/env python

class Persona:
    # ejercicio 1
    #__edad = 0
    #__nombre = ""

    # ejercicio 2
    def __init__(self, nombre = "", edad = 0):
        self.__nombre = nombre
        self.__edad = edad

    # ejercicio 1
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    # ejercicio 1
    def getNombre(self):
        return self.__nombre
    
    # ejercicio 1
    def setEdad(self, edad):
        self.__edad = edad
    
    # ejercicio 1
    def getEdad(self):
        return self.__edad
    
    # ejercicio 1
    def print_persona(self):
        print(f"\"nombre\": \"{self.__nombre}\", \"edad\": {self.__edad}")

    # ejercicio 3
    def es_mayor_de_edad(self):
        return self.__edad > 18
    
    # ejercicio 4
    def es_mayor_que(self, persona):
        return self.__edad > persona.getEdad()
    
    # ejercicio 5
    @staticmethod
    def get_mayor(persona1, persona2):
        return persona1 if persona1.getEdad() > persona2.getEdad() else persona2

# ejercicio 6
class Alumno:

    def __init__(self, nombre = "", nota = 0):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        print(f"\"nombre\": \"{self.nombre}\", \"nota\": {self.nota}")
    
    def aprobo(self):
        print("aprobo") if self.nota >= 6 else print("desaprobo")



