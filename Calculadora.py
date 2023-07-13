import os

# Exemplo de cores
cor_vermelho = '\033[91m'
cor_verde = '\033[92m'
cor_amarelo = '\033[93m'
cor_azul = '\033[94m'
cor_reset = '\033[0m'

def soma():
    n1 = float(input('Digite o 1º Número:'))
    n2 = float(input('Digite o 2º Número:'))
    soma = n1 + n2
    print('\nSoma = {}'.format(soma))
def subtracao():
    n1 = float(input('Digite o 1º Número:'))
    n2 = float(input('Digite o 2º Número:'))
    sub = n1 - n2
    print('\nSubtração = {}'.format(sub))
def divi():
    n1 = float(input('Digite o 1º Número:'))
    n2 = float(input('Digite o 2º Número:'))
    div = n1 / n2
    print('\nDivisão = {}'.format(div))
def mult():
    n1 = float(input('Digite o 1º Número:'))
    n2 = float(input('Digite o 2º Número:'))
    mult = n1 * n2
    print('\nMultiplicação = {}'.format(mult))
def expon():
    n1 = float(input('Digite o 1º Número:'))
    n2 = float(input('Digite o 2º Número:'))
    expo = n1 ** n2
    print('\nExponenciação = {}'.format(expo))
    
def menu():
    print(cor_verde + '##### MENU #####') # Coloca a cor azul no texto
    print('0 - Soma')
    print('1 - Subtração')
    print('2 - Divisão')
    print('3 - Multiplicação')
    print('4 - Exponenciação')
    print('--------------------' + cor_reset)

    opcoes = [soma, subtracao, divi, mult, expon]
    escolha = int(input(cor_azul+'Seleciona a Opção desejada:'))
    if escolha >= 0 and escolha < len(opcoes):
        opcoes[escolha]()
    else:
        print(cor_vermelho + '\nOpção inválidade!' + cor_reset)
        
while True:
    os.system('clear')
    menu()
    cond = int(input(cor_amarelo+'\nDeseja fazer outra Operação?'
                     +cor_verde+'\n0 - Sim'+cor_reset
                     +'\n'+cor_vermelho+'1 - Não\n'+cor_reset))
    if cond == 1:
        break
    
    
