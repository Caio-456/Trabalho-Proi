import Artista

class Podcaster(Artista):
    def __init__(self, nome, marca):
        super().__init__(nome)
        self.__marca = marca