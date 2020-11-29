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

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["1", "2", "5"])
    def test_ejercicio_11(self, mock_input, mock_stdout):
        ej_u2.ejercicio_11()
        self.assertEqual(
            mock_stdout.getvalue(),
            "El resultado es 1\n"+
            "El resultado es 2\n"+
            "El resultado es 120\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_12(self, mock_stdout):
        ej_u2.ejercicio_12()
        self.assertEqual(
            mock_stdout.getvalue(),
            "1:1\n1:2\n1:3\n1:4\n1:5\n1:6\n2:2\n2:3\n2:4\n2:5\n2:6\n"+
            "3:3\n3:4\n3:5\n3:6\n4:4\n4:5\n4:6\n5:5\n5:6\n6:6\n"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_13(self, mock_stdout):
        ej_u2.ejercicio_13(6)
        self.assertEqual(
            mock_stdout.getvalue(),
            "1:1\n1:2\n1:3\n1:4\n1:5\n1:6\n2:2\n2:3\n2:4\n2:5\n2:6\n"+
            "3:3\n3:4\n3:5\n3:6\n4:4\n4:5\n4:6\n5:5\n5:6\n6:6\n"
        )

    def test_ejercicio_14_1(self):
        hora_0 = "20:34:30"
        hora_1 = "20:40:30"
        self.assertAlmostEqual(ej_u2.duracion_segundos(hora_0, hora_1), 360.00, 2)

    def test_ejercicio_14_2(self):
        hora_0 = "20:34:30"
        hora_1 = "20:40:30"
        self.assertAlmostEqual(ej_u2.duracion_horas(hora_0, hora_1), 0.10, 2)

    def test_ejercicio_15(self):
        hora_0 = "20:34:30"
        hora_1 = "20:40:30"
        self.assertEqual(
            ej_u2.ejercicio_15(hora_0, hora_1),
            "0 horas, 6 minutos, 360 segundos"
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_ejercicio_16(self, mock_stdout):
        ej_u2.ejercicio_16(5)
        self.assertEqual(
            mock_stdout.getvalue(),
            "1 0 0 0 0 \n"+
            "0 1 0 0 0 \n"+
            "0 0 1 0 0 \n"+
            "0 0 0 1 0 \n"+
            "0 0 0 0 1 \n\n"
        )

    # ejercicio 17
    def test_bisiesto(self):
        self.assertEqual(ej_u2.anio_bisiesto(2000), True)
        self.assertEqual(ej_u2.anio_bisiesto(2400), True)
        self.assertEqual(ej_u2.anio_bisiesto(1900), False)
        self.assertEqual(ej_u2.anio_bisiesto(2100), False)
        self.assertEqual(ej_u2.anio_bisiesto(2300), False)

    def test_dias_por_anio_mes(self):
        self.assertEqual(ej_u2.dias_por_anio_mes(11, 2020), 305)

    @patch("sys.stdout", new_callable=StringIO)
    def test_fecha_valida_1(self, mock_stdout):
        ej_u2.fecha_valida(28, 7, 1983)
        self.assertEqual(mock_stdout.getvalue(), "Fecha valida\n")

    @patch("sys.stdout", new_callable=StringIO)
    def test_fecha_valida_2(self, mock_stdout):
        ej_u2.fecha_valida(55, 99, 1983)
        self.assertEqual(mock_stdout.getvalue(), "Fecha invalida\n")

    def test_dias_a_fin_de_mes(self):
        fecha = "28/11/2020"
        self.assertEqual(ej_u2.dias_a_fin_de_mes(fecha), 2)

    def test_dias_a_fin_de_anio(self):
        fecha = "28/11/2020"
        self.assertEqual(ej_u2.dias_a_fin_de_anio(fecha), 33)

    def test_dias_trascurridos_hasta(self):
        fecha = "28/11/2020"
        self.assertEqual(ej_u2.dias_trascurridos_hasta(fecha), 333)
        # anio bisiesto

    def test_diferencia_365_30(self):
        self.assertEqual(
            ej_u2.diferencia_365_30("28/11/2020", "15/06/2025"),
            {'anios': 4, 'meses': 6, 'dias': 20}
        )

    def test_ejercicio_18(self):
        self.assertEqual(ej_u2.ejercicio_18(1), "lunes")
        self.assertEqual(ej_u2.ejercicio_18(9), "martes")

    def test_ejercicio_19(self):
        self.assertEqual(ej_u2.ejercicio_19(   3),    "III")
        self.assertEqual(ej_u2.ejercicio_19(   4),     "IV")
        self.assertEqual(ej_u2.ejercicio_19(   5),      "V")
        self.assertEqual(ej_u2.ejercicio_19(   8),   "VIII")
        self.assertEqual(ej_u2.ejercicio_19(   9),     "IX")
        self.assertEqual(ej_u2.ejercicio_19(  10),      "X")
        self.assertEqual(ej_u2.ejercicio_19(  15),     "XV")
        self.assertEqual(ej_u2.ejercicio_19(  19),    "XIX")
        self.assertEqual(ej_u2.ejercicio_19(  30),    "XXX")
        self.assertEqual(ej_u2.ejercicio_19(  39),  "XXXIX")
        self.assertEqual(ej_u2.ejercicio_19(  40),     "XL")
        self.assertEqual(ej_u2.ejercicio_19(  41),    "XLI")
        self.assertEqual(ej_u2.ejercicio_19(  45),    "XLV")
        self.assertEqual(ej_u2.ejercicio_19(  49),   "XLIX")
        self.assertEqual(ej_u2.ejercicio_19(  50),      "L")
        self.assertEqual(ej_u2.ejercicio_19(  80),   "LXXX")
        self.assertEqual(ej_u2.ejercicio_19(  90),     "XC")
        self.assertEqual(ej_u2.ejercicio_19(  99),   "XCIX")
        self.assertEqual(ej_u2.ejercicio_19( 100),      "C")
        self.assertEqual(ej_u2.ejercicio_19( 150),     "CL")
        self.assertEqual(ej_u2.ejercicio_19( 190),    "CXC")
        self.assertEqual(ej_u2.ejercicio_19( 300),    "CCC")
        self.assertEqual(ej_u2.ejercicio_19( 390),  "CCCXC")
        self.assertEqual(ej_u2.ejercicio_19( 400),     "CD")
        self.assertEqual(ej_u2.ejercicio_19( 410),    "CDX")
        self.assertEqual(ej_u2.ejercicio_19( 450),    "CDL")
        self.assertEqual(ej_u2.ejercicio_19( 495),  "CDXCV")
        self.assertEqual(ej_u2.ejercicio_19( 490),   "CDXC")
        self.assertEqual(ej_u2.ejercicio_19( 499), "CDXCIX")
        self.assertEqual(ej_u2.ejercicio_19( 500),      "D")
        self.assertEqual(ej_u2.ejercicio_19( 800),   "DCCC")
        self.assertEqual(ej_u2.ejercicio_19( 900),     "CM")
        self.assertEqual(ej_u2.ejercicio_19( 990),   "CMXC")
        self.assertEqual(ej_u2.ejercicio_19( 999), "CMXCIX")
        self.assertEqual(ej_u2.ejercicio_19(1900),    "MCM")
        self.assertEqual(ej_u2.ejercicio_19(1500),     "MD")
        self.assertEqual(ej_u2.ejercicio_19(1000),      "M")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["21", "1"])
    def test_ejercicio_20_1(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Tu signo es: acuario\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["20", "2"])
    def test_ejercicio_20_2(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Tu signo es: acuario\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["21", "2"])
    def test_ejercicio_20_3(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Tu signo es: piscis\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["20", "3"])
    def test_ejercicio_20_4(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Tu signo es: piscis\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["21", "3"])
    def test_ejercicio_20_5(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(), "Tu signo es: aries\n")

    @patch("sys.stdout", new_callable=StringIO)
    @patch("builtins.input", side_effect=["20", "4"])
    def test_ejercicio_20_6(self, mock_input, mock_stdout):
        ej_u2.ejercicio_20()
        self.assertEqual(mock_stdout.getvalue(),"Tu signo es: aries\n")

if __name__ == "__main__":
    unittest.main()