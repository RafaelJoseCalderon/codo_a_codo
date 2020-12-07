#!/usr/bin/env python

numero_1 = int(input("Escriba un entero: "))
numero_2 = int(input("Escriba otro entero: "))

if numero_1 > numero_2:
    resultado = numero_1
else:
    resultado = numero_2

print("El mayor es: %d" % resultado)
