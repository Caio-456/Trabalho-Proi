from Models.Assinante.Assinante import Assinante

class AssinanteGratuito(Assinante):
    def __init__(self, tipo):
        self.__tipo = tipo
        self.__faixa_anuncios = True
        self.__limite_pulos = 5
        self.__alta_qualidade = False
        self.__ouvir_offline = False
        
    @property
    def tipo(self):
        return self.__tipo

    def pular_musica(self):
        if limite_pulos <= 8:
            print("Pulando música...")
            limite_pulos -= 1
        else:
            print("Pulos esgotados.")

    def baixar_musica(self):
        print('Indisponível no plano gratuito.')

    def trocar_qualidade(self):
        print('Indisponível no plano gratuito.')
