from Models.Conteudo.Conteudo import Conteudo


class SomAmbiente(Conteudo):
    def __init__ (self, titulo, artista, data, genero, duracao, loopable, faixaRuido):
        super().__init__(titulo, artista, data, genero, duracao)
        self.__titulo = titulo
        self.__artista = artista
        self.__data = data
        self.__genero = genero
        self.__duracao = duracao
        self.__loopable = loopable
        self.__faixaRuido = faixaRuido

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
    def genero(self):
        return self.__genero
    
    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def loopable(self):
        return self.__loopable
    
    @property
    def faixaRuido(self):
        return self.__faixaRuido