'''
1) Construa um algoritmo para calcular a média de um aluno, dado 3 notas. Após
mostrar na tela se o aluno foi aprovado, reprovado ou está em exame, considerando
que:
Aprovado >=6
Exame >=4
Reprovado < 4 '''

# nota1 = float(input('Digite a nota 1: '))
# nota2 = float(input('Digite a nota 2: '))
# nota3 = float(input('Digite a nota 3: '))
# media = (nota1 + nota2 + nota3) / 3

# if media >= 6:
#     print(f'O aluno foi aprovado com uma media de{media: .2f}')
# elif media < 4:
#     print(f'O aluno foi reprovado com uma media de{media: .2f}')
# else:
#     print(f'O aluno esta em exame com uma media de{media: .2f}')

''' ------------------------------------------------------------------------------------------
2) Escreva um algoritmo que leia dois números A e B e imprima qual o maior, o menor
ou se são iguais. '''

# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))

# if num1 > num2:
#         print(f'O primeiro numero ({num1}) e maior que o segundo ({num2}).')
# elif num1 < num2:
#         print(f'O segundo numero ({num2}) e maior que o primeiro ({num1}).')
# else:
#         print('Os numeros sao iguais.')


''' ------------------------------------------------------------------------------------------
3) Escreva um algoritmo que leia dois números e efetue a subtração. Caso o valor
subtraído seja maior que zero, este deverá ser apresentado somando-se a ele mais
1; caso o valor subtraído seja menor que zero, este deverá ser apresentado
somando-se 1 e caso o valor seja igual a zero, este deverá ser apresentado
somando-se 2. '''

# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))
# subtracao = num1 - num2

# if subtracao > 0:
#     print(f'Subtracao > 0, entao subtracao + 1 = {subtracao + 1}')
# elif subtracao < 0:
#     print(f'Subtracao < 0, entao subtracao + 1 = {subtracao + 1}')
# else:
#     print(f'Subtracao = 0, entao subtracao + 2 = {subtracao + 2}')


''' ------------------------------------------------------------------------------------------
4) Faça um algoritmo que leia os valores A, B e C. Mostre uma mensagem que informe
se a soma de A com B é menor, maior ou igual a C. '''

# a = int(input('Digite um numero para A: '))
# b = int(input('Digite um numero para B: '))
# c = int(input('Digite um numero para C: '))
# somaAB = a + b

# if somaAB > c:
#     print(f'A soma de A e B ({somaAB}) e maior que C ({c})')
# elif somaAB < c:
#     print(f'A soma de A e B ({somaAB}) e menor que C ({c})')
# else:
#     print(f'A soma de A e B ({somaAB}) e igual a C ({c})')


''' ------------------------------------------------------------------------------------------
5) Uma sorveteria vende três tipos de picolés. Sabendo-se que o picolé do tipo 1 é
vendido por R$ 2.50, o do tipo 2 por R$ 2.60 e o do tipo 3 por R$ 2.75, faça um
algoritmo que, para cada tipo de picolé, mostre a quantidade vendida e o total
arrecadado. '''

while True:
    tipo = int(input('Digite:\n1 para picolé de R$ 2.50\n2 para picolé de R$ 2.60\n3 para picolé de R$ 2.75\n'))
    if tipo in [1,2,3]:
        break

qnt = int(input('Digite a quantidade vendida: '))

def calcular(num, qnt):
    return num * qnt

if tipo == 1:
    total = calcular(2.5, qnt)
elif tipo == 2:
    total = calcular(2.6, qnt)
else:
    total = calcular(2.75, qnt)


print(f'\nPicolé do tipo {tipo}.\nQuantidade vendida: {qnt}\nTotal arrecadado: R${total: .2f}\n')


