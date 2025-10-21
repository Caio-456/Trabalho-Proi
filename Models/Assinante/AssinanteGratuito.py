import Assinante

class Gratuito(Assinante):
    def __init__(self, faixa_anuncios = True, limite_pulos = 8, alta_qualidade = False, ouvir_offline = False):
        super().__init__(
            tipo = "Gratuito",
            preco = 0.00)
        
        self.__faixa_anuncios = faixa_anuncios
        self.__limite_pulos = limite_pulos
        self.__alta_qualidade = alta_qualidade
        self.__ouvir_offline = ouvir_offline
        

    def pular_musica(self):
        if limite_pulos <= 8:
            print("Pulando música...")
            limite_pulos -= 1
            
        else:
            print("Pulos esgotados")