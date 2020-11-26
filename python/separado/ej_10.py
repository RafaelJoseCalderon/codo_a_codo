#!/usr/bin/env python

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
resultado = 0
frase = input("Escriba un frase: ").lower()

for letra in frase:
    if letra in vocales:
        resultado += 1

print("La cantidad de vocales presentes en la frace es: %d" % resultado)
