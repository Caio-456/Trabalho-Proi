import Conteudo

class AudioLivro(Conteudo):
    def __init__ (self, iscrLivro, generoLivro, titulo, duracao, data, Artista):
        super().__init__(self, titulo, duracao, data, Artista)
        self.__iscrLivro = iscrLivro
        self.__generoLivro = generoLivro