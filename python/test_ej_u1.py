#!/usr/bin/env python

import unittest
import ej_u1

from io import StringIO
from unittest.mock import patch

class TestEJU1(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_1(self, mock_stdout):
        ej_u1.ejercicio_1()
        self.assertEqual(mock_stdout.getvalue(), "Hola mundo\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_2(self, mock_stdout):
        ej_u1.ejercicio_2()
        self.assertEqual(mock_stdout.getvalue(), "8\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="Rafael")
    def test_ejercicio_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_3()
        self.assertEqual(mock_stdout.getvalue(), "Hola Rafael\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=[10, 20])
    def test_ejercicio_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_4()
        self.assertEqual(mock_stdout.getvalue(), "La suma es: 30\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=[10, 20])
    def test_ejercicio_5(self, mock_input, mock_stdout):
        ej_u1.ejercicio_5()
        self.assertEqual(mock_stdout.getvalue(), "El mayor es: 20\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=[10, 20, 30])
    def test_ejercicio_6(self, mock_input, mock_stdout):
        ej_u1.ejercicio_6()
        self.assertEqual(mock_stdout.getvalue(), "El maximo es: 30\n")

    # es divisible por2
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=10)
    def test_ejercicio_7_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_7()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por 2\n")

    # no es divisible por2
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_7_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_7()
        self.assertEqual(mock_stdout.getvalue(), "No es divisible por 2\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="Una frase")
    def test_ejercicio_8(self, mock_input, mock_stdout):
        ej_u1.ejercicio_8()
        self.assertEqual(mock_stdout.getvalue(), "La letra 'a' aparece, 2 veces\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="Las vocales presentes en la frace son: ")
    def test_ejercicio_9(self, mock_input, mock_stdout):
        ej_u1.ejercicio_9()
        self.assertEqual(
            mock_stdout.getvalue(), "Las vocales presentes en la frace son: a e o \n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="Las vocales presentes en la frace son: ")
    def test_ejercicio_10(self, mock_input, mock_stdout):
        ej_u1.ejercicio_10()
        self.assertEqual(
            mock_stdout.getvalue(), "La cantidad de vocales presentes en la frace es: 12\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="A a EE ee Ii Oo")
    def test_ejercicio_11(self, mock_input, mock_stdout):
        ej_u1.ejercicio_11()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Las vocales presentes en la frace son: \n"+
            "\tLa a aparece 2 veces\n"+
            "\tLa e aparece 4 veces\n"+
            "\tLa i aparece 2 veces\n"+
            "\tLa o aparece 2 veces\n"+
            "\tLa u aparece 0 veces\n"
        )

    # es divisible por 2
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=4)
    def test_ejercicio_12_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_12()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por 2\n")

    # es divisible por 3
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_12_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_12()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por 3\n")

    # es divisible por 5
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=25)
    def test_ejercicio_12_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_12()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por 5\n")

    # es divisible por 7
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=49)
    def test_ejercicio_12_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_12()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por 7\n")

    # es divisible por 2
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=4)
    def test_ejercicio_13_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_13()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por: 2\n")

    # es divisible por 3
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_13_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_13()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por: 3\n")

    # es divisible por 5
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=25)
    def test_ejercicio_13_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_13()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por: 5\n")

    # es divisible por 7
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=49)
    def test_ejercicio_13_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_13()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por: 7\n")

    # es divisible por todos
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=210)
    def test_ejercicio_13_5(self, mock_input, mock_stdout):
        ej_u1.ejercicio_13()
        self.assertEqual(mock_stdout.getvalue(), "Es divisible por: 2 3 5 7\n")

    # es divisible por 2
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=4)
    def test_ejercicio_14_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_14()
        self.assertEqual(
            mock_stdout.getvalue(),
            "\nLos divisores de 4 son:  1 2\n"+
            "Nota: los divisores no son necesariamnete primos\n"
        )

    # es divisible por 3
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_14_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_14()
        self.assertEqual(
            mock_stdout.getvalue(),
            "\nLos divisores de 9 son:  1 3\n"+
            "Nota: los divisores no son necesariamnete primos\n"
        )

    # es divisible por 5
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=25)
    def test_ejercicio_14_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_14()
        self.assertEqual(
            mock_stdout.getvalue(),
            "\nLos divisores de 25 son:  1 5\n"+
            "Nota: los divisores no son necesariamnete primos\n"
        )

    # es divisible por 7
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=49)
    def test_ejercicio_14_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_14()
        self.assertEqual(
            mock_stdout.getvalue(),
            "\nLos divisores de 49 son:  1 7\n"+
            "Nota: los divisores no son necesariamnete primos\n"
        )

    # es divisible por 2 3 5 7
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=210)
    def test_ejercicio_14_5(self, mock_input, mock_stdout):
        ej_u1.ejercicio_14()
        self.assertEqual(
            mock_stdout.getvalue(),
            "\nLos divisores de 210 son:  1 2 3 5 6 7 10 14 15 21 30 35 42 70 105\n"+
            "Nota: los divisores no son necesariamnete primos\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=[10, 20])
    def test_ejercicio_15(self, mock_input, mock_stdout):
        ej_u1.ejercicio_15()
        self.assertEqual(mock_stdout.getvalue(), "Los divisores comunes son 1 2 5 10 \n")

    # numero primo (2)
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=2)
    def test_ejercicio_16_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_16()
        self.assertEqual(mock_stdout.getvalue(), "El numero es primo\n")

    # numero primo (3)
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=3)
    def test_ejercicio_16_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_16()
        self.assertEqual(mock_stdout.getvalue(), "El numero es primo\n")

    # numero primo (13)
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=13)
    def test_ejercicio_16_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_16()
        self.assertEqual(mock_stdout.getvalue(), "El numero es primo\n")

    # numero primo (9)
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_16_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_16()
        self.assertEqual(mock_stdout.getvalue(), "El numero NO es primo\n")

    # mayor de edad
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=30)
    def test_ejercicio_17_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_17()
        self.assertEqual(mock_stdout.getvalue(), "Ud. ya puede conducir\n")

    # menor de edad
    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=10)
    def test_ejercicio_17_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_17()
        self.assertEqual(
            mock_stdout.getvalue(),
            "Ud. NO debe conducir (puede pero, no se lo diga a nadie)\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=1.5)
    def test_ejercicio_18_1(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, muy deficiente\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=4.5)
    def test_ejercicio_18_2(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, insuficiente\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=5.5)
    def test_ejercicio_18_3(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, suficiente\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=6.5)
    def test_ejercicio_18_4(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, bien\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=8)
    def test_ejercicio_18_5(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, notable\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9.5)
    def test_ejercicio_18_6(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "Su calificación es, sobresaliente\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=11)
    def test_ejercicio_18_7(self, mock_input, mock_stdout):
        ej_u1.ejercicio_18()
        self.assertEqual(mock_stdout.getvalue(), "valor incorrecto\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["Hola", " ", "mundo", ", ", "como estas?", "cancelar"])
    def test_ejercicio_20(self, mock_input, mock_stdout):
        ej_u1.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Hola mundo, como estas?\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["1", "2", "3", "4", "5", "cancelar"])
    def test_ejercicio_21(self, mock_input, mock_stdout):
        ej_u1.ejercicio_21()
        self.assertEqual(mock_stdout.getvalue(), "El resultado de la suma es: 15\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["12345678", "cancelar"])
    def test_ejercicio_22(self, mock_input, mock_stdout):
        ej_u1.ejercicio_22()
        self.assertEqual(mock_stdout.getvalue(), "La letra que corresponde es Z\n")

    # paso, hacer prueba manual

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_24(self, mock_stdout):
        ej_u1.ejercicio_24()
        self.assertEqual(
            mock_stdout.getvalue(),
            "666666\n55555\n4444\n333\n22\n1\n\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=9)
    def test_ejercicio_25(self, mock_input, mock_stdout):
        ej_u1.ejercicio_25()
        self.assertEqual(
            mock_stdout.getvalue(),
            "1\n22\n333\n4444\n55555\n666666\n7777777\n88888888\n999999999\n\n"
        )

    # paso hacer prueba manual 

if __name__ == "__main__":
    unittest.main()
