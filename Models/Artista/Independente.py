from Models.Artista.Artista import Artista

class Independente(Artista):
    def __init__(self, nome):
        super().__init__(nome)
        self.__taxa_pagamento = 0.01  # Ex.: 1 centavo por stream

    def receber_pagamento_streams(self):
        valor = self._streams_validos * self.__taxa_pagamento
        self._adicionar_receita(valor)
        print(f"Pagamento realizado: R${valor:.2f}")