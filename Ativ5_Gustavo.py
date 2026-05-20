''' 1. Escreva um algoritmo para determinar se um dado número N é POSITIVO ou NEGATIVO. '''

# num = int(input('Digite um numero: '))
# if num > 0:
#     print('Numero positivo!')
# elif num < 0:
#     print('Numero negativo')
#------------------------------------------------------------------------------------------------------------

''' 2. Escreva um algoritmo que leia um número e imprima a raiz quadrada do número
caso ele seja positivo ou igual a zero. '''

# num = int(input('Digite um numero: '))
# if num >= 0: 
#     num = num ** 0.5
#     print(f'A raiz quadrada desse numero: {num}')
#------------------------------------------------------------------------------------------------------------

''' 3. Escreva um algoritmo que leia um número e escreva se este número é PAR ou
ÍMPAR. '''

# num = int(input('Digite um numero: '))
# if (num % 2 == 0):
#     print('Numero par.')
# else:
#     print('Numero impar.')
#------------------------------------------------------------------------------------------------------------

''' 4. Escreva um algoritmo que leia dois números e efetue a adição. Caso o valor somado
seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o
valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5. '''

# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))
# soma = num1 + num2
# if soma > 20:
#     soma += 8
# else:
#     soma -= 5
# print(soma)
#------------------------------------------------------------------------------------------------------------

''' 5. Escreva um algoritmo que leia dois números A e B e imprima qual o maior deles. '''

# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))
# if num1 > num2:
#     print('O primeiro numero e maior.')
# elif num1 < num2:
#     print('O segundo numero e maior.')
# else:
#     print('Os numeros sao iguais.')
#------------------------------------------------------------------------------------------------------------

''' 6. Ler o nome de 2 times e o número de gols marcados na partida (para cada time).
Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a
palavra EMPATE. '''

# nomeTime1 = input('Digite o nome do time 1: ')
# golsTime1 = int(input(f'Quantos gols o {nomeTime1} marcou? '))
# nomeTime2 = input('Digite o nome do time 2: ')
# golsTime2 = int(input(f'Quantos gols o {nomeTime2} marcou? '))

# if golsTime1 > golsTime2:
#     print(f'{nomeTime1} venceu!')
# elif golsTime1 < golsTime2:
#     print(f'{nomeTime2} venceu!')
# else:
#     print('EMPATE!')
#------------------------------------------------------------------------------------------------------------

''' 7. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
para homens: (72.7 * altura) - 58
para mulheres: (62.1 * altura) - 44.7 '''

# altura = float(input('Digite a sua algura: '))
# sexo = int(input('Qual o seu sexo?\nDigite 1 para homem.\nDigite 2 para mulher.\n'))
# if sexo == 1:
#     pesoIdeal = (72.7 * altura) - 58
# elif sexo == 2:
#     pesoIdeal = (62.1 * altura) - 44.7
# print(f'Seu peso ideal: {pesoIdeal: .2f}')
#------------------------------------------------------------------------------------------------------------

''' 8. Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 5,50 e o preço
do litro do álcool é R$ 6,90. '''

# litros = float(input('Quantos litros voce abasteceu? '))
# tipoDeCombustivel = input('Voce abasteceu com?\nA-álcool\nG-gasolina\n').lower()
# if tipoDeCombustivel == 'a':
#     valorDoCombustivel = 6.90
# elif tipoDeCombustivel == 'g':
#     valorDoCombustivel = 5.5
# if litros > 0 and (tipoDeCombustivel == 'a' or tipoDeCombustivel == 'g'):
#     valorPago = valorDoCombustivel * litros
#     print(f'Valor pago pelo combustivel: R${valorPago: .2f}')
#------------------------------------------------------------------------------------------------------------

""" 9. Em uma fruteira X, as maçãs custam R$ 3,00 cada se forem compradas menos do
que uma dúzia, e R$ 2,50 se forem compradas pelo menos doze. Escreva um
programa que leia o número de maçãs compradas, calcule e escreva o valor total da
compra. """

# numMacas = int(input('Quantas macas voce esta comprando? '))
# if numMacas < 12:
#     valorTotal = numMacas * 3
# else:
#     valorTotal = numMacas * 2.5
# if valorTotal > 0:
#     print(f'Valor total a ser pago: R${valorTotal}')
#------------------------------------------------------------------------------------------------------------

""" 10.Elaborar um algoritmo que leia a velocidade permitida em uma estrada e a
velocidade de um condutor. Se a velocidade for inferior ou igual à permitida, exiba a
mensagem “Sem Multa”. Se a velocidade for de até 20% maior que a permitida, exiba
a mensagem “Multa Grave” """

# while True:
#     velocidadePermida = int(input('Digite a velocidade maxima permitida: '))
#     velocidadeRegistrada = int(input('Digite a velocidade registrada: '))
#     if velocidadePermida > 0 and velocidadeRegistrada > 0:
#         break

# if velocidadeRegistrada <= velocidadePermida:
#     print('Sem Multa')
# elif velocidadeRegistrada > velocidadePermida * 1.2:
#     print('Multa Gravissima')
# else:
#     print('Multa Grave')