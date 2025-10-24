import Assinante

class Familia(Assinante):
    def __init__(self, perfis_conta = {}, faixa_anuncios = False, alta_qualidade = True, ouvir_offline = True):
        super().__init__(
            tipo = "Família",
            preco = 40.90)
        
        self.__perfis_conta = perfis_conta
        self.__faixa_anuncios = faixa_anuncios
        self.__alta_qualidade = alta_qualidade
        self.__ouvir_offline = ouvir_offline


    def adicionar_perfil(self):
        if len(self.__perfis_conta) <= 5:
            print("Adicionando perfil ao plano...")
        else:
            print("Não é possível adicionar mais perfis a este plano.")

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