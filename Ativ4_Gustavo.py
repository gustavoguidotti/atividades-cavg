# 1) Calcular o dobro de um numero.

# n = int(input('Digite um número: '))
# n*=2
# print(n)

# ---------------------------------------------------------------------------------------------------------
# 2) Calcular a seguinte expressão: (a+b) * (c+d).

# a = float(input('Digite um valor para A: '))
# b = float(input('Digite um valor para B: '))
# c = float(input('Digite um valor para C: '))
# d = float(input('Digite um valor para D: '))

# expressao = (a + b) * (c + d)

# print(expressao)

# ---------------------------------------------------------------------------------------------------------
# 3) Ler um número inteiro e escrever o seu antecessor e o seu sucessor.

# num = int(input('Digite um número: '))

# numAntecessor = num - 1
# numSucessor = num + 1

# print(f'O antecessor do número {num} é {numAntecessor} e o sucessor é {numSucessor}')

# ---------------------------------------------------------------------------------------------------------
# 4) Ler o raio de um círculo, calcular e escrever a sua área, sabendo-se que: Área = π * raio².

# raio = float(input('Digite o valor do raio: '))

# area = 3.141592653589793 * (raio ** 2)

# print(f'A área do circulo é: {area: .2f}')

# ---------------------------------------------------------------------------------------------------------
# 5) Calcular e mostrar a área de um trapézio, sabendo-se: Área = ((base maior + base menor)* altura)/2.

# baseMaior = float(input('Digite o valor da base maior do trapézio: '))
# baseMenor = float(input('Digite o valor da base menor do trapézio: '))
# altura = float(input('Digite a altura do trapézio: '))

# area = ((baseMaior + baseMenor) * altura) / 2

# print(f'A área do trapezio é: {area: .2f}')

# ---------------------------------------------------------------------------------------------------------
# 6) Uma loja de peças automotivas precisa automatizar seu controle de vendas de
# peças. Para isso devem ser solicitados o código, valor e quantidade de peças
# vendidas. Após, deve ser calculado o valor total que foi vendido das peças, que
# será calculado como:
# Valor total = quantidade * valor da peça
# Ao final deve ser mostrado o código da peça e o valor total.

# codigo = input('Digite o código do produto: ')
# valor = float(input('Digite o valor do produto: '))
# quantidade = int(input('Digite a quantidade de peças vendidas: '))

# total = quantidade * valor

# print(f'O valor total da peça de código {codigo} é: {total}')

# ---------------------------------------------------------------------------------------------------------
# 7) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e
# escrever o valor correspondente em graus Celsius

# tempF = float(input('Digite a temperatura em fahrenheit: '))
# tempC = ((tempF - 32) * 5) / 9
# print(f'{tempF} fahrenheit é igual a {tempC: .2f} celsius.')

# ---------------------------------------------------------------------------------------------------------
# 8) Desenvolva um programa que leia o peso (em kg) e a altura (em metros) de uma
# pessoa e calcule o Índice de Massa Corporal (IMC).

# peso = float(input('Digite o seu peso: '))
# altura = float(input('Digite a sua altura: '))
# imc = peso / (altura ** 2) 
# print(f'Seu  Índice de Massa Corporal é: {imc: .2f}')

# ---------------------------------------------------------------------------------------------------------
# 9) Crie um programa que leia a distância percorrida (em km) e o tempo gasto (em horas) e
# calcule a velocidade média.

# distancia = float(input('Digite a distância percorrida (em km): '))
# tempo = int(input('Digite o tempo gasto (em horas) para percorrer essa distância: '))
# velocidadeMedia = distancia / tempo
# print(f'A velocidade média foi {velocidadeMedia} km/h')

# ---------------------------------------------------------------------------------------------------------
# 10) Faça um algoritmo para uma pizzaria, o qual leia o valor total de uma conta e quantos
# clientes vão pagá-la. Calcule e informe o valor a ser pago por cliente.

# valorTotal = float(input('Digite o valor total da conta: '))
# numClientes = int(input('Digite a quantidade de clientes pagantes: '))
# valorPorCliente = valorTotal / numClientes
# print(f'Cada um dos {numClientes} clientes deve pagar R${valorPorCliente}.')

# ---------------------------------------------------------------------------------------------------------
# 11) Uma empresa contratou um plano de armazenamento em nuvem e precisa estimar
# quanto espaço está sendo utilizado. Sabe-se que foram enviados vários arquivos de
# mesmo tamanho para o servidor.
# Desenvolva um programa que permita calcular o espaço total ocupado e apresentar
# o resultado em gigabytes.
# (Considere que 1 GB equivale a 1024 MB.)

# qntdArquivos = int(input('Quantidade de arquivos: '))
# tamanhoArquivos = float(input('Tamanho de cada arquivo (em MB): '))
# totalEmMB = qntdArquivos * tamanhoArquivos
# totalEmGB = totalEmMB / 1024

# print(f'Espaço total utilizado: {totalEmMB} MB')
# print(f'Espaço total utilizado em GB: {totalEmGB: .2f} GB')

# ---------------------------------------------------------------------------------------------------------
# 12) Uma loja de roupas está realizando uma liquidação especial e oferecendo 20% de
# desconto para compras pagas à vista.
# Crie um programa que leia o valor total da compra e calcule quanto o cliente pagará
# caso opte pelo pagamento à vista, aplicando o desconto informado.

# valorCompra = float(input('Valor da compra: '))
# desconto = valorCompra * 0.2
# valorAVista = valorCompra - desconto

# print(f'Valor da compra: R${valorCompra: ,.2f}')
# print(f'Desconto (20%): R${desconto: ,.2f}')
# print(f'Valor à vista: R${valorAVista: ,.2f}')

# ---------------------------------------------------------------------------------------------------------
# 13) Faça um algoritmo para ler o salário de um funcionário e reajustá-lo com aumento
# de 15%. Após, desconte 8% de impostos. Imprima o salário inicial, o valor do
# reajuste, o valor dos impostos e o salário final.
salario = float(input('Salário: '))
reajuste = salario * 0.15
impostos = (salario + reajuste) * 0.08
salarioFinal = salario + reajuste - impostos

print(f'Salário: R${salario: ,.2f}')
print(f'Reajuste: R${reajuste: ,.2f}')
print(f'Impostos: R${impostos: ,.2f}')
print(f'Salário final: R${salarioFinal: ,.2f}')
