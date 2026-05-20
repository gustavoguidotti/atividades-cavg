def formatarValor(valor):
    return f'{valor: .2f}'.replace('.', ',')

""" 1) Escreva um algoritmo que imprima os números de 1(inclusive) a 10(inclusive) em
ordem decrescente. """

# num = 10
# while True:
#     print(num)
#     num -= 1
#     if num < 1 : break


""" ----------------------------------------------------------------------------------
2) Escreva um algoritmo que imprima os números os números menores que 100, de
10 em 10. """

# num = 0
# while True:
#     print(num)
#     num += 10
#     if num > 99: break

""" ----------------------------------------------------------------------------------
3) Escreva um algoritmo para imprimir 10 números pares que sejam menores que 20. """

# num = 0
# while True:
#     print(num)
#     num += 2
#     if num >= 20: break

""" ----------------------------------------------------------------------------------
4) Escreva um algoritmo para imprimir a tabuada do 4 (1 a 10). """

# num = 1
# while True:
#     print(f'4 x {num} = {num * 4}')
#     num += 1
#     if num > 10: break

""" ----------------------------------------------------------------------------------
5) Escreva um algoritmo para ler 10 valores, calcular e escrever a média aritmética
desses valores. """

# num = 1
# somaValores = 0
# while True:
#     somaValores += float(input(f'Digite o {num}º valor: '))
#     if num >=10: break
#     num += 1

# mediaValores = somaValores / num
# print(f'Media dos {num} valores:{formatarValor(mediaValores)}')

""" ----------------------------------------------------------------------------------
6) Fazer um algoritmo para ler 2 valores e imprimir o resultado da divisão do primeiro
pelo segundo. Se o segundo valor informado for ZERO, deve ser lido um novo valor
até que o valor informado seja válido. """

# dividendo = float(input('Digite o valor do dividendo: '))

# while True:
#     divisor = float(input('Digite o valor do divisor (diferente de zero): '))
#     if divisor != 0: break

# resultado = dividendo / divisor
# print(f'{formatarValor(dividendo)} /{formatarValor(divisor)} = {formatarValor(resultado)}')

""" ----------------------------------------------------------------------------------
7) Fazer um algoritmo para ler 10 valores informados pelo usuário, deve ser mostrado
qual o menor valor informado. """

# i = 0
# valorInformado = float(input(f'Digite o {i + 1}º valor: '))
# menorValor = valorInformado

# while True:
#     valorInformado = float(input(f'Digite o {i + 1}º valor: '))
#     menorValor = valorInformado if valorInformado < menorValor else menorValor
#     i += 1
#     if i == 10: break

# print(f'Menor valor informado: {formatarValor(menorValor)}')

""" ----------------------------------------------------------------------------------
8) Modifique o exercício anterior para mostrar o maior valor. """

# i = 0
# while True:
#     valorInformado = float(input(f'Digite o {i + 1}º valor: '))
#     if i > 0:
#         maiorValor = valorInformado if valorInformado > maiorValor else maiorValor
#     else:
#         maiorValor = valorInformado
#     i += 1
#     if i == 10: break

# print(f'Maior valor informado: {maiorValor}')

""" ----------------------------------------------------------------------------------
9) Faça um algoritmo para ler base e altura de 50 triângulos e escreva a sua área. """

# i = 0
# while True:
#     base = float(input(f'Digite o valor da base do {i + 1}º triângulo: '))
#     altura = float(input(f'Digite o valor da altura do {i + 1}º triângulo: '))
#     area = (base * altura) / 2
#     print(f'Area do {i + 1}º triângulo: {formatarValor(area)}')
#     i += 1
#     if i == 50: break

""" ----------------------------------------------------------------------------------
10) Faça um algoritmo que calcule a hipotenusa de 10 triângulos.
OBS.: Considere que não devem ser permitidos valores negativos e nulos (zero)
para o cálculo da fórmula.
hipotenusa2 = cateto2 + cateto2 """

# i = 0
# while i < 10:
#     while True:
#         cateto1 = float(input(f'Digite o valor do cateto 1 do {i + 1}º triângulo: '))
#         if cateto1 > 0: break
#     while True:
#         cateto2 = float(input(f'Digite o valor do cateto 2 do {i + 1}º triângulo: '))
#         if cateto2 > 0: break
#     hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
#     print(f'\nHipotenusa do {i + 1}º triângulo:{formatarValor(hipotenusa)}\n\n')
#     i += 1