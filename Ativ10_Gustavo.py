''' 
1) Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da
compra for menor que R$20,00; caso contrário, o lucro será de 30%. Entrar com o valor do
produto e imprimir o valor da venda. '''

# valor_da_compra = float(input('Valor da compra do produto: '))

# if valor_da_compra < 20:
#     valor_de_venda = (valor_da_compra * 1.45)
# else:
#     valor_de_venda = valor_da_compra * 1.3

# print(f'Voce comprou o produto por R${valor_da_compra: .2f}\nO valor de venda deve ser R${valor_de_venda: .2f}')


''' -------------------------------------------------------------------------------------------------------------
2) Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo
é Acutângulo, Retângulo ou Obtusângulo. Sendo que:
− Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
− Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90º)
− Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º) '''


# while True:
#     angulo1 = float(input('Valor angulo 1: '))
#     angulo2 = float(input('Valor angulo 2: '))
#     angulo3 = float(input('Valor angulo 3: '))
#     soma = angulo1 + angulo2 + angulo3
#     if soma == 180:
#         break
#     print('Entrada invalida: não é um triangulo.')

# def maior_angulo(ang1, ang2, ang3):
#     if ang2 < ang1 > ang3:
#         return ang1
#     elif ang1 < ang2 > ang3:
#         return ang2
#     elif ang1 < ang3 > ang2:
#         return ang3
    
# m_ang = maior_angulo(angulo1, angulo2, angulo3)

# if m_ang == 90:
#     print('Triângulo Retângulo.')
# elif m_ang > 90:
#     print('Triângulo Obtusângulo.')
# else:
#     print('Triângulo Acutângulo.')


''' -------------------------------------------------------------------------------------------------------------
3) Um endocrinologista deseja controlar a saúde de seus pacientes e, para isso, se utiliza do
índice de Massa Corporal (IMC). Sabendo-se que o IMC é calculado através da seguinte
formula:
    IMC = peso/altura^2
Onde: peso é dado em kg e altura em metros. '''

# nome = input('Digite seu nome: ')
# altura = float(input('Digite sua altura: '))
# peso = float(input('Digite seu peso: '))
# imc = float(f'{peso/altura**2: .2f}')

# if imc < 20:
#     msg = 'Abaixo do peso.'
# elif 20 <= imc <= 25:
#     msg = 'Normal.'
# elif 25 < imc <= 30:
#     msg = 'Excesso de peso.'
# elif 30 < imc <= 35:
#     msg = 'Obesidade.'
# else:
#     msg = 'Obesidade mórbida.'


# print(f'\n{nome.capitalize()}, seu IMC é {imc}: {msg}')


''' -------------------------------------------------------------------------------------------------------------
4) Faça um algoritmo que escreva nome, categoria e salário reajustado de cada empregado.
A empresa irá dar um aumento de salário aos seus funcionários de acordo com a categoria de
cada empregado. O aumento seguirá a seguinte regra:
• Funcionários das categorias A, C, F, e H ganharão 10% de aumento sobre o salário;
• Funcionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre o salário;
• Funcionários das categorias K e R ganharão 25% de aumento sobre o salário;
• Funcionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento sobre o
salário;
• Funcionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento sobre o
salário. '''

# nome = input('Digite seu nome: ').capitalize()
# salario = float(input('Digite seu salario atual: '))

# while True:
#     categoria = input('Digite sua categoria: ').upper()
#     match categoria:
#         case 'A' | 'C'| 'F' | 'H':
#             salario_reajustado = salario * 1.10
#         case 'B' | 'D'| 'E' | 'I' | 'J' | 'T':
#             salario_reajustado = salario * 1.15
#         case 'K' | 'R':
#             salario_reajustado = salario * 1.25
#         case 'L' | 'M'| 'N' | 'P' | 'Q' | 'S':
#             salario_reajustado = salario * 1.35
#         case 'U' | 'V'| 'X' | 'Y' | 'W' | 'Z':
#             salario_reajustado = salario * 1.5
#     if 'salario_reajustado' in globals(): break
#     if not 'salario_reajustado' in globals(): print('\nCategoria invalida, tente novamente.')

# reajuste = salario_reajustado - salario

# print(f'\nAumento de {reajuste * 100 / salario: ,.2f}% e R${reajuste: ,.2f}.')
# print(f'{nome}, seu salário atual é R${salario: ,.2f}, com base na sua categoria ({categoria}) seu salário será reajustado para R${salario_reajustado: ,.2f}.')


''' -------------------------------------------------------------------------------------------------------------
5) Faça um algoritmo que leia três valores para as variáveis A, B, C e dependendo da opção
escolhida no menu, faça as seguintes operações:
Opção 1: Calcule: (A + B)*C2;
Opção 2: Mostrar o maior valor;
Opção 3: Mostra o menor valor;
Opção 4: Mostre o quadrado dos 3 números;
Opção 5: Inverta os valores de A e C;'''

# # User inputs
# a = float(input('Digite o valor para A: '))
# b = float(input('Digite o valor para B: '))
# c = float(input('Digite o valor para C: '))
# while True:
#     opcao = int(input("\nOpção 1: Calcule: (A + B)*C2.\nOpção 2: Mostrar o maior valor.\nOpção 3: Mostra o menor valor.\nOpção 4: Mostre o quadrado dos 3 números.\nOpção 5: Inverta os valores de A e C. \n"))
#     if opcao in (1, 2, 3, 4, 5): break
#     print('Entrada invalida: digite um numero de 1 a 5.')

# # Helper functions
# def maior_valor (a, b, c):
#     if b <= a >= c:
#         return f'A = {a}'
#     elif a <= b >= c:
#         return f'B = {b}'
#     elif a <= c >= b:
#         return f'C = {c}'
    
# def menor_valor (a, b, c):
#     if b >= a <= c:
#         return f'A = {a}'
#     elif a >= b <= c:
#         return f'B = {b}'
#     elif a >= c <= b:
#         return f'C = {c}'

# def inv_A_e_C (a, b, c):
#     temp = a
#     a = c
#     c = temp
#     return f'A = {a}, B = {b}, C = {c}'

# # Match case  
# match opcao:
#     case 1:
#         resultado = (a + b) * c ** 2
#     case 2:
#         resultado = maior_valor(a, b, c)
#     case 3:
#         resultado = menor_valor(a, b, c)
#     case 4:
#         resultado = f'A = {a ** 2}, B = {b ** 2}, C = {c ** 2}'
#     case 5:
#         resultado = inv_A_e_C(a, b, c)

# print(resultado)


