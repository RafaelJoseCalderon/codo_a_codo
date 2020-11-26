#!/usr/bin/env python

# el masacote este esta sin probrar, individualmente andan, aunque no garantizo nada.

def ejercicio_1():
    print("Hola mundo")

def ejercicio_2():
    print(3 + 5)

def ejercicio_3():
    nombre = input("Escriba su nombre ")
    print("Hola " + nombre)

def ejercicio_4():
    numero_1 = int(input("Escriba un entero: "))
    numero_2 = int(input("Escriba otro entero: "))
    print("La suma es: %d" % (numero_1 + numero_2))

def ejercicio_5():
    numero_1 = int(input("Escriba un entero: "))
    numero_2 = int(input("Escriba otro entero: "))

    if numero_1 > numero_2:
        resultado = numero_1
    else:
        resultado = numero_2

    print("El mayor es %d" % resultado)

def ejercicio_6():
maximo = int(input("Escriba un entero: "))

for n in range(2):
    numero = int(input("Escriba un entero: "))

    if numero > maximo:
        maximo = numero

    print("El maximo es: %d" % maximo)

def ejercicio_7():
    if int(input("Escriba un entero: ")) % 2 == 0:
        print("Es divisible por 2")
    else:
        print("No es divisible por 2")

def ejercicio_8():
    print("La letra 'a' aparece, %d veces" % input("Escriba un frase: ").count("a"))

def ejercicio_9():
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    resultado = ""
    frase = input("Escriba un frase: ").lower()

    for vocal in vocales:
        if vocal in frase:
            resultado += vocal + " "

    print("Las vocales presentes en la frace son: " + resultado)

def ejercicio_10():
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    resultado = 0
    frase = input("Escriba un frase: ").lower()

    for letra in frase:
        if letra in vocales:
            resultado += 1

    print("La cantidad de vocales presentes en la frace es: %d" % resultado)

def ejercicio_11():
    vocales = ["a", "e", "i", "o", "u"]

    frase = input("Escriba un frase: ").lower()

    print("Las vocales presentes en la frace son: ")
    for vocal in vocales:
        print("\tLa %s aparece %d veces" % (vocal, frase.count(vocal)))

def ejercicio_12():
    numero = int(input("Escriba un entero: "))

    if numero % 2 == 0:
        print("Es divisible por 2")
    elif numero % 3 == 0:
        print("Es divisible por 3")
    elif numero % 5 == 0:
        print("Es divisible por 5")
    elif numero % 7 == 0:
        print("Es divisible por 7")

def ejercicio_13():
    numero = int(input("Escriba un entero: "))
    resultado = ""
    divisores = [2, 3, 5, 7]

    for divisor in divisores:
        if numero % divisor == 0:
            resultado += " " + str(divisor)

    if not resultado:
        print("No es divisible por: 2, 3, 5 o 7")
    else:
        print("Es divisible por: " + resultado)

def ejercicio_14():
    numero = int(input("Ingrese un entero "))

    respuesta = ""
    for i in range(1, int(numero / 2)):
        if numero % i == 0:
            respuesta += " " + str(i)

    print("\nLos divisores de %s  son: %s" % (numero, respuesta))
    print("Nota: los divisores no son necesariamnete primos")

def ejercicio_15():
    numero_1 = int(input("Ingrese un entero "))
    numero_2 = int(input("Ingrese otro entero "))

    respuesta = "Los divisores comunes son "
    maximo = numero_1 if numero_1 > numero_2 else numero_2

    for i in range(1, maximo):
        if numero_1 % i == 0 and numero_2 % i == 0:
            respuesta += str(i) + " "

    print(respuesta)

def ejercicio_16():
    numero = abs(int(input("Ingrese un entero ")))

    i = 2
    mitad = int(numero / 2)

    while numero % i != 0 and i <= mitad:
        i += 1

    if i > mitad:
        print("El numero es primo")
    else:
        print("El numero NO es primo")

def ejercicio_17():
    edad = int(input("Ingrese su edad "))

    if edad > 18:
        print("Ud. ya puede conducir")
    else:
        print("Ud. NO debe conducir (puede pero, no se lo diga a nadie)")

def ejercicio_18():
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

def ejercicio_20():
    resultado = ""
    lectura = input("Ingrese la cadena ")

    while lectura != "cancelar":
        if lectura:
            resultado += lectura

        lectura = input("Ingrese la cadena ")

    print(resultado)

def ejercicio_21():
    entrada = input("Ingrese un entero ")
    suma = 0

    while entrada != "cancelar":
        if entrada.isnumeric():
            suma += int(entrada)
        else:
            print("dato ingresado invalido, intente otra vez")

        entrada = input("Ingrese un entero ")

    print("El resultado de la suma es: %d" % suma)

def ejercicio_22():
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

def ejercicio_23():
    piramide.piramide(1, 31, 1)

def ejercicio_24():
    piramide.piramide(6, 1, -1)

def ejercicio_25():
    lectura = int(input("Ingrese un entero no mayor a 50 "))

    if lectura <= 50:
        piramide.piramide(1, lectura + 1, 1)

def ejercicio_26():
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

def piramide(inicio, fin, paso):
    salida = ""
    for i in range(inicio, fin, paso):
        cadena = ""

        for j in range(i):
            cadena += str(i)

        salida += cadena + "\n"

    print(salida)