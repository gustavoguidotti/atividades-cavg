def formatarValor(valor, casasDecimais):
    return f'{valor: .{casasDecimais}f}'.replace('.', ',')

''' 1. Escreva um algoritmo que imprima os números de 1(inclusive) a
10(inclusive) em ordem decrescente. '''

# i = 10
# while i > 0:
#     print(i)
#     i -= 1

''' ------------------------------------------------------------------------
2. Escreva um algoritmo que imprima os números os números menores que
100, de 10 em 10. '''

# i = 0
# while i < 100:
#     print(i)
#     i += 10

''' ------------------------------------------------------------------------
3. Escreva um algoritmo para imprimir 10 números pares que sejam
menores que 20. '''

# i = 0
# while i < 20:
#     print(i)
#     i += 2

''' ------------------------------------------------------------------------
4. Escreva um algoritmo para imprimir a tabuada do 4 (1 a 10). '''

# i = 1
# while i < 11:
#     print(f'4 x {i}: {4 * i}')
#     i += 1

''' ------------------------------------------------------------------------
5. Escreva um algoritmo para ler 10 valores, calcular e escrever a média
aritmética desses valores. '''

# i = 0
# sum = 0
# while i < 10:
#     value = int(input(f'Digite o valor para {i + 1}: '))
#     sum += value
#     i += 1

# avg = sum / i
# print(f'A media dos {i} valores é {avg}')

''' ------------------------------------------------------------------------
6) Fazer um algoritmo para ler 2 valores e imprimir o resultado da divisão do primeiro 
pelo segundo. Se o segundo valor informado for ZERO, deve ser lido um novo valor 
até que o valor informado seja válido. '''

# dividendo = int(input('Digite o valor do dividendo: '))
# divisor = 0

# while divisor == 0:
#     divisor = int(input('Digite o valor do divisor (diferente de zero): '))

# resultado = dividendo / divisor
# print(f'O valor da divisao de {dividendo} por {divisor} é igual a {formatarValor(resultado, 2)}')

''' ------------------------------------------------------------------------
7) Fazer um algoritmo para ler 10 valores informados pelo usuário, deve ser mostrado 
qual o menor valor informado. '''

# valorUsuario = int(input('Digite o 1° número: '))
# menorValor = valorUsuario
# i = 0
# while i < 10:
#     if i > 0:
#         valorUsuario = int(input(f'Digite o {i + 1}° número: '))
#     menorValor = valorUsuario if valorUsuario < menorValor else menorValor
#     i += 1

# print(f'Menor valor: {menorValor}')

''' ------------------------------------------------------------------------
8) Modifique o exercício anterior para mostrar o maior valor. '''

# valorUsuario = int(input('Digite o 1° número: '))
# maiorValor = valorUsuario
# i = 0
# while i < 10:
#     if i > 0:
#         valorUsuario = int(input(f'Digite o {i + 1}° número: '))
#     maiorValor = valorUsuario if valorUsuario > maiorValor else maiorValor
#     i += 1

# print(f'Maior valor: {maiorValor}')

''' ------------------------------------------------------------------------
9) Faça um algoritmo para ler base e altura de 50 triângulos e escreva a sua área. '''

# i = 0
# while i < 50:
#     base = float(input(f'Digite o valor da base do {i + 1}° triângulo: '))
#     altura = float(input(f'Digite o valor da altura do {i + 1}° triângulo: '))

#     area = (base * altura) / 2
#     print(f'Área do {i + 1}° triângulo: {area}\n')
#     i += 1

''' ------------------------------------------------------------------------
10) Faça um algoritmo que calcule a hipotenusa de 10 triângulos.

OBS.: Considere que não devem ser permitidos valores negativos e nulos (zero) 
para o cálculo da fórmula.
hipotenusa2  = cateto2 +  cateto2 '''

# i = 0
# while i < 10:
#     while True:
#         cateto1 = float(input(f'Digite o valor do 1° cateto do {i + 1}° triângulo (maior que zero): '))
#         if cateto1 > 0: break
#     while True:
#         cateto2 = float(input(f'Digite o valor do 2° cateto do {i + 1}° triângulo (maior que zero): '))
#         if cateto2 > 0: break

#     hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
#     print(f'Hipotenusa do {i + 1}° triangulo: {formatarValor(hipotenusa, 3)}\n')
#     i += 1

''' ------------------------------------------------------------------------
11) Faça um algoritmo para ler um número indeterminado de dados, contendo a idade 
de uma pessoa. O último dado que não entrará nos cálculos, contém o valor de idade 
igual a ZERO. Calcular e imprimir a idade média deste grupo de indivíduos. '''

# qntPessoas = 0
# idadeSomada = 0
# idade = int(input(f'\n---DIGITE 0 PARA SAIR---\nDigite a idade da {qntPessoas + 1}ª pessoa: '))

# while idade > 0:
#     if qntPessoas > 0:
#         idade = int(input(f'\n---DIGITE 0 PARA SAIR---\nDigite a idade da {qntPessoas + 1}ª pessoa: '))
#     if idade > 0:
#         idadeSomada += idade
#         qntPessoas += 1

# if qntPessoas > 0:
#     media = idadeSomada / qntPessoas
#     print(f'A média de idade desse grupo de {qntPessoas} pessoas é{formatarValor(media, 2)}')

''' ------------------------------------------------------------------------
12) Uma empresa com X funcionários precisa saber a média de seus salários. Faça um 
algoritmo para ler a quantidade de funcionários e o salário de cada um e escrever a 
média dos salários. '''

# i = 0
# somaSalarios = 0
# qntFuncionarios = int(input('Digite a quantidade de funcionários da empresa: '))

# while i < qntFuncionarios:
#     somaSalarios += float(input(f'Digite o salário do {i + 1}° funcionário: '))
#     i += 1

# mediaSalarios = somaSalarios / qntFuncionarios

# print(f'Média salarial dos {qntFuncionarios} funcionários: R${formatarValor(mediaSalarios, 2)}')

''' ------------------------------------------------------------------------
13) Escreva um algoritmo para ler um número indeterminado de dados, contendo cada 
um o peso de um indivídio. O último dado que não entrará nos cálculos, contém um 
valor negativo. Calcular e imprimir: 
• A média aritmética das pessoas que possuem mais de 60 kg. 
• O peso do mais pesado entre aqueles que possuem menos de 60 kg. '''

# numPessoas = 0
# pesoSomado = 0
# maiorPeso = 0
# i = 1
# pesoInformado = float(input(f'\n---DIGITE QUALQUER VALOR NEGATIVO PARA SAIR---\nDigite o peso da {i}ª pessoa: '))

# while pesoInformado > 0:
#     if i > 1:
#         pesoInformado = float(input(f'\n---DIGITE QUALQUER VALOR NEGATIVO PARA SAIR---\nDigite o peso da {i}ª pessoa: '))
#     i += 1
#     if pesoInformado >= 60:
#         pesoSomado += pesoInformado
#         numPessoas += 1
#     else:
#         maiorPeso = pesoInformado if pesoInformado > maiorPeso else maiorPeso

# if numPessoas > 0:
#     media = pesoSomado / numPessoas
#     print(f'Media de peso das {numPessoas} pessoas que possuem mais de 60kg: {formatarValor(media, 2)}')
# if maiorPeso > 0:
#     print(f'Peso do mais pesado entre aqueles que possuem menos de 60 kg: {formatarValor(maiorPeso, 2)}')


''' ------------------------------------------------------------------------
14) Uma farmácia está levantando o valor total de todas as mercadorias em estoque. 
Escreva um algoritmo que permita a entrada das seguintes informações:  
a) o número total de mercadorias no estoque;  
b) o valor de cada mercadoria.  
c) Ao final imprimir a média de valor das mercadorias. 
OBS.: Ao ler o valor de cada mercadoria, deve-se ter a opção de perguntar “Deseja 
continuar (S/N)?”, para decidir se o programa irá continuar ou não '''

# ttlMerc = int(input('Digite o número total de mercadorias no estoque: '))
# somaTtlMerc = 0
# continuar = 'S'

# i = 0
# while continuar == 'S' and i < ttlMerc:
#     somaTtlMerc += float(input(f'Digite o valor da {i + 1}ª mecadoria: '))
#     i += 1
#     if i != ttlMerc:
#         continuar = input('Deseja continuar (S/N)? ')
#         while continuar not in ('S', 'N'):
#             continuar = input('Deseja continuar (S/N)? ')

# if somaTtlMerc > 0 and i == ttlMerc:
#     mediaVlrMerc = somaTtlMerc / ttlMerc
#     print(f'\nMédia de valor das {ttlMerc} mercadorias: R${formatarValor(mediaVlrMerc, 2)}')
# else:
#     print('\nO programa foi finalizado prematuramente. Nenhum cálculo foi feito.')