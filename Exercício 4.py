#Exercício 4
# Criação de Software com as seguintes funções:
# 1- Cadastrar Produto
# 2- Consultar Produtos(s) - abre outro menu com as seguintes oções: Consultar Todos os Produtos Consultar Produto(s) por Código, Consultar Produto(s) por Fabricante e Retornar ao menu anterior.
# 3- Remover Produto
# 4- Sair

#Lista de produtos
listaprodutos = []

#Menu para cadastrar produtos
def cadastroProduto(codigoproduto):
    print('Você selecionou a opção 01 - Cadastrar produto')
    print('O produto cadastrado é: {}'.format(codigoproduto))
    nomeproduto = input('Digite o nome do produto: ')
    fabricanteproduto = input('Digite o fabricante do produto: ')
    precoproduto = input('Digite o preço do produto: ')
    dicionarioProdutos = {'nomeproduto' : nomeproduto,
                         'fabricanteproduto': fabricanteproduto,
                         'precoproduto' : precoproduto,
                         'codigoproduto'  : codigoproduto}
    listaprodutos.append(dicionarioProdutos.copy())

#Menu para consultar produtos
def consultarProduto():
    while True:
        try:
            print('Você selecionou a opção 02 - Consultar produto(s)')
            opConsultar = input('Entre com a opção desejada:\n'
                                'A - Consultar Todos os Produtos\n'
                                'B - Consultar Produto(s) por Código\n'
                                'C - Consultar Produto(s) por Fabricante\n' 
                                'D - Retornar ao menu anterior\n'
                                '>> ')
            if (opConsultar == 'A'):
                print('Você selecionou: Consultar todos os produtos')
                for produto in listaprodutos: #Selecionar cada produto da lista
                    for key, value in produto.items(): #Selecionar cada campo do dicionário
                        print('{} : {}' .format(key,value))
            elif (opConsultar == 'B'):
                print('Você selecionou: Produto(s) por Código')
                entrada = int(input('Digite o código desejado: '))
                for produto in listaprodutos:  # Selecionar cada produto da lista
                    if(produto['codigoproduto'] == entrada):
                        for key, value in produto.items():
                            print('{} : {}' .format(key,value))
            elif (opConsultar =='C'):
                print('Você selecionou: Consultar Produto(s) por Fabricante')
                escolha = input('Digite o fabricante desejado: ')
                for produto in listaprodutos:  # Selecionar cada produto da lista
                    if(produto['fabricanteproduto'] == escolha):
                        for key, value in produto.items():
                            print('{} : {}' .format(key,value))
            elif (opConsultar == 'D'):
                return
            else:#Em caso de digitação incorreta, retorna ao cliente a opção correta
                print('Opção incorreta. Escolha entre A, B, C ou D.')
                continue
        except ValueError:
            print('Opção incorreta. Tente novamente.')

#Menu para remover produtos
def removerProduto():
    while True:
        try:
            print('Você selecionou a opção 03 - Remover Produto')
            escolha = int(input('Digite o código que deseja excluir: '))
            for produto in listaprodutos:  # Selecionar cada produto da lista
                if (produto['codigoproduto'] == escolha):
                    for key, value in produto.items():
                        listaprodutos.remove(produto)
                        return
        except:
            print('Código não localizado.')
        continue


#Menu de entrada software de controle de estoque para uma mercearia
print('Seja Bem Vindo(a) ao Controle de Estoque da Marcearia da Alessandra de Cássia Souza Cruz - 4184047\n')
codigoproduto = 0
while True:
    escolha = input('Escolha a opção desejada:\n'
                        '1- Cadastrar Produto\n'
                        '2- Consultar Produtos(s)\n'
                        '3- Remover Produto\n'
                        '4- Sair'
                        '\n>> ')
    if (escolha == '1'):
        codigoproduto = codigoproduto + 1
        cadastroProduto(codigoproduto)
        continue
    elif (escolha == '2'):
        consultarProduto()
    elif (escolha == '3'):
        removerProduto()
    elif escolha == '4': #Finaliza o programa
        print('Programa encerrado...')
        break
    else:#Em caso de digitação incorreta, retorna ao cliente a opção correta
        print('Opção incorreta, tente novamente.')
        continue