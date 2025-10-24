import Artista

class Podcaster(Artista):
    def __init__(self, nome, saldo, marca):
        super().__init__(self, nome, saldo)
        self.__marca = marca