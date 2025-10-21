import Conteudo

class Podcast(Conteudo):
    def __init__ (self, titulo, criador, data, genero, duracao, temporada, episodio, RSS, capitulos):
        super().__init__(self, titulo, criador, data, genero, duracao)
        self.__temporada = temporada
        self.__episodio = episodio
        self.__RSS = RSS
        self.__capitulos = capitulos