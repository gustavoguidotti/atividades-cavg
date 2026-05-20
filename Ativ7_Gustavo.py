# Gustavo Guidotti 

''' 
6) Crie um algoritmo que leia a idade da pessoa e se ela tem carteirinha de idoso (s para
sim ou n para não).
A entrada no parque é gratuita se a pessoa tiver menos de 10 anos ou tiver a
carteirinha de idoso. O algoritmo deve mostrar as mensagens:
• “Entrada gratuita” ou
• “Precisa pagar ingresso”. '''

# idade = int(input('Digite sua idade: '))
# temCarteirinha = 'n'
# if idade >= 60:
#     temCarteirinha = input('Voce tem carteirinha de idoso (s/n): ').lower()

# if idade < 10 or temCarteirinha == 's':
#     print('Entrada gratuita.')
# else:
#     print('Precisa pagar ingresso.')


# ----------------------------------------------------------------------------------------------------
''' 
7) Crie um algoritmo que leia a idade da pessoa e se ela possui carteira de motorista (s
para sim ou n para não).
A pessoa só pode dirigir se tiver 18 anos ou mais e tiver carteira de motorista. O
algoritmo deve mostrar as mensagens:
• “Pode dirigir” ou
• “Não pode dirigir”. '''

# idade = int(input('Digite sua idade: '))
# temCNH = input('Voce tem carteira de motorista? (s/n) ').lower()

# if idade >= 18 and temCNH == 's':
#     print('Pode dirigir.')
# else:
#     print('Não pode dirigir.')


# ----------------------------------------------------------------------------------------------------
''' 
8) Elabore um algoritmo que peça ao usuário três notas e a frequência (em %).
➔ O aluno só será aprovado se:
• A média for maior ou igual a 6 e
• A frequência for maior ou igual a 75.
➔ Caso não seja aprovado, mostre uma mensagem específica:
• Se a média for menor que 6, diga "Reprovado por nota".
• Se a frequência for menor que 75%, diga "Reprovado por falta".
• Se ambos forem insuficientes, diga "Reprovado por nota e falta". '''


# nota1 = float(input('Digite a nota 1: '))
# nota2 = float(input('Digite a nota 2: '))
# nota3 = float(input('Digite a nota 3: '))

    
# frequencia = float(input('Digite a frequência (em %) do aluno (apenas numeros): '))

# media = (nota1 + nota2 + nota3) / 3

# if (10 >= media >= 6 and media > 0) and (100 >= frequencia >= 75 and frequencia > 0):
#     print(f'Aprovado com uma média de{media: .2f} e frequência de{frequencia: .2f}%.')
# elif media < 6 and frequencia < 75:
#     print(f'Reprovado com uma média de{media: .2f} e frequência de{frequencia: .2f}%.')
# elif media < 6:
#     print(f'Reprovado por média:{media: .2f}.')
# elif frequencia < 75:
#     print(f'Reprovado por falta, com uma frequência de{frequencia: .2f}%.')
# else:
#     print('Erro ao calcular, por favor tente novamente.')
    

# ----------------------------------------------------------------------------------------------------
''' 
9) Dado três valores, A, B e C, construa um algoritmo para verificar se estes valores
formam um triangulo escaleno, equilátero ou isósceles.
Equilátero > Todos os lados iguais.
Isósceles > Dois lados iguais.
Escaleno > Todos os lados diferentes. '''

# A = float(input('Digite para o lado A do triangulo: '))
# B = float(input('Digite para o lado B do triangulo: '))
# C = float(input('Digite para o lado C do triangulo: '))

''' 1 ---------------- '''
# if A == B == C:
#     print('Triangulo Equilátero.')
# elif A != B != C:
#     print('Triangulo Escaleno.')
# else:
#     print('Triangulo Isósceles')


''' 2 ---------------- '''
# if A == B and B == C:
#     print('Triangulo Equilátero.')
# elif (A == B or A == C or B == C) and (A != B or A != C or B != C):
#     print('Triangulo Isósceles')
# elif not A == B and not B == C and not A == C:
#     print('Triangulo Escaleno.')


''' 3 ---------------- '''
# if A == B and B == C:
#     print('Triangulo Equilátero.')
# elif A != B and A != C and B != C:
#     print('Triangulo Escaleno.')
# else:
#     print('Triangulo Isósceles')



# ----------------------------------------------------------------------------------------------------
''' 
10) Crie um algoritmo que leia a idade de uma pessoa e informe a sua classe eleitoral:
• não eleitor (abaixo de 16 anos).
• eleitor obrigatório (entre a faixa de 18 e menor de 65 anos).
• eleitor facultativo (de 16 até 18 anos e maior de 65 anos, inclusive) '''

idade = int(input('Digite sua idade: '))


''' 1 ---------------- '''
# if idade < 16:
#     print('Não eleitor.')
# elif idade >= 18 and idade < 65:
#     print('Eleitor obrigatório.')
# else:
#     print('Eleitor facultativo.')


if (idade >= 16 and idade < 18) or idade >= 65:
    print('Eleitor facultativo.')
elif idade < 16:
    print('Não eleitor.')
else:
    print('Eleitor obrigatório.')


