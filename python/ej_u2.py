#!/usr/bin/env python

from math import pi, sqrt, factorial

def ejercicio_1(numero_1, numero_2):
    return numero_1 * numero_2

def ejercicio_2():
    numero_1 = int(input("Escriba un entero: "))
    numero_2 = int(input("Escriba otro entero: "))
    print("El producto es: %d" % ejercicio_1(numero_1, numero_2))

# ejercicio 3
def rectangulo_perimitro(base, altura):
    return 2 * (base + altura)

def rectangulo_area(base, altura):
    return base * altura

def circulo_perimitro(radio):
    return 2 * pi * radio

def circulo_area(radio):
    return pi * radio ** 2

def volumen_esfera(radio):
    return 4 * pi * radio ** 3 / 3

def hipotenusa_rectangulo(cMayor, cMenor):
    return sqrt(cMayor ** 2 + cMenor ** 2)

#ejercicio 4
# parte 1
#  >>> for i in range(5):
#  ...     print(i*i)
#  ... 
#  0
#  1
#  4
#  9
#  16
#
# parte 2
#  >>> for i in range(2, 6):
#  ...     print(i, 2 ** i)
#  ... 
#  2 4
#  3 8
#  4 16
#  5 32

# ejercicio 5
def factorial_1(n):
    return factorial(n)

def factorial_2(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

def factorial_3(n):
    return n * factorial_3(n - 1) if n > 1 else 1

# ejercicio 6
def operaciones(numero_1, numero_2):
    print("La suma es:      %f" % (numero_1 + numero_2))
    print("La resta es:     %f" % (numero_1 - numero_2))
    print("El producto es:  %f" % (numero_1 * numero_2))
    print("El cociente es:  %f" % (numero_1 / numero_2))

def tabla_de_multiplicar(n):
    for i in range(1, 11):
        print("5 * %d = %d" % (i, i * n))

def ejercicio_7():
    palabra = input("Escriba un palabra: ")
    for i in range(1000):
        print(palabra, end=" ")
    
    print("")

# ejercicio 8
def paridad_1(numero):
    if numero % 2 == 0:
        resultado = 1
    else:
        resultado = 0
    
    return resultado

def paridad_2(numero):
    return not paridad_1(numero)

def unidad(numero):
    return numero % 10

def multiplo_inferior_10(numero):
    return numero - numero % 10

# ejercicio 9
def pares_entre(numero_1, numero_2):
    numero_1 = numero_1 if paridad_1(numero_1) else numero_1 + 1
    numero_2 = numero_2 + 2 if paridad_1(numero_2) else numero_2
    for i in range(numero_1, numero_2, 2):
        print(i)

# ejercicio 10
def triangulares_1():
    numero = int(input("Escriba el valor de los valores algulares que requiere: "))
    acumulador = 0
    for i in range(1, numero + 1):
        acumulador += i
        print(f'{i} - {acumulador}')