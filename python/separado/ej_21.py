#!/usr/bin/env python

entrada = input("Ingrese un entero ")
suma = 0

while entrada != "cancelar":
    if entrada.isnumeric():
        suma += int(entrada)
    else:
        print("dato ingresado invalido, intente otra vez")

    entrada = input("Ingrese un entero ")

print("El resultado de la suma es: %d" % suma)
