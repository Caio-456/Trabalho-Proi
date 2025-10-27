from Models.Conteudo.Conteudo import Conteudo

class Musica(Conteudo):
    def __init__(self, titulo, artista, data, duracao, genero, isrc, album, faixa, selo, explicito):
        super().__init__(titulo, artista, data, genero, duracao)
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__isrc = isrc
        self.__album = album
        self.__faixa = faixa
        self.__selo = selo
        self.__explicito = explicito

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
    def isrc(self):
        return self.__isrc
    
    @property
    def album(self):
        return self.__album
    
    @property
    def faixa(self):
        return self.__faixa
    
    @property
    def selo(self):
        return self.__selo
    
    @property
    def explicito(self):
        return self.__explicito