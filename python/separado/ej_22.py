#!/usr/bin/env python

letras = [
    "T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
    "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"
]

lectura = input("Ingrese su DNI ")
while lectura != "cancelar":
    if lectura.isnumeric():
        lectura = int(lectura)

        if lectura >= 0 and lectura <= 99999999:
            print("La letra que corresponde es %s" % letras[lectura % 23])
        else:
            print("Numero fuera de rango")

    else:
        print("No es un numero, intente otra vez")

    lectura = input("Ingrese su DNI ")
