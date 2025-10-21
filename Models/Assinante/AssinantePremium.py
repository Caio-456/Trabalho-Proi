import Assinante

class Premium(Assinante):
    def __init__(self, faixa_anuncios = False, alta_qualidade = True, ouvir_offline = True):
        super().__init__(
            tipo = "Premium",
            preco = 23.90) 
            
        self.__faixa_anuncios = faixa_anuncios
        self.__alta_qualidade = alta_qualidade
        self.__ouvir_offline = ouvir_offline
        

    def baixar_musica(self, musica):
        print(f'A música {musica.titulo} foi baixada')