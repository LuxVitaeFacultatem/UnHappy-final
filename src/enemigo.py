from personaje import Personaje


class Enemigo(Personaje):
    def __init__(self, puntos_de_vida, ataque, defensa, nivel, tipo, x, y):
        super().__init__(puntos_de_vida, ataque, defensa, nivel)
        self.tipo = tipo
        self.x = x
        self.y = y

    def atacar(self, objetivo):
        danio = max(0, self.ataque - objetivo.defensa)
        objetivo.recibir_ataque(danio)

    def defender(self, danio):
        danio_reducido = max(0, danio - self.defensa)
        self.recibir_ataque(danio_reducido)
