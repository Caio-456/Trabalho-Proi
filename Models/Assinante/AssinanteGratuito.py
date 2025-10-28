from Models.Assinante.Assinante import Assinante

class AssinanteGratuito(Assinante):
    def __init__(self, tipo):
        self.__tipo = tipo
        self.__historico = []
        self.__faixa_anuncios = True
        self.__limite_pulos = 5
        self.__alta_qualidade = False
        self.__ouvir_offline = False
        
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def limite_pulos(self):
        return self.__limite_pulos
    
    @property
    def historico(self):
        return self.__historico
    
    def pular_musica(self):
        if self.__limite_pulos >= 0:
            print("Pulando música...")
            self.__limite_pulos -= 1
            print('Pulos restantes: ', self.__limite_pulos)
        else:
            print("Pulos esgotados.")

    def baixar_musica(self):
        print('Indisponível no plano gratuito.')

    def trocar_qualidade(self):
        print('Indisponível no plano gratuito.')
