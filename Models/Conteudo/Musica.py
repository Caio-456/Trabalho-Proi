import Conteudo

class Musica(Conteudo):
    def __init__(self, titulo, criador, data, genero, duracao, iscrMusica, album, numeroFaixa, selo, explicito):
        super().__init__(self, titulo, criador, data, genero, duracao)
        self.__iscrMusica = iscrMusica
        self.__album = album
        self.__numerFaixa = numeroFaixa
        self.__selo = selo
        self.__explicito = explicito

    @property
    def titulo(self):
        return self.__titulo