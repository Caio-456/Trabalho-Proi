# Imports:
from Models.Assinante.AssinanteFamilia import AssinanteFamilia
from Models.Assinante.AssinanteGratuito import AssinanteGratuito
from Models.Assinante.AssinantePremium import AssinantePremium

from Models.Artista.Gravadora import Gravadora
from Models.Artista.Independente import Independente
from Models.Artista.Podcaster import Podcaster

from Services.ConteudoServices import ConteudoServices


def inicializar_servico():
    service = ConteudoServices()
    service.carregar_csv("lancamentos.csv")
    service.salvar_no_banco()
    service.adicionarPlays() # Adiciona coluna de plays as músicas.
    return service


def menu_login():
    while True:
        print('\nComo quem você quer entrar? ')
        print(' ----------------')
        print('| 1. Sou Ouvinte |')
        print('| 2. Sou Artista |')
        print(' ----------------')
        opcao = input('Insira a opção: ')
        
        if opcao in ['1', '2']:
            return opcao
        
        print('Opção inválida.')


def menu_ouvinte_tipo():
    while True:
        print('\nSelecione o plano: ')
        print(' -------------------')
        print('| 1. Plano Gratuito |')
        print('| 2. Plano Premium  |')
        print('| 3. Plano Família  |')
        print(' -------------------')
        tipo = input('Insira a opção: ')
        
        if tipo == '1':
            return AssinanteGratuito(1)
        if tipo == '2':
            return AssinantePremium(2)
        if tipo == '3':
            ouvinte = AssinanteFamilia(3)
            for _ in range(5):
                adicionar = input('Adicionar um perfil à conta?(s/n) ')
                if adicionar == 's':
                    nome = input('Nome: ').lower()
                    idade = input('Idade: ')
                    ouvinte.adicionar_perfil(nome, idade)
                elif adicionar == 'n':
                    break
                else:
                    print('Opção inválida.')
            return ouvinte
        
        print('Opção inválida.')


def menu_artista_tipo():
    while True:
        print('\nSelecione o tipo: ')
        print(' -------------------------')
        print('| 1. Artista Independente |')
        print('| 2. Podcaster            |')
        print('| 3. Gravadora            |')
        print(' -------------------------')
        tipo = input('Insira a opção: ')
        
        if tipo in ['1', '2', '3']:
            nome = input('Insira o nome: ')
            
            if tipo == '1':
                return Independente(nome)
            if tipo == '2':
                return Podcaster(nome)
            if tipo == '3':
                pais = input('Insira o país: ')
                return Gravadora(nome, pais)
        
        print('Opção inválida.')


def tocar_conteudo(ouvinte, service):
    print('\nQual tipo de conteúdo?')
    print(' -----------------')
    print('| 1. Música       |')
    print('| 2. Podcast      |')
    print('| 3. Audiolivro   |')
    print('| 4. Som Ambiente |')
    print(' -----------------')
    tipo = input('Opção: ')
    
    service.carregar_do_banco()
    colecoes = {
        '1': service.musicas,
        '2': service.podcasts,
        '3': service.audiolivros,
        '4': service.sons_ambiente
    }
    
    if tipo not in colecoes:
        print('Opção inválida.')
        return
    
    conteudos = colecoes[tipo]
    for i, item in enumerate(conteudos, start = 1):
        print(i, '-', item.titulo)
    
    try:
        id = int(input('Qual tocar? ')) - 1
        conteudo = conteudos[id]
    except:
        print('Opção inválida.')
        return
    
    print(f'Tocando "{conteudo.titulo}..."')
    ouvinte.adicionar_historico(conteudo.titulo)


def menu_ouvinte(ouvinte, service):
    while True:
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
        
        if opcao == '1':
            tocar_conteudo(ouvinte, service)
        elif opcao == '2':
            ouvinte.pular_musica()
        elif opcao == '3':
            ouvinte.trocar_qualidade()
        elif opcao == '4':
            ouvinte.baixar_musica()
        elif opcao == '5':
            print('Histórico:')
            for item in ouvinte.historico:
                print('•', item)
        elif opcao == '6':
            break
        else:
            print('Opção inválida.')


def menu_artista(artista, service):
    while True:
        print('\nO que deseja fazer?')
        print(' -------------------------------------------')
        print('| 1. Enviar novo conteúdo                  |')
        print('| 2. Ver desempenho por criador            |')
        print('| 3. Ver saldo                             |')
        print('| 4. Sair                                  |')
        print(' -------------------------------------------')
        opcao = input('Opção: ')
        
        if opcao == '1':
            service.cadastrar_conteudo(artista)
            service.carregar_do_banco()
        elif opcao == '2':
            artista.relatorio_desempenho()
        elif opcao == '3':
            print(f"Saldo atual: R${artista.saldo:.2f}")
        elif opcao == '4':
            break
        else:
            print('Opção inválida.')


service = inicializar_servico()
print('\nBem-vindo!')
    
tipo = menu_login()
    
if tipo == '1':
    ouvinte = menu_ouvinte_tipo()
    menu_ouvinte(ouvinte, service)
else:
    artista = menu_artista_tipo()
    menu_artista(artista, service)