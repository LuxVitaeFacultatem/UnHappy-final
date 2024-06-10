class Objeto:
    def __init__(self, nombre, tipo, valor, efecto):
        self.nombre = nombre
        self.tipo = tipo  # Puede ser 'arma' o 'defensa'
        self.valor = valor
        self.efecto = efecto

    def usar(self, personaje):
        # Lógica para aplicar el efecto del objeto al personaje
        if self.tipo == 'arma':
            personaje.ataque += self.efecto
        elif self.tipo == 'defensa':
            personaje.defensa += self.efecto

    def vender(self, vendedor):
        # Lógica para vender el objeto
        vendedor.comprar(self)
