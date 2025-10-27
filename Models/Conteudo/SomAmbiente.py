from Models.Conteudo.Conteudo import Conteudo


class SomAmbiente(Conteudo):
    def __init__ (self, titulo, criador, data, genero, duracao, loopavel, faixaRuido):
        super().__init__(self, titulo, criador, data, genero, duracao)
        self.__loopavel = loopavel
        self.__faixaRuido = faixaRuido