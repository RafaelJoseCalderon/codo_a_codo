#!/usr/bin/env python

numero = int(input("Ingrese un entero "))

respuesta = ""
for i in range(1, int(numero / 2)):
    if numero % i == 0:
        respuesta += " " + str(i)

print("\nLos divisores de %s  son: %s" % (numero, respuesta))
print("Nota: los divisores no son necesariamnete primos")
