import unittest
import math
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.personaje import Personaje

class TestPersonaje(unittest.TestCase):

    def setUp(self):
        self.personaje = Personaje(puntos_de_vida=10, ataque=3, defensa=2, nivel=1, x=50, y=50)

    def test_mover(self):
        self.personaje.mover('arriba')
        self.assertEqual(self.personaje.posicion_actual(), (50, 49.62))

    def test_recibir_ataque(self):
        self.personaje.recibir_ataque(3)
        self.assertEqual(self.personaje.puntos_de_vida, 7)

    def test_atacar(self):
        enemigo = Personaje(puntos_de_vida=5, ataque=2, defensa=1, nivel=1, x=50, y=50)
        self.personaje.atacar(enemigo)
        self.assertEqual(enemigo.puntos_de_vida, 2)

    def test_recolectar(self):
        self.personaje.recolectar('Flecha')
        self.assertIn('Flecha', self.personaje.inventario)

    def test_usar(self):
        self.personaje.recolectar('pocion')
        self.personaje.usar('pocion')
        self.assertEqual(self.personaje.puntos_de_vida, 15)

    def test_vender(self):
        self.personaje.recolectar('Flecha')
        self.personaje.vender('Flecha')
        self.assertNotIn('Flecha', self.personaje.inventario)

    def test_subir_nivel(self):
        self.personaje.subir_nivel({'ataque': 2, 'defensa': 3})
        self.assertEqual(self.personaje.nivel, 2)
        self.assertEqual(self.personaje.ataque, 5)
        self.assertEqual(self.personaje.defensa, 5)

if __name__ == '__main__':
    unittest.main()