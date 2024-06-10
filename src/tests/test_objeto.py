import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.objeto import Objeto
from src.personaje import Personaje

class MockVendedor:
    def __init__(self):
        self.inventario = []

    def comprar(self, objeto):
        self.inventario.append(objeto)

class TestObjeto(unittest.TestCase):
    def setUp(self):
        self.objeto = Objeto("Espada", "arma", 100, 10)
        self.personaje = Personaje(100, 20, 10, 1)
        self.vendedor = MockVendedor()

    def test_usar_arma(self):
        self.objeto.usar(self.personaje)
        self.assertEqual(self.personaje.ataque, 30)

    def test_usar_defensa(self):
        objeto_defensa = Objeto("Escudo", "defensa", 50, 5)
        objeto_defensa.usar(self.personaje)
        self.assertEqual(self.personaje.defensa, 15)

    def test_vender(self):
        self.objeto.vender(self.vendedor)
        self.assertIn(self.objeto, self.vendedor.inventario)

if __name__ == "__main__":
    unittest.main()

