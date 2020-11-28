import unittest
import ej_u2

from io            import StringIO
from unittest.mock import patch
from math          import pi

class TestEJU2(unittest.TestCase):
    def test_ejercicio_1(self):
        self.assertEqual(ej_u2.ejercicio_1(20, 30), 600)

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=[20, 30])
    def test_ejercicio_2(self, mock_input, mock_stdout):
        ej_u2.ejercicio_2()
        self.assertEqual(mock_stdout.getvalue(), "El producto es: 600\n")

    # rectangulo_perimitro
    def test_ejercicio_3_1(self):
        self.assertAlmostEqual(ej_u2.rectangulo_perimitro(20, 30), 100, 2)

    # rectangulo_area
    def test_ejercicio_3_2(self):
        self.assertAlmostEqual(ej_u2.rectangulo_area(20, 30), 600, 2)

    # circulo_perimitro
    def test_ejercicio_3_3(self):
        self.assertAlmostEqual(ej_u2.circulo_perimitro(10), 62.83, 2)

    # circulo_area
    def test_ejercicio_3_4(self):
        self.assertAlmostEqual(ej_u2.circulo_area(10), 314.16, 2)

    # volumen_esfera
    def test_ejercicio_3_5(self):
        self.assertAlmostEqual(ej_u2.volumen_esfera(10), 4188.79, 2)

    # hipotenusa_rectangulo
    def test_ejercicio_3_6(self):
        self.assertAlmostEqual(ej_u2.hipotenusa_rectangulo(10, 20), 22.36, 2)

    # factorial_1
    def test_ejercicio_4_1(self):
        self.assertEqual(ej_u2.factorial_1(5), 120)

    # factorial_2
    def test_ejercicio_4_2(self):
        self.assertEqual(ej_u2.factorial_2(5), 120)

    # factorial_3
    def test_ejercicio_4_3(self):
        self.assertEqual(ej_u2.factorial_3(5), 120)

    # operaciones
    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_5_1(self, mock_stdout):
        ej_u2.operaciones(20, 10)
        self.assertEqual(
            mock_stdout.getvalue(),
            "La suma es:      30.000000\n"+
            "La resta es:     10.000000\n"+
            "El producto es:  200.000000\n"+
            "El cociente es:  2.000000\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_5_2(self, mock_stdout):
        ej_u2.tabla_de_multiplicar(5)
        self.assertEqual(
            mock_stdout.getvalue(),
            "5 * 1 = 5\n"+
            "5 * 2 = 10\n"+
            "5 * 3 = 15\n"+
            "5 * 4 = 20\n"+
            "5 * 5 = 25\n"+
            "5 * 6 = 30\n"+
            "5 * 7 = 35\n"+
            "5 * 8 = 40\n"+
            "5 * 9 = 45\n"+
            "5 * 10 = 50\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value="frase")
    def test_ejercicio_7(self, mock_input, mock_stdout):
        ej_u2.ejercicio_7()
        self.assertEqual(mock_stdout.getvalue().count("frase"), 1000)

    # paridad_1
    def test_ejercicio_8_1_1(self):
        self.assertEqual(ej_u2.paridad_1(2), 1)

    # paridad_1
    def test_ejercicio_8_1_2(self):
        self.assertEqual(ej_u2.paridad_1(3), 0)

    # paridad_2
    def test_ejercicio_8_2_1(self):
        self.assertEqual(ej_u2.paridad_2(2), 0)

    # paridad_2
    def test_ejercicio_8_2_2(self):
        self.assertEqual(ej_u2.paridad_2(3), 1)

    def test_ejercicio_8_3(self):
        self.assertEqual(ej_u2.unidad(153), 3)

    def test_ejercicio_8_4(self):
        self.assertEqual(ej_u2.multiplo_inferior_10(153), 150)

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_9_1(self, mock_stdout):
        ej_u2.pares_entre(10, 20)
        self.assertEqual(mock_stdout.getvalue(), "10\n12\n14\n16\n18\n20\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_9_2(self, mock_stdout):
        ej_u2.pares_entre(9, 20)
        self.assertEqual(mock_stdout.getvalue(), "10\n12\n14\n16\n18\n20\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_9_3(self, mock_stdout):
        ej_u2.pares_entre(10, 21)
        self.assertEqual(mock_stdout.getvalue(), "10\n12\n14\n16\n18\n20\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_9_4(self, mock_stdout):
        ej_u2.pares_entre(9, 21)
        self.assertEqual(mock_stdout.getvalue(), "10\n12\n14\n16\n18\n20\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", return_value=5)
    def test_ejercicio_10(self, mock_input, mock_stdout):
        ej_u2.triangulares_1()
        self.assertEqual(mock_stdout.getvalue(), "1 - 1\n2 - 3\n3 - 6\n4 - 10\n5 - 15\n")

if __name__ == "__main__":
    unittest.main()