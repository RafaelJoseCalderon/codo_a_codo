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

if __name__ == "__main__":
    unittest.main()
