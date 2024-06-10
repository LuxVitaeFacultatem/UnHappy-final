import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.escenario import Escenario
from src.enemigo import Enemigo
from src.objeto import Objeto

class TestEscenario(unittest.TestCase):
    def setUp(self):
        self.escenario = Escenario("Bosque", ["Área1", "Área2"])

    def test_ubicar_enemigos(self):
        enemigo1 = Enemigo(100, 20, 10, 1, "Orco")
        enemigo2 = Enemigo(80, 15, 5, 1, "Goblin")
        self.escenario.ubicar_enemigos([enemigo1, enemigo2])
        self.assertEqual(len(self.escenario.ubicacion_enemigos), 2)

    def test_ubicar_objetos(self):
        objeto1 = Objeto("Espada", "arma", 100, "Aumenta ataque")
        objeto2 = Objeto("Escudo", "defensa", 150, "Aumenta defensa")
        self.escenario.ubicar_objetos([objeto1, objeto2])
        self.assertEqual(len(self.escenario.ubicacion_objetos), 2)

if __name__ == "__main__":
    unittest.main()

