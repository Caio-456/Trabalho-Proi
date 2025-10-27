from Models.Conteudo.Conteudo import Conteudo

class AudioLivro(Conteudo):
    def __init__(self, titulo, artista, data, duracao, genero, narrador, editora, capitulos):
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__duracao = duracao
        self.__genero = genero
        self.__narrador = narrador
        self.__editora = editora
        self.__capitulos = capitulos

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
    def narrador(self):
        return self.__narrador
    
    @property
    def editora(self):
        return self.__editora
    
    @property
    def capitulos(self):
        return self.__capitulos

        