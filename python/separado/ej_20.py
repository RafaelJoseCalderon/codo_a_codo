#!/usr/bin/env python

resultado = ""
lectura = input("Ingrese la cadena ")

while lectura != "cancelar":
    if lectura:
        resultado += lectura

    lectura = input("Ingrese la cadena ")

print(resultado)
