#!/usr/bin/env python


def piramide(inicio, fin, paso):
    salida = ""
    for i in range(inicio, fin, paso):
        cadena = ""

        for j in range(i):
            cadena += str(i)

        salida += cadena + "\n"

    print(salida)
