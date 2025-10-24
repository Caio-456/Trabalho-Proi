# Integrantes: Alice Matos Ferreira, Caio Motta Barcelos, Davi Quinelato Falçoni e Eduarda Aleixo Felizardo.

# from Services.instrucoes"Caminho" import "classe"

def quem_esta_usando():
    print('Selecione uma opção: ')
    print(' ----------------')
    print('| 1. Sou ouvinte |')
    print('| 2. Sou Artista |')
    print(' ----------------')
    ouvinte_ou_artista = input('Insira a opção: ')
    if ouvinte_ou_artista not in ['1', '2']:
        raise Exception('Opção Inválida.')
    return ouvinte_ou_artista

print('Bem-vindo!')
try:
    ouvinte_ou_artista = quem_esta_usando()
except:
    ouvinte_ou_artista = quem_esta_usando()

print('\n Selecione uma opção: ')
print(' ----------------')
print('| 1. Login        |')
print('| 2. Cadastro     |')
print(' ----------------')
login_ou_cadastro = input('Insira a opção: ')
if login_ou_cadastro not in ['1', '2']:
    raise Exception('Opção Inválida.')

'''
if login_ou_cadastro == '1':
    matchouvinte_ou_artista:
        case '1':
            print('\n Selecione uma opção: ')
            print(' ----------------')
            print('| 1. Login        |')
            print('| 2. Cadastro     |')
            print(' ----------------')
        case '2':
            print('\n Selecione uma opção: ')
            print(' ----------------')
            print('| 1. Login        |')
            print('| 2. Cadastro     |')
            print(' ----------------')
        case _:
            print('Opção Inválida.')
elif login_ou_cadastro == '2':
    match ouvinte_ou_artista:
        case '1':
            print('\n Selecione uma opção: ')
            print(' ----------------')
            print('| 1. Login        |')
            print('| 2. Cadastro     |')
            print(' ----------------')
        case '2':
            print('\n Selecione uma opção: ')
            print(' ----------------')
            print('| 1. Login        |')
            print('| 2. Cadastro     |')
            print(' ----------------')
        case _:
            print('Opção Inválida.')
else:
    'Opção Inválida'
    '''