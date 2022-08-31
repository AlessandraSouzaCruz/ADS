#EXERCICIO 2
#Identificação da Pizzaria
print('Olá, seja bem vindo(a) a Pizzaria da Alessandra de Cássia Souza Cruz - 4184047!')
print('Cardápio:')

#Cardápio da Pizzaria
print('*---------------* Cardápio *--------------*')
print('| CÓDIGO | DESCRIÇÃO  | PIZZA M | PIZZA G |')
print('| 21     | Napolitana | R$20.00 | R$26.00 |')
print('| 22     | Marguerita | R$20.00 | R$26.00 |')
print('| 23     | Calabresa  | R$25.00 | R$32.50 |')
print('| 24     | Toscana    | R$30.00 | R$39.00 |')
print('| 25     | Portuguesa | R$30.00 | R$39.00 |')
print('*-----------------------------------------*')

#Tamanho da Pizza para escolha do cliente
subtotal = 0
while (True):
    tamanho = input('Qual o tamanho da pizza desejada (M/G)? ')
    if (tamanho == 'M'):
        tamanho = 'Medio'
    elif (tamanho == 'G'):
        tamanho = 'Grande'
    else:
        print('Tamanho inválido. Digite o Tamanho desejado: M ou G? ')
        continue

#Código da pizza com o valor conforme o sabor da pizza e o tamanho
    codigo = input('Qual o código do sabor desejado: ')
    if (codigo == '21'): #Sabor da pizza
        pizza = 'Napolitana'
        if (tamanho == 'Medio'):
            subtotal = subtotal + 20
        else:#20 reais
            subtotal = subtotal + 20
    elif (codigo == '22'):#Sabor da pizza
        pizza='Marguerita'
        if (tamanho == 'Medio'):#20 reais
            subtotal = subtotal + 20
        else:#26 reais
            subtotal = subtotal + 26
    elif (codigo == '23'):#Sabor da pizza
        pizza='Calabresa'
        if (tamanho == 'Medio'):#25 reais
            subtotal = subtotal + 25
        else:#32.50 reais
            subtotal = subtotal + 32.50
    elif (codigo == '24'):#Sabor da pizza
        pizza='Toscana'
        if (tamanho == 'Medio'):#30 reais
            subtotal = subtotal + 30
        else:#39.50 reais
            subtotal = subtotal + 39.50
    elif (codigo == '25'):#Sabor da pizza
        pizza='Portuguesa'
        if (tamanho == 'Medio'):#30 reais
            subtotal = subtotal + 30
        else:#39.50 reais
            subtotal = subtotal + 39.50
    else:
        print('Código incorreto, digite novamente.')
        continue

#Resumo do primeiro Pedido
    print('Você pediu uma pizza {}.'.format(pizza))

#Caso o cliente queira realizar um novo Pedido ou encerrar
    print('Deseja mais alguma coisa?')
    print('1 - SIM')
    print('2 - NÃO')
    pedido = input('>> ')
    if (pedido == '1'):#Caso ele queria mais uma pizza
        continue
    elif (pedido == '0'):#Caso ele queria encerrar o pedido
        print('O total a ser pago é R$ {:.2f}. Volte sempre!'.format(subtotal))
        break
    else:
        print('Operação invalida.')
        continue