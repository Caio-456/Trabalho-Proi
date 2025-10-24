import Artista
from Models.Conteudo import Musica

class Independente(Artista):
    def __init__(self, nome, saldo, streamsMensais = 0, salario = 0):
        super().__init__(self, nome, saldo)
        self.__streamsMensais = streamsMensais
        self.__salario = salario

    def enviarMusica(self):
        titulo = input('Insira o título da música: ')
        data = input('Insira a data de lançamento: ')
        genero = input('Insira o gênero da música a: ')
        duracao = input('Insira a duração da música (em segundos): ')
        iscrMusica = input('Insira o ISCR: ')
        album = input('Insira o álbum: ')
        numeroFaixa = input('Insira número da faixa: ')
        selo = input('Insira quem é o selo musical: ')
        explicito = input('Essa música contém conteúdo explicíto?(s/n) ')
        musicaAdd = Musica(titulo, self, data, genero, duracao, iscrMusica, album, numeroFaixa, selo, explicito)
        print('Música enviada com sucesso!')

    def receber(self):
        salario = self.__streamsMensais * 0.1