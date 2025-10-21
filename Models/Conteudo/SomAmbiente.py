import Conteudo

class somAmbiente(Conteudo):
    def __init__ (self, titulo, criador, data, genero, duracao, loopavel, faixaRuido):
        super().__init__(self, titulo, criador, data, genero, duracao)
        self.__loopavel = loopavel
        self.__faixaRuido = faixaRuido