#!/usr/bin/env python

salida = ""
for i in range(501):
    if i % 4 == 0:
        salida += str(i) + " (Múltiplo de 4) \n"
    elif i % 9 == 0:
        salida += str(i) + " (Múltiplo de 9) \n"
    else:
        salida += str(i) + "\n"

    if i % 5 == 0:
        salida += "--------------------------- \n"

print(salida)
