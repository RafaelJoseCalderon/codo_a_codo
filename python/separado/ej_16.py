#!/usr/bin/env python

numero = abs(int(input("Ingrese un entero ")))

i = 2
mitad = int(numero / 2)

while numero % i != 0 and i <= mitad:
    i += 1

if i > mitad:
    print("El numero es primo")
else:
    print("El numero NO es primo")
