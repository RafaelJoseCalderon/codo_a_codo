#!/usr/bin/env python

maximo = int(input("Escriba un entero: "))

for n in range(2):
    numero = int(input("Escriba un entero: "))

    if numero > maximo:
        maximo = numero

print("El maximo es: %d" % maximo)
