# !/usr/bin/python

import unittest

class TestNumero(unittest.TestCase):
    """
    Clase de test de numeros par y impar 
    """
    def test_par(self):
        """
        Funcion que analizar un numero par 
        :return: nada 
        """
        par = 4 % 2
        self.assertFalse(par)

    def test_noPar(self):
        no_impar = 15 % 2
        self.assertEqual(no_impar, 0)

    def test_impar(self):
        impar = 19 % 2
        self.assertTrue(impar)

    def test_noImpar(self):
        no_par = 10 % 2
        self.assertEqual(no_par, 1)


if __name__ == '__main__':
    TestNumero.main()