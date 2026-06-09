# 1)Escreva um algoritmo que armazene em um vetor e imprima os números de
# 1(inclusive) a 10(inclusive) em ordem decrescente, utilizando vetores.

""" numeros = []
for i in range(1, 11):
    numeros.append(i)
print(numeros) """

'''----------------------------------------------------------------------------------'''
# 2) Escreva um algoritmo que armazene em um vetor e imprima os 10 números
# pares que sejam menores que 20.

""" numeros = []
for i in range(20):
    if i % 2 == 0:
        numeros.append(i)
print(numeros) """

'''----------------------------------------------------------------------------------'''
# 3) Crie um programa que leia a altura de 5 pessoas e armazene em uma lista.

""" alturas = []
for i in range(5):
    usrInput = float(input(f'Digite a alturas da {i + 1}ª pessoa: '))
    alturas.append(usrInput)
print(alturas) """

'''----------------------------------------------------------------------------------'''
# 4) Crie um programa que leia 8 números inteiros e armazene em uma lista.
# Depois, mostre:
# •quantos números são positivos;
# •quantos números são negativos;
# •quantos números são iguais a zero.

""" numeros = []
pos = neg = zero = 0
for i in range(8):
    usrInput = int(input(f'Digite o {i + 1}º numero: '))
    numeros.append(usrInput)
    if usrInput > 0:
        pos += 1
    elif usrInput < 0:
        neg += 1
    else:
        zero += 1

print(f'Numeros positivo: {pos}\nNumeros negativos: {neg}\nNumeros iguais a zero: {zero}') """

        

'''----------------------------------------------------------------------------------'''
# 4) Escreva um algoritmo em que receba dez números do usuário e armazene
# em um vetor a metade de cada número. Após isso, o algoritmo deve imprimir
# todos os valores armazenados.

""" numeros = []
for i in range(10):
    userInput = float(input(f'Digite o {i + 1}º numero: '))
    numeros.append(userInput / 2)
print(f'Metade de cada numero digitado: {numeros}') """

'''----------------------------------------------------------------------------------'''
# 5) Escreva um algoritmo que armazene em um vetor todos os números
# múltiplos de 5, no intervalo fechado de 1 a 500. Após isso, o algoritmo deve
# imprimir todos os valores armazenados.

""" numeros = []
for i in range(1, 500):
    if i % 5 == 0:
        numeros.append(i)
print(numeros) """

'''----------------------------------------------------------------------------------'''
# 6) Crie um programa que leia a temperatura registrada durante 7 dias da
# semana.
# Depois, mostre:
# •todas as temperaturas;
# •a média da semana;
# •quantos dias tiveram temperatura acima da média.

""" def formValor(valor):
    return f'{valor: .2f}'.replace('.', ',')

diasDaSemana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']
temperaturas = []
totalTemperaturas = 0
tempsAcimaDaMedia = 0

for dia in diasDaSemana:
    temperatura = int(input(f'Digite a temperatura de {dia}: '))
    temperaturas.append(temperatura)
    totalTemperaturas += temperatura

mediaDeTemperaturas = totalTemperaturas / len(temperaturas)
for temp in temperaturas:
    if temp > mediaDeTemperaturas: tempsAcimaDaMedia += 1

print(end='\n\n')
for i in range(len(diasDaSemana)):
    print(f'{diasDaSemana[i].capitalize()}:{temperaturas[i]}')
print(f'\nMedia da semana: {formValor(mediaDeTemperaturas)}\nDias com temperatura acima da media: {tempsAcimaDaMedia}') """

'''----------------------------------------------------------------------------------'''
# 7) Crie um programa que leia 6 números inteiros e armazene em uma lista.
# Depois, mostre os números na ordem em que foram digitados e também na
# ordem inversa.
# → OBS.: Não utilizar a função reverse do Pyhton.

""" numeros = []
for i in range(6):
    numero = int(input(f'Digite o {i + 1}º numero: '))
    numeros.append(numero)

numerosOrdemInversa = []
for i in range(len(numeros), 0, -1):
    numerosOrdemInversa.append(i)

print(f'Numeros em ordem: {numeros}')
print(f'Numeros em ordem inversa: {numerosOrdemInversa}') """



'''----------------------------------------------------------------------------------'''
# 8) Crie um programa que tenha uma lista com alguns nomes de alunos.
# Depois, peça para o usuário digitar um nome e verifique se esse nome está na lista.

""" alunos = ['Ana Paula', 'Cristian', 'Eduardo', 'Gabriela', 'Gustavo', 'Helena', 'Jamil', 'Joao Victor', 'Nicole', 'Wellington']

userInput = input('Digite o nome do aluno: ').capitalize()
if userInput in alunos:
    print(f'{userInput} esta na lista.')
else:
    print(f'{userInput} nao esta na lista.') """
    