def formatValue(value):
    return f'{value: .2f}'.replace('.', ',')

""" # 1) Escreva um laço que calcule:
# a) A soma de todos os números pares entre 2 e 100 (inclusive).

sumA = 0
for i in range(101):
    if i % 2 == 0:
        sumA += i
print(sumA)

# ----------------------------------------------------------------------------------
# b) A soma de todos os quadrados entre 1 e 100 (inclusive).

sumB = 0
for i in range(1,101):
    sumB += i ** 2
print(sumB)

# ----------------------------------------------------------------------------------
# c) A soma de todos os números ímpares entre a e b.

sumC = 0
for i in range(sumA, sumB):
    if i % 2 == 1:
        sumC += i
print(sumC)

# ----------------------------------------------------------------------------------
# d) Todos os números positivos que são divisíveis por 10 e menores que 100.

for i in range(1, 100):
    if i % 10 == 0:
        print(i) """

# ----------------------------------------------------------------------------------
# 2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá
# calcular e mostrar :
# a. A menor altura do grupo
# b. A maior altura do grupo

""" userInput = float(input(f'Digite a altura da 1ª pessoa: '))
maxHeight = minHeight = userInput

for i in range(14):
    userInput = float(input(f'Digite a altura da {i + 2}ª pessoa: '))
    if userInput > maxHeight: maxHeight = userInput
    elif userInput < minHeight: minHeight = userInput
print(f'Menor altura do grupo:{formatValue(minHeight)}m.\nMaior altura do grupo:{formatValue(maxHeight)}m.') """
    

# ----------------------------------------------------------------------------------
# 3) Faça um algoritmo que leia uma quantidade não determinada de números positivos.
# Calcule a quantidade de números pares e ímpares, a média de valores pares e a
# média geral dos números lidos. O número que encerrará a leitura será zero.

nums = evenNums = oddNums = sumEvenNums = sumNums = 0
while True:
    while True:
        userInput = int(input('---Digite 0 para sair---\nDigite um numero positivo: '))
        if userInput >= 0: break

    if userInput % 2 == 0 and userInput != 0:
        nums += 1
        evenNums += 1
        sumEvenNums += userInput
        sumNums += userInput
    elif userInput != 0:
        nums += 1
        oddNums += 1
        sumNums += userInput

    if userInput == 0: break

avgNums = sumNums / nums
avgEvenNums = sumEvenNums / evenNums

print(f'Numeros pares: {evenNums}\nNumeros Impares: {oddNums}\nMedia numeros pares: {avgEvenNums}\nMedia de todos os numeros: {avgNums}')


# ----------------------------------------------------------------------------------
# 4) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

""" for i in range(100, 201):
    if i % 2 == 1:
        print(i) """

# ----------------------------------------------------------------------------------
# 5) Peça ao usuário um número inteiro não-negativo e, com um laço while ou for,
# calcule o seu fatorial (N!). Exemplo:
# • 1! = 1
# • 2! = 2 x 1 = 2
# • 3! = 3 x 2 x 1 = 6
# • 4! = 4 x 3 x 2 x 1 = 24
# • 5! = 5 x 4 x 3 x 2 x 1 = 120

""" while True:
    while True:
        num = int(input('\n----------Digite 0 para sair----------\nDigite um número inteiro não-negativo: '))
        if num >= 0: break
    if num == 0: break    

    if num == 1:
        print(f'{num}! = {num}')
    else:
        fact = num
        print(f'{num}! = {num} ', end='')
        for i in range(num - 1, 0, -1):
            fact*=i
            print(f'x {i} ', end='')
        print(f'= {fact}') """

# ----------------------------------------------------------------------------------
# 6) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que
# são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.

""" sum = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        sum += i
print(sum) """

# ----------------------------------------------------------------------------------
# 7) A loja TudoLimpo esta implementando um sistema para registrar a quantidade de
# produtos vendidos por tipo. Crie um algoritmo que:

""" typeA = typeB = typeC = 0

# a) Peca ao usuario que informe o tipo de produto (A, B ou C) e a quantidade vendida.
while True:
    while True:
        prodType = input('---Digite "X" para sair---\nDigite o tipo do produto (A, B, C): ').upper()
        if prodType in ('A', 'B', 'C', 'X'): break
# b) Valide que a quantidade seja maior que zero.
    if prodType == 'X': break
    while True:
        prodQty = int(input(f'Digite a quantidade vendida do produto de tipo {prodType}: '))
        if prodQty > 0: break
# c) Registre as quantidades em acumuladores diferentes para cada tipo.
    match prodType:
        case 'A':
            typeA += prodQty
        case 'B':
            typeB += prodQty
        case 'C':
            typeC += prodQty

# d) Apos uma entrada especifica (ex: tipo = 'X'), o programa deve ser encerrado e exibir:
# O total vendido de cada tipo de produto.
print(f'\n----------------------------------\nProduto do tipo A: {typeA}\nProduto do tipo B: {typeB}\nProduto do tipo C: {typeC}\n----------------------------------\n')
# O total geral de produtos vendidos.
total = typeA + typeB + typeC
print(f'Total de produtos vendidos: {total}\n----------------------------------') """
