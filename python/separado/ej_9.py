#!/usr/bin/env python

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
resultado = ""
frase = input("Escriba un frase: ").lower()

for vocal in vocales:
    if vocal in frase:
        resultado += vocal + " "

print("Las vocales presentes en la frace son: " + resultado)
