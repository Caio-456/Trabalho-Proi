from Models.Assinante.Assinante import Assinante

class AssinanteFamilia(Assinante):
    def __init__(self, tipo):
        self.__tipo = tipo
        self.__perfis_conta = {}
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
    
    @property
    def perfis_conta(self):
        return self.__perfis_conta

    def adicionar_perfil(self, usuario, idade):
        self.__perfis_conta[usuario] = idade
        print('Perfil adicionado.')

    def baixar_musica(self, musica, usuario):
        if self.__perfis_conta[usuario] < 18:
            print('Ativando Controle Parental')
            print(f'A música {musica.titulo} foi baixada')
        else:
            print(f'A música {musica.titulo} foi baixada')

    def tocar_musica(self, usuario):
        if self.__perfis_conta[usuario] < 18:
            print('Ativando Controle Parental')
            print(f'Tocando')
        else:
            print(f'Tocando')
