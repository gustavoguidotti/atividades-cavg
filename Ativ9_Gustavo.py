# Gustavo Guidotti

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
operacao = int(input('Digite 1 para adicao\nDigite 2 para subtracao\nDigite 3 para multiplicacao\nDigite 4 para divisao\n'))

match operacao:
    case 1:
        resultado = num1 + num2
    case 2:
        resultado = num1 - num2
    case 3:
        resultado = num1 * num2
    case 4:
        resultado = num1 / num2
    case _:
        resultado = 'Algo deu errado, tente novamente.'

print(resultado)

''' 
1) Construa um algoritmo que leia um número inteiro de 1 a 7 e informe o dia da semana
correspondente, sendo domingo o dia de número 1. Se o número não corresponder
a um dia da semana, mostre uma mensagem de erro. '''

# dia = int(input('Digite o numero da semana (de 1 a 7): '))

# match dia:
#     case 1:
#         print('Domingo.')
#     case 2:
#         print('Segunda.')
#     case 3:
#         print('Terca.')
#     case 4:
#         print('Quarta.')
#     case 5:
#         print('Quinta.')
#     case 6:
#         print('Sexta.')
#     case 7:
#         print('Sabado.')
#     case _:
#         print('Numero invalido.')

''' 
2) Construa um algoritmo que solicite um mês do ano (01 a 12) e, de acordo com as
condições abaixo, dizer : 01 (Férias), 02 a 06 (1º semestre letivo), 07 (Recesso), 08
a 11 (2º semestre letivo), 12 (Férias). '''

# mes = int(input('Digite o numero do mes: '))

# match mes:
#     case 1 | 12:
#         print('Ferias.')
#     case mes if mes in range(2, 7):
#         print('1º semestre letivo.')
#     case mes if mes in range(8, 12):
#         print('2º semestre letivo.')
#     case 7:
#         print('Recesso.')
#     case other:
#         print('Numero invalido, por favor tente novamente.')

''' 
3) Escreva um algoritmo que leia o código de um determinado produto e mostre a sua
classificação.  '''

# codigo = int(input('Digite o codigo do produto: '))

# match codigo:
#     case 1:
#         print('Alimento nao perecivel.')
#     case 2 | 3 | 4:
#         print('Alimento perecivel.')
#     case 5 | 6:
#         print('Vestuario.')
#     case 7 :
#         print('Higiene pessoal.')
#     case codigo if codigo in range(8, 16):
#         print('Limpeza e utensilios domesticos.')
#     case other:
#         print('Numero invalido, por favor tente novamente.')

''' 
4) Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias. '''

# idade = int(input('Digite a sua idade: '))

# match idade:
#     case 5 | 6 | 7:
#         print('Infantil A.')
#     case 8 | 9 | 10:
#         print('Infantil B.')
#     case 11 | 12 | 13:
#         print('Juvenil A.')
#     case 14 | 15 | 16 | 17:
#         print('Juvenil B.')
#     case idade if idade > 17:
#         print('Adulto.')
#     case other:
#         print('Desculpe, voce nao se encaixa em nenhuma categoria.')

''' 
5) O programa de uma loja de móveis mostra o seguinte menu na tela de vendas:
1-Venda a Vista
2-Venda a Prazo 30 dias
3-Venda a Prazo 60 dias
4-Venda a Prazo com 90 dias
5-Venda com cartão de débito
6-Venda com cartão de crédito
Escolha a opção:'''

valor_venda = int(input('Digite o valor da compra: '))
forma_pagamento = int(input('1-Venda a Vista\n2-Venda a Prazo 30 dias\n3-Venda a Prazo 60 dias\n4-Venda a Prazo com 90 dias\n5-Venda com cartão de débito\n6-Venda com cartão de crédito\nEscolha a opção: '))

# match forma_pagamento:
#     case 1:
#         valor_final = f'Valor final: R${valor_venda * 0.9: .2f}'
#     case 2:
#         valor_final = f'Valor final: R${valor_venda * 0.95: .2f}'
#     case 3:
#         valor_final = f'Valor final: R${valor_venda: .2f}'
#     case 4:
#         valor_final = f'Valor final: R${valor_venda * 1.05: .2f}'
#     case 5:
#         valor_final = f'Valor final: R${valor_venda * 0.92: .2f}'
#     case 6:
#         valor_final = f'Valor final: R${valor_venda * 0.93: .2f}'
#     case other:
#         valor_final = 'Algo deu errado, por favor tente novamente.'

# print(valor_final)

