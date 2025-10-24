class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__saldo = 0.0

    @property
    def nome(self):
        return self.__nome

    @property
    def saldo(self):
        return self.__saldo

    def _adicionar_receita(self, valor):
        self.__saldo += valor