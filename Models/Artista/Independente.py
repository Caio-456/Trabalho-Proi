import Artista

class Independente(Artista):
    def __init__(self, nome, formaPagamento):
        super().__init__(self, nome)
        self.__formaPagamento = formaPagamento