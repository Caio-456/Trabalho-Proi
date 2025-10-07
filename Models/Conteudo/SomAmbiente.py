import Conteudo

class somAmbiente(Conteudo):
    def __init__ (self, iscrSom, generoDeSom, titulo, duracao, data, Artista):
        super().__init__(self, titulo, duracao, data, Artista)
        self.__iscrSom = iscrSom
        self.__generoDeSom = generoDeSom