class Assinante:
    def __init__(self, tipo, preco):
        self._tipo = tipo
        self._preco = preco
        self._beneficio = beneficio
        self._limitacao = limitacao

    def __str__(self):
        return f"Tipo: {self._tipo}  |  Preço: R${self._preco:.2f}"