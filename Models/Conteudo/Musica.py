import Conteudo

class Musica(Conteudo):
    def __init__(self, generoMusica, iscrMusica, titulo, duracao, data, Artista):
        super().__init__(self, titulo, duracao, data, Artista)
        self.__generoMusica = generoMusica
        self.__iscrMusica = iscrMusica