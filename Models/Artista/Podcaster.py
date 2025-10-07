import Artista

class Podcaster(Artista):
    def __init__(self, nome, marca):
        super().__init__(self, nome)
        self.__marca = marca