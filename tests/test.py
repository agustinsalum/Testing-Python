
import sys
sys.path.append("..") # Agrega un directorio superior a la ruta de los módulos de Python

from clasePila import agregar, crear, ultimoElemento, eliminarTope
import unittest

class TestPila(unittest.TestCase):
    def test_case1(self):

        """ Testea que la pila este vacia una vez creada"""
        self.assertEqual(crear(), 0)


    def test_case2(self):

        """ Testea que se agrega un nuevo elemento"""
        self.assertEqual(agregar(), 5)


    def test_case3(self):

        """ Testea el elemento del tope de la pila"""
        self.assertEqual(ultimoElemento(), 9)


    def test_case4(self):

        """ Testea que se elimina el ultimo elemento"""
        self.assertEqual(eliminarTope(), 8)

if __name__ == '__main__':
    unittest.main()