from Models.Artista.Artista import Artista

class Gravadora(Artista):
    def __init__(self, nome, pais, percentual_repasse=0.7):
        super().__init__(nome)
        self.pais = pais
        self.__percentual_repasse = percentual_repasse
        self.catalogo = []

    def adicionar_conteudo(self, conteudo):
        self.catalogo.append(conteudo)

    def repassar_pagamentos(self, total_gerado):
        valor = total_gerado * self.__percentual_repasse
        self._adicionar_receita(valor)
        print(f"Repasse realizado: R${valor:.2f}")