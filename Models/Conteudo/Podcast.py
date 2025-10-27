from Models.Conteudo.Conteudo import Conteudo


class Podcast(Conteudo):
    def __init__(self, titulo, artista, data, duracao, genero, season, episode, rss, isrc):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__season = season
        self.__episode = episode
        self.__rss = rss
        self.__isrc = isrc

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def data(self):
        return self.__data
    
    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def season(self):
        return self.__season
    
    @property
    def episode(self):
        return self.__episode
    
    @property
    def rss(self):
        return self.__rss
    
    @property
    def isrc(self):
        return self.__isrc