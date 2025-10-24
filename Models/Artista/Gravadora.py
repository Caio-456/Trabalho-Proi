import Artista

class Gravadora(Artista):
    def __init__(self, nome, saldo, pais):
        super().__init__(self, nome, saldo)
        self.pais = pais