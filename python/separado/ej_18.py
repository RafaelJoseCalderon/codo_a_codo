#!/usr/bin/env python

calificacion = float(input("Ingrese la calificación "))

if calificacion >= 0 and calificacion < 3:
    print("Su calificación es, muy deficiente")
elif calificacion >= 3 and calificacion < 5:
    print("Su calificación es, insuficiente")
elif calificacion >= 5 and calificacion < 6:
    print("Su calificación es, suficiente")
elif calificacion >= 6 and calificacion < 7:
    print("Su calificación es, bien")
elif calificacion >= 7 and calificacion < 9:
    print("Su calificación es, notable")
elif calificacion >= 9 and calificacion <= 10:
    print("Su calificación es, sobresaliente")
else:
    print("valor incorrecto")
