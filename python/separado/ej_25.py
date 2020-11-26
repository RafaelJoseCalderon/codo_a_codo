#!/usr/bin/env python
import piramide

lectura = int(input("Ingrese un entero no mayor a 50 "))

if lectura <= 50:
    piramide.piramide(1, lectura + 1, 1)
