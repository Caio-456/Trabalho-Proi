# Integrantes: Alice Matos Ferreira, Caio Motta Barcelos, Davi Quinelato Falçoni e Eduarda Aleixo Felizardo.

# Imports:
from Models.Assinante.Assinante import Assinante
from Models.Assinante.AssinanteFamilia import AssinanteFamilia
from Models.Assinante.AssinanteGratuito import AssinanteGratuito
from Models.Assinante.AssinantePremium import AssinantePremium

from Models.Artista.Artista import Artista
from Models.Artista.Gravadora import Gravadora
from Models.Artista.Independente import Independente
from Models.Artista.Podcaster import Podcaster

from Services.ConteudoServices import ConteudoServices

# Carregar Catálogo:
service = ConteudoServices()
service.carregar_csv("lancamentos.csv")
service.salvar_no_banco()

'''
print(service.musicas)
print(service.podcasts)
print(service.audiolivros)
print(service.sons_ambiente)
print(service.erros)
'''

print('\nBem-vindo!')

loop = True
while loop:
    print('\nComo quem você quer entrar? ')
    print(' ----------------')
    print('| 1. Sou Ouvinte |')
    print('| 2. Sou Artista |')
    print(' ----------------')
    ouvinte_ou_artista = input('Insira a opção: ')
    if ouvinte_ou_artista in ['1', '2']:
        loop = False
    else: print('Opção inválida.')


if ouvinte_ou_artista == '1':
    loop = True
    while loop:
        print('\nSelecione o plano: ')
        print(' -------------------')
        print('| 1. Plano Gratuito |')
        print('| 2. Plano Premium  |')
        print('| 3. Plano Família  |')
        print(' -------------------')
        tipo_ouvinte = input('Insira a opção: ')
        if tipo_ouvinte in ['1', '2', '3']:
            loop = False
            match tipo_ouvinte:
                case '1':
                    ouvinte = AssinanteGratuito(1)
                case '2':
                    ouvinte = AssinantePremium(2)
                case '3':
                    ouvinte = AssinanteFamilia(3)
        else:
            print('Opção inválida.')
        print(ouvinte.tipo)
else:
    loop = True
    while loop:
        print('\nSelecione o tipo: ')
        print(' -------------------------')
        print('| 1. Artista Independente |')
        print('| 2. Podcaster            |')
        print('| 3. Gravadora            |')
        print(' -------------------------')
        tipo_artista = input('Insira a opção: ')
        if tipo_artista in ['1', '2', '3']:
            loop = False
            match tipo_artista:
                case '1':
                    nome = input('Insira o nome: ')
                    ouvinte = Independente(nome)
                case '2':
                    nome = input('Insira o nome: ')
                    ouvinte = Podcaster(nome)
                case '3':
                    nome = input('Insira o nome: ')
                    pais = input('Insira o país: ')
                    ouvinte = Gravadora(nome, pais)
        else:
            print('Opção inválida.')

'''
def menu_ouvinte():
    print('\nO que deseja fazer?')
    print(' -------------------------------------------')
    print('| 1. Abrir conteúdo                        |')
    print('| 2. Pular faixa                           |')
    print('| 3. Trocar qualidade                      |')
    print('| 4. Download offline                      |')
    print('| 5. Ver meu histórico                     |')
    print('| 6. Sair                                  |')
    print(' -------------------------------------------')
    return input('Opção: ')

def menu_artista():
    print('\nO que deseja fazer?')
    print(' -------------------------------------------')
    print('| 1. Enviar novo conteúdo                  |')
    print('| 2. Importar CSV de catálogo              |')
    print('| 3. Ver desempenho por criador            |')
    print('| 4. Ver dados financeiros (se autorizado) |')
    print('| 5. Sair                                  |')
    print(' -------------------------------------------')
'''