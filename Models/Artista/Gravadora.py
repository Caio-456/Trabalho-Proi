import Artista

class Gravadora(Artista):
    def __init__(self, nome, pais):
        super().__init__(self, nome)
        self.pais = pais