class Assinante:
    def __init__(self, tipo, preco):
        self.__tipo = tipo
        self.__preco = preco

    def __str__(self):
        return f"Tipo: {self.__tipo}  |  Preço: R${self.__preco:.2f}"