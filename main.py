
# RM553521 - Rafael Cristofali

# 1 - Escreva um código que conte quantas vezes cada palavra aparece na
# frase abaixo e guarde num dicionário as palavras como chave e as ocorrências como valor


frase = 'Concluímos que chegamos à conclusão que não concluímos nada. Por isso, conclui-se que a conclusão será concluída quando todas tiverem concluído que já é tempo de concluir uma conclusão.'

for char in '.,':
    frase = frase.replace(char, '')
frase_array = frase.lower().split(' ')

dic = {}
for p in frase_array:
    if (p not in dic.keys()):
        dic[p] = 1
    else:
        dic[p] += 1
for key in dic.keys():
    print(f'A palavra "{key}" aparece {dic[key]} vez(es)')



# 2 - Dado o dicionário abaixo, dê uma opção para o usuário buscar qual o carro mais
# caro ou o mais barato e traga todas as informações sobre ele na tela.
# Dê também a opção do usuário remover todas as infos sobre um carro ou cadastrar
# um novo carro. Isso tudo deve estar dentro de um laço de repetição e deve haver a
# opção 'sair' para quebrar o loop e encerrar.


carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4,2,6,2],
    'preço': [1000,200,300,100],
    'ano de fabricação': [2014,2018,1970,2005]
}

menu = ['Mais Caro', 'Mais Barato', 'Remover', 'Cadastrar', 'Sair']

indices = []

def main():
    global indices
    indices = atualizaIndices()
    print('Bem-vindo ao nosso sistema!')

    menu_selecionado = selecionarMenu()
    while (menu_selecionado != 'Sair'):
        print(f'|----- {menu_selecionado.upper()} -----|')
        if (menu_selecionado == 'Mais Caro'):
            maisCaro()
        elif (menu_selecionado == 'Mais Barato'):
            maisBarato()
        elif (menu_selecionado == 'Remover'):
            remover()
            indices = atualizaIndices()
        elif (menu_selecionado == 'Cadastrar'):
            cadastrar()
            indices = atualizaIndices()
        menu_selecionado = selecionarMenu()
    print('Obrigado por utilizar nosso sistema!')

def atualizaIndices():
   return {carros['nomes'][i] : i for i in range(len(carros['nomes']))}

def inputComValidacao(inputText, options, showOptions = False):
    if (showOptions):
        inputText += '\n' + '\n'.join(options) + '\n'
    value = input(inputText)
    while (value not in options):
        print('Opção inválida!')
        value = input(inputText)
    return value

def selecionarMenu():
    print('|----- MENU -----|')
    for m in menu:
        print(m)
    return inputComValidacao('', menu)

def maisCaro():
    indice_caro = 0
    for i in range(len(carros['preço'])):
        if (float(carros['preço'][i]) > float(carros['preço'][indice_caro])):
            indice_caro = i
    print(f'O carro mais caro é:')
    for key in carros.keys():
        print(f'{key}: {carros[key][indice_caro]}')
    return

def maisBarato():
    indice_barato = 0
    for i in range(len(carros['preço'])):
        if (float(carros['preço'][i]) < float(carros['preço'][indice_barato])):
            indice_barato = i
    print(f'O carro mais barato é:')
    for key in carros.keys():
        print(f'{key}: {carros[key][indice_barato]}')
    return

def remover():
    carro_remover = inputComValidacao('Qual carro deseja remover? ', carros['nomes'], True)
    indice_remover = indices[carro_remover]
    for key in carros.keys():
        carros[key].pop(indice_remover)

    print('Carro removido!')
    return

def cadastrar():
    for key in carros.keys():
        info = input(f'Digite o/a {key}: ')
        carros[key].append(info)
    return

main()
