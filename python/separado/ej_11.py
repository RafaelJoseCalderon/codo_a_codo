#!/usr/bin/env python

vocales = ["a", "e", "i", "o", "u"]

frase = input("Escriba un frase: ").lower()

print("Las vocales presentes en la frace son: ")
for vocal in vocales:
    print("\tLa %s aparece %d veces" % (vocal, frase.count(vocal)))
