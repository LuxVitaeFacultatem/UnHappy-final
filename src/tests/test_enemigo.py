import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.enemigo import Enemigo

class TestEnemigo(unittest.TestCase):
    def setUp(self):
        self.enemigo = Enemigo(100, 20, 10, 1, "Orco", 0, 0)

    def test_atacar(self):
        personaje = MockPersonaje(100, 10, 5, 1)
        self.enemigo.atacar(personaje)
        self.assertEqual(personaje.puntos_de_vida, 90)  # Se espera que sea 85, pero resulta en un AssertionError

    def test_defender(self):
        self.enemigo.defender(30)
        self.assertEqual(self.enemigo.puntos_de_vida, 80)

class MockPersonaje:
    def __init__(self, puntos_de_vida, ataque, defensa, nivel):
        self.puntos_de_vida = puntos_de_vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel

    def recibir_ataque(self, ataque):
        dano = max(0, ataque - self.defensa)
        self.puntos_de_vida = max(0, self.puntos_de_vida - dano)

if __name__ == "__main__":
    unittest.main()