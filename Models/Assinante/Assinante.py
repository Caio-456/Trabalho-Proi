class Assinante:
    def __init__(self, tipo, preco):
        self.__tipo = tipo
        self.__preco = preco

    def pular_musica(self):
        print("Pulando música...")

    def baixar_musica(self):
        print('A música foi baixada.')

    def trocar_qualidade(self):
        print('Qualidade trocada.')

    def tocar_musica(self, usuario):
        print('Tocando Música')