#Exercício 3
#Parte do software referente ao pedido por parte do cliente:
#Código para informar a quantidade desejada de feijoada
def volumeFeijoada():
    while True:
        try:
            print('MENU VOLUME FEIJOADA.')
            volume = float(input('Digite a quantidade que seja (ml): '))
            if (300 <= volume <= 5000): #Somente será permitido valor entre 300 ml e 5l
                valorvolume = (volume * 0.08) #Multiplica o volume escolhido pelo cliente por 0.08
                return valorvolume
            else: #Em caso de digitação incorreta, retorna ao cliente a opção correta
                print('Não aceitamos pedido inferior a 300ml ou maior que 5l. Tente novamente.')
        except:
                print('Não entendemos. Tente novamente!')

#Código para informa ao cliente as opções do Menu
opcao = 1
def opcaoFeijoada():
    while True:
        print('MENU OPÇÃO FEIJOADA')
        print('Escolha a opção de fejoada:')
        print('B- Básica (Feijão + paiol + costelinha)')
        print('P- Premium (Feijão + pail + costelinha + partes de porco)')
        print('S- Suprema (Feijão + pail + costelinha + partes de porco + charque + calabresa + bacon)')
        opcaoFeijo = input('Entre com a opção de fejoada >> ')
        if (opcaoFeijo == 'B'):
            opcao = 1
        elif(opcaoFeijo == 'P'):
            opcao = 1.25
        elif(opcaoFeijo == 'S'):
            opcao = 1.5
        else:
            print('Opção inválida. Tente novamente.')
            continue
        return opcao


#Código caso o cliente queira, opção para informar os acompanhamentos da feijoada
def acompanhamentoFeijoada():
    acomp = float(0) #variavel acumuladora para o acompanhamento
    while True:
        print('Deseja mais algum acompanhamento?')
        print('0- Não desejo mais acompanhamentos')
        print('1- 200g de arroz')
        print('2- 150g de farofa especial')
        print('3- 100g de couve cozida')
        print('4- 1 laranja descascada')
        acompanhaFeijoada = input('Opção >> ')
        if (acompanhaFeijoada == '0'):
            acomp = acomp + 0 #Finaliza o pedido
            return acomp
        elif (acompanhaFeijoada == '1'):
            acomp = acomp + 5 #5reais
            continue
        elif (acompanhaFeijoada == '2'):
            acomp = acomp + 6 #6reais
            continue
        elif (acompanhaFeijoada == '3'):
            acomp = acomp + 7 #7reais
            continue
        elif (acompanhaFeijoada == '4'):
            acomp = acomp + 3 #3reais
            continue
        else:
            print('Opção inválida. Tente novamente!')
            continue
        return acomp

# Código com a identificação da loja

print('Olá, seja bem vindo(a) ao Programa de Feijoada da Alessandra de Cássia Souza Cruz - 4184047!\n')

#Main
volm = volumeFeijoada()
opca = opcaoFeijoada()
acom = acompanhamentoFeijoada()

#Finalização, sabendo que o total é = (volumefeijoada() * opcaoFeijoada()) + acompanhamentoFeijoada())
print('O valor final a ser pago é de: R$ {:.2f}. (Volume: {} * opção {} + acompanhamento: {}.)'.format(((volm*opca)+acom),volm,opca,acom))