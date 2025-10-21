import Conteudo

class AudioLivro(Conteudo):
    def __init__ (self, titulo, criador, data, genero, duracao, narrador, editora, capitulo):
        super().__init__(self, titulo, criador, data, genero, duracao)
        self.__narrador = narrador
        self.__editora = editora
        self.__capitulo = capitulo