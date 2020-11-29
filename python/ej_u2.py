#!/usr/bin/env python

from math import pi, sqrt, factorial, trunc
from time import mktime, strptime, strftime

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

def hipotenusa_rectangulo(c_mayor, c_menor):
    return sqrt(c_mayor ** 2 + c_menor ** 2)

# ejercicio 4
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
    for _ in range(1000):
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
    numero = int(
        input("Escriba el valor de los valores algulares que requiere: "))
    acumulador = 0
    for i in range(1, numero + 1):
        acumulador += i
        print(f'{i} - {acumulador}')

def ejercicio_11():
    for _ in range(3):
        numero = int(input("ingrese un entero para calcular su factorial: "))
        print(f'El resultado es {factorial_1(numero)}')

# no entendi el enunciado, copio y pego
def ejercicio_12():
    for i in range(1, 7):
        for j in range(i, 7):
            print("{}:{}".format(i, j))

def ejercicio_13(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print("{}:{}".format(i, j))

# ejercicio 14
def duracion_segundos(tiempo_0, tiempo_1):  # "20:40:30"
    tiempo_0 = mktime(strptime(tiempo_0, "%H:%M:%S"))
    tiempo_1 = mktime(strptime(tiempo_1, "%H:%M:%S"))
    return tiempo_1 - tiempo_0

def duracion_horas(tiempo_0, tiempo_1):  # "20:40:30"
    return duracion_segundos(tiempo_0, tiempo_1) / 3600

def ejercicio_15(tiempo_0, tiempo_1):  # "20:40:30"
    segundos = trunc(duracion_segundos(tiempo_0, tiempo_1))
    minutos = trunc(segundos / 60)
    horas = trunc(duracion_horas(tiempo_0, tiempo_1))
    return f'{horas} horas, {minutos} minutos, {segundos} segundos'

def ejercicio_16(d):  # x(
    f = ""
    I = ""

    for i in range(d):
        f += "0 "

    for i in range(d):
        I += f[:2 * i] + "1" + f[2 * i + 1:] + "\n"

    print(I)

# ejercicio 17
def anio_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def dias_por_anio_mes(mes, anio):
    return deferencia_fechas(f'1/1/{anio}', f'1/{mes}/{anio}') // 86400

def fecha_valida(dia, mes, anio):
    try:
        mktime(strptime(f'{dia}/{mes}/{anio}', "%d/%m/%Y"))
        print("Fecha valida")
    except ValueError:
        print("Fecha invalida")

def dias_a_fin_de_mes(fecha):
    base = strptime(fecha, "%d/%m/%Y")
    return deferencia_fechas(fecha, f'1/{base.tm_mon + 1}/{base.tm_year}') // 86400 - 1

def dias_a_fin_de_anio(fecha):
    base = strptime(fecha, "%d/%m/%Y")
    return deferencia_fechas(fecha, f'1/1/{base.tm_year + 1}') // 86400 - 1

def dias_trascurridos_hasta(fecha):
    base = strptime(fecha, "%d/%m/%Y")
    return 1 - deferencia_fechas(fecha, f'1/1/{base.tm_year}') // 86400

def diferencia_365_30(fecha_1, fecha_2):
    resto = deferencia_fechas(fecha_1, fecha_2)
    (anios, resto) = divmod(resto, 31536000) # anios de 365 dias
    (meses, resto) = divmod(resto, 2592000)  # meses de 30 dias
    dias = resto // 86400
    return {'anios': int(anios), 'meses': int(meses), 'dias': int(dias)}

def deferencia_fechas(fecha_1, fecha_2):
    fecha_1 = mktime(strptime(fecha_1, "%d/%m/%Y"))
    fecha_2 = mktime(strptime(fecha_2, "%d/%m/%Y"))
    return fecha_2 - fecha_1

def ejercicio_18(dia): # 1996 anio bisiesto que empieza en lunes
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    return dias[(dia - 1) % 7]

# copiado y pegado
def ejercicio_19(decimal):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    retorno = ""

    if decimal > 0 and decimal <= 4000:
        for i in range(12, -1, -1):
            while decimal >= num[i]:
                decimal -= num[i]
                retorno += rom[i]
    
    return retorno

def ejercicio_20():
    signo  = ["capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario"]

    dia = int(input("dia: "))
    mes = int(input("mes: ")) - 1

    if dia > 20:
        mes += 1
    
    if mes == 12:
        mes = 0

    print ("Tu signo es: " + signo[mes])