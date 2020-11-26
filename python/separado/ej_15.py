#!/usr/bin/env python

numero_1 = int(input("Ingrese un entero "))
numero_2 = int(input("Ingrese otro entero "))

respuesta = "Los divisores comunes son "
maximo = numero_1 if numero_1 > numero_2 else numero_2

for i in range(1, maximo):
    if numero_1 % i == 0 and numero_2 % i == 0:
        respuesta += str(i) + " "

print(respuesta)
