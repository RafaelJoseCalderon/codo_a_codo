#!/usr/bin/env python

import unittest
from ej_u3 import Persona, Alumno

from io import StringIO
from unittest.mock import patch

class TestEJU3(unittest.TestCase):
    def setUp(self):
        self.juan = Persona()
        self.juan.setNombre("Juan")
        self.juan.setEdad(120)

        self.pepe = Persona("Pepe", 60)

        self.pedro = Alumno("Pedro", 2)
 
    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_1(self, mock_stdout):
        self.assertEqual(self.juan.getNombre(), "Juan")
        self.assertEqual(self.juan.getEdad(), 120)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_1_print(self, mock_stdout):
        self.juan.print_persona()
        self.assertEqual(mock_stdout.getvalue(), "\"nombre\": \"Juan\", \"edad\": 120\n")

    def test_ejercicio_2(self):
        self.assertEqual(self.pepe.getNombre(), "Pepe")
        self.assertEqual(self.pepe.getEdad(), 60)

    def test_ejercicio_3_true(self):
        self.assertTrue(self.juan.es_mayor_de_edad())

    def test_ejercicio_3_false(self):
        self.pepe.setEdad(10)
        self.assertFalse(self.pepe.es_mayor_de_edad())

    def test_ejercicio_4_true(self):
        self.assertTrue(self.juan.es_mayor_que(self.pepe))

    def test_ejercicio_4_false(self):
        self.assertFalse(self.pepe.es_mayor_que(self.juan))

    def test_ejercicio_5(self):
        self.assertEqual(Persona.get_mayor(self.juan, self.pepe), self.juan)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_6_1(self, mock_stdout):
        self.pedro.__str__()
        self.assertEqual(mock_stdout.getvalue(), "\"nombre\": \"Pedro\", \"nota\": 2\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_6_2_1(self, mock_stdout):
        self.pedro.aprobo()
        self.assertEqual(mock_stdout.getvalue(), "desaprobo\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_6_2_2(self, mock_stdout):
        self.pedro.nota = 10
        self.pedro.aprobo()
        self.assertEqual(mock_stdout.getvalue(), "aprobo\n")

if __name__ == "__main__":
    unittest.main()