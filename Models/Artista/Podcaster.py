from Models.Artista.Artista import Artista

class Podcaster(Artista):
    def __init__(self, nome, marca=None):
        super().__init__(nome)
        self.marca = marca
        self._receita_publicidade = 0

    def registrar_receita_ads(self, valor):
        self._receita_publicidade += valor
        self._adicionar_receita(valor)

    def monetizar(self):
        print(f"Receita acumulada de anúncios: R${self._receita_publicidade:.2f}")
