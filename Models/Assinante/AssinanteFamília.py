import Assinante

class Familia(Assinante):
    def __init__(self, perfis_conta = 5, controle_parental = True, faixa_anuncios = False, alta_qualidade = True, ouvir_offline = True):
        super().__init__(
            tipo = "Família",
            preco = 40.90)
        
        self.__perfis_conta = perfis_conta
        self.__controle_parental = controle_parental
        self.__faixa_anuncios = faixa_anuncios
        self.__alta_qualidade = alta_qualidade
        self.__ouvir_offline = ouvir_offline


    def add_perfil(self):
        if perfis_conta <= 5:
            print("Adicionando perfil ao plano...")
            perfis_conta -= 1
            
        else:
            print("Não é possível adicionar mais perfis a esta conta.")

    def baixar_musica(self, musica):
        print(f'A música {musica.titulo} foi baixada')
