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

if ouvinte_ou_artista == '1':
    loop = True
    while loop:
        print('\nO que deseja fazer?')
        print(' ----------------------')
        print('| 1. Tocar conteúdo    |')
        print('| 2. Pular faixa       |')
        print('| 3. Trocar qualidade  |')
        print('| 4. Download          |')
        print('| 5. Ver meu histórico |')
        print('| 6. Sair              |')
        print(' ----------------------')
        opcao = input('Opção: ')
        if opcao in ['1', '2', '3', '4', '5', '6']:
            match opcao:
                case '1':
                    print('\nQual tipo de conteúdo?')
                    print(' -----------------')
                    print('| 1. Música       |')
                    print('| 2. Podcast      |')
                    print('| 3. Audiolivro   |')
                    print('| 4. Som Ambiente |')
                    print(' -----------------')
                    opcaoTipo = input('Opção: ')
                    index = 0
                    match opcaoTipo:
                        case '1':
                            print('Músicas: ')
                            for item in service.musicas:
                                index += 1
                                print(index, '-', item.titulo)
                            qualTocar = int(input('Qual tocar? '))
                            try:
                                print(f'Tocando "{service.musicas[qualTocar - 1].titulo}..."')
                                ouvinte.adicionar_historico(service.musicas[qualTocar - 1].titulo)
                            except:
                                print('Opção Inválida.')
                        case '2':
                            print('Podcasts: ')
                            for item in service.podcasts:
                                index += 1
                                print(index, '-', item.titulo)
                            qualTocar = int(input('Qual tocar? '))
                            try:
                                print(f'Tocando "{service.podcasts[qualTocar - 1].titulo}..."')
                                ouvinte.adicionar_historico(service.podcasts[qualTocar - 1].titulo)
                            except:
                                print('Opção Inválida.')
                        case '3':
                            print('Audiolivros: ')
                            for item in service.audiolivros:
                                index += 1
                                print(index, '-', item.titulo)
                            qualTocar = int(input('Qual tocar? '))
                            try:
                                print(f'Tocando "{service.audiolivros[qualTocar - 1].titulo}..."')
                                ouvinte.adicionar_historico(service.audiolivros[qualTocar - 1].titulo)
                            except:
                                print('Opção Inválida.')
                        case '4':
                            print('Sons ambiente: ')
                            for item in service.sons_ambiente:
                                index += 1
                                print(index, '-', item.titulo)
                            qualTocar = int(input('Qual tocar? '))
                            try:
                                print(f'Tocando "{service.sons_ambiente[qualTocar - 1].titulo}..."')
                                ouvinte.adicionar_historico(service.sons_ambiente[qualTocar - 1].titulo)
                            except:
                                print('Opção Inválida')
                        case _:
                            print('Opção Inválida')
                            break
                case '2':
                    ouvinte.pular_musica()
                case '3':
                    ouvinte.trocar_qualidade()
                case '4':
                    ouvinte.baixar_musica()
                case '5':
                    print('Histórico: ')
                    for item in ouvinte.historico:
                        print('•', item)
                case '6':
                    loop = False
        else:
            print('Opção inválida.')
else:
    loop = True
    while loop:
        print('\nO que deseja fazer?')
        print(' -------------------------------------------')
        print('| 1. Enviar novo conteúdo                  |')
        print('| 2. Ver desempenho por criador            |')
        print('| 3. Ver dados financeiros                 |')
        print('| 4. Sair                                  |')
        print(' -------------------------------------------')
        opcao = input('Opção: ')
        if opcao in ['1', '2', '3','4','5']:
            loop = False
            match opcao:
                case '1':
                    pass
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    loop = False
        else:
            print('Opção inválida.')