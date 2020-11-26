#!/usr/bin/env python

numero = int(input("Escriba un entero: "))
resultado = ""
divisores = [2, 3, 5, 7]

for divisor in divisores:
    if numero % divisor == 0:
        resultado += " " + str(divisor)

if not resultado:
    print("No es divisible por: 2, 3, 5 o 7")
else:
    print("Es divisible por: " + resultado)
