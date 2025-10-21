import Artista
from Models.Conteudo import Musica

class Independente(Artista):
    def __init__(self, nome, formaPagamento):
        super().__init__(self, nome)
        self.__formaPagamento = formaPagamento

    def enviarMusica(self):
        
        print('Enviando Música...')
        print('Música enviada com sucesso!')


