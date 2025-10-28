from Models.Assinante.Assinante import Assinante

class AssinantePremium(Assinante):
    def __init__(self, tipo):
        self.__tipo = tipo
        self.__historico = []
        self.__faixa_anuncios = False
        self.__alta_qualidade = True
        self.__ouvir_offline = True

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def historico(self):
        return self.__historico
