import Artista

class Independente(Artista):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.__idade = idade
