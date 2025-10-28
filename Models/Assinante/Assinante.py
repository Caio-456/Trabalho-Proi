class Assinante:
    def __init__(self, tipo):
        self.__tipo = tipo
    
    @property
    def tipo(self):
        return self.__tipo
    
    def adicionar_historico(self, conteudo):
        self.historico.append(conteudo)

    def pular_musica(self):
        print("Pulando música...")

    def baixar_musica(self):
        print('A música foi baixada.')

    def trocar_qualidade(self):
        print('Qualidade trocada.')

    def tocar_musica(self, usuario = 'Não é plano família'):
        print('Tocando Música')