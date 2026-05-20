# GUSTAVO GUIDOTTI


''' 
1) Bolsa de estudo
Um aluno receberá bolsa se atender a uma das condições:
• tiver média maior ou igual a 8 e frequência maior ou igual a 75%;
ou
• for cotista e tiver média maior ou igual a 7 e frequência maior ou igual a 75%. '''

# media = float(input("Digite a média: "))
# frequencia = float(input("Digite a frequência: "))
# cotista = input("É cotista? (s/n): ")
# # if media >= 8 and frequencia >= 75 or cotista == "s" and media >= 7<<<<<<<:
# if media >= 8 and frequencia >= 75 or cotista == "s" and media >= 7 and frequencia >= 75:
#     print("Recebe bolsa")
# else:
#     print("Não recebe bolsa")
''' 1) O aluno cotista estava recebendo bolsa mesmo com uma frequencia menor que 75. '''
    

''' 
2) Acesso ao laboratório de química
O estudante poderá entrar se:
• estiver de jaleco e com óculos de proteção;
e além disso,
• não estiver usando sandália. '''

# jaleco = input("Está de jaleco? (s/n): ")
# oculos = input("Está com óculos? (s/n): ")
# sandalia = input("Está usando sandália? (s/n): ")
# # if jaleco == "s" and oculos == "s" >>>or<<< sandalia == "n":
# if jaleco == "s" and oculos == "s" and sandalia == "n":
#     print("Entrada permitida")
# else:
#     print("Entrada negada")
''' 2)  O acesso estava sendo liberado se o estudande estivesse usando oculos OU se o estudante nao estivesse usando sandalia.'''


''' 
3) Classificação de faixa etária para competição
Regras:
• Infantil: 10 a 13 anos
• Juvenil: 14 a 17 anos
• Adulto: 18 a 39 anos
• Master: 40 anos ou mais 
idade = int(input("Digite a idade: "))
if idade >= 10 or idade <= 13:
print("Infantil")
elif idade >= 14 or idade <= 17:
print("Juvenil")
elif idade >= 18 or idade <= 39:
print("Adulto")
else:
print("Master")'''

# idade = int(input("Digite a idade: "))
# if idade >= 10 and idade <= 13:
#     print("Infantil")
# elif idade >= 14 and idade <= 17:
#     print("Juvenil")
# elif idade >= 18 and idade <= 39:
#     print("Adulto")
# elif idade >= 39:
#     print("Master")
# else:
#     print('Sem permissao para competir.')
    
''' 3) O operador logico 'and' deve ser usado para testar o 'range', apenas trocar o 'or' pelo 'and' em todos os blocos. 
Alem disso, se o usuario esta no range de 1 a 9, entra em faixa etaria master.'''


''' 
4) Aprovação com exame
Regras:
• aprovado direto: média >= 7 e frequência >= 75
• exame: média entre 4 e 6.9 e frequência >= 75
• reprovado: demais casos
media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequência: "))
if media >= 7 and frequencia >= 75:
print("Aprovado")
elif media >= 4 or media < 7 and frequencia >= 75:
print("Exame")
else:
print("Reprovado") '''

# media = float(input("Digite a média: "))
# frequencia = float(input("Digite a frequência: "))
# if media >= 7 and frequencia >= 75:
#     print("Aprovado")
# # elif media >= 4 >>>or<<< media < 7 and frequencia >= 75:
# elif media >= 4 and media < 7 and frequencia >= 75:
#     print("Exame")
# else:
#     print("Reprovado")

''' 4) O aluno com frequencia maior que 75 estava indo para exame, mesmo com uma media menor que 4.
Trocar do 'or' por 'and' no bloco elif do exame resolve o problema. '''

'''
5) Login administrativo
O acesso administrativo só deve ser liberado se:
• o usuário for "admin"
• a senha for "1234"
• e o código de segurança for "999"
usuario = input("Usuário: ")
senha = input("Senha: ")
codigo = input("Código de segurança: ")
if usuario == "admin" and senha == "1234" or codigo == "999":
print("Acesso administrativo liberado")
else:
print("Acesso negado")'''

# usuario = input("Usuário: ")
# senha = input("Senha: ")
# codigo = input("Código de segurança: ")
# # if usuario == "admin" and senha == "1234" >>>or<<< codigo == "999":
# if usuario == "admin" and senha == "1234" and codigo == "999":

#     print("Acesso administrativo liberado")
# else:
#     print("Acesso negado")

''' 5)  O login administrativo estava sendo liberado se a senha fosse '1234' OU o codigo fosse '999' '''


''' 
6) Validação de desconto progressivo
Regras:
• desconto de 20%: cliente premium e compra acima de 500
• desconto de 10%: cliente comum e compra acima de 500
• desconto de 5%: cliente premium e compra entre 300 e 500
• sem desconto: demais casos
tipo = input("Tipo de cliente (premium/comum): ")
valor = float(input("Valor da compra: "))
if tipo == "premium" and valor > 500:
    print("20% de desconto")
elif tipo == "comum" and valor > 500:
    print("10% de desconto")
elif tipo == "premium" and valor >= 300 or valor <= 500:
    print("5% de desconto")
else:
    print("Sem desconto") '''

# tipo = input("Tipo de cliente (premium/comum): ")
# valor = float(input("Valor da compra: "))
# if tipo == "premium" and valor > 500:
#     print("20% de desconto")
# elif tipo == "comum" and valor > 500:
#     print("10% de desconto")
# elif tipo == "premium" and valor >= 300 and valor <= 500:
#     print("5% de desconto")
# else:
#     print("Sem desconto")

"""  6) Clientes premium estavam recebendo 5% de desconto em qualquer valor, pois o valor não estava entre 300 e 500. """

""" 7) Triagem médica
Encaminhar para atendimento prioritário se:
• tiver febre e falta de ar;
ou
• tiver idade maior ou igual a 65 e dor no peito.
febre = input("Febre? (s/n): ")
falta_ar = input("Falta de ar? (s/n): ")
idade = int(input("Idade: "))
dor_peito = input("Dor no peito? (s/n): ")
if febre == "s" and falta_ar == "s" or idade >= 65 and dor_peito == "s":
    print("Atendimento prioritário")
else:
    print("Atendimento normal") """

# febre = input("Febre? (s/n): ").lower()
# falta_ar = input("Falta de ar? (s/n): ").lower()
# idade = int(input("Idade: "))
# dor_peito = input("Dor no peito? (s/n): ").lower()
# if febre == "s" and falta_ar == "s" or idade >= 65 and dor_peito == "s":
#     print("Atendimento prioritário")
# else:
#     print("Atendimento normal")

""" 7) Tudo certo nesse """

""" 8) Sistema de empréstimo da biblioteca
O aluno pode pegar livro emprestado se:
• não estiver suspenso;
• e tiver menos de 3 livros atrasados;
• e for aluno ativo.
suspenso = input("Está suspenso? (s/n): ")
atrasados = int(input("Quantos livros atrasados possui? "))
ativo = input("É aluno ativo? (s/n): ")
if not suspenso == "s" and atrasados < 3 or ativo == "s":
 print("Empréstimo autorizado")
else:
 print("Empréstimo negado")"""


# suspenso = input("Está suspenso? (s/n): ").lower()
# atrasados = int(input("Quantos livros atrasados possui? "))
# ativo = input("É aluno ativo? (s/n): ").lower()
# # if not suspenso == "s" and atrasados < 3 or ativo == "s":
# if not suspenso == "s" and atrasados < 3 and ativo == "s":
#     print("Empréstimo autorizado")
# else:
#     print("Empréstimo negado")
""" 8) Se o aluno fosse ativo, estava sendo autorizado a pegar livros, mesmo com 3 ou mais livros atrasados. 
Alem disso, se o aluno tivesse menos de 3 livros atrasados, conseguia pegar livros, mesmo não estando ativo.
Trocar o 'or' por 'and' na linha 202 resolveu o problema."""

""" 9) Elegibilidade para estágio
Pode concorrer ao estágio se:
• estiver no 2º, 3º ou 4º ano;
• tiver idade mínima de 16 anos;
• e não estiver em dependência em mais de 2 disciplinas.
ano = int(input("Ano escolar: "))
idade = int(input("Idade: "))
dependencias = int(input("Número de dependências: "))
if ano >= 2 and ano <= 4 and idade >= 16 and not dependencias >
2:
 print("Pode concorrer ao estágio")
else:
 print("Não pode concorrer ao estágio") """

# ano = int(input("Ano escolar: "))
# idade = int(input("Idade: "))
# dependencias = int(input("Número de dependências: "))
# if ano in (2,3,4) and idade >= 16 and not dependencias > 2:
#     print("Pode concorrer ao estágio")
# else:
#     print("Não pode concorrer ao estágio")
""" 9) Tudo certo nesse """

""" 10) Verificação de promoção em curso online
O aluno ganha certificado com destaque se:
• tiver nota final maior ou igual a 9
• e participação maior ou igual a 80%
• ou for monitor do curso, desde que também tenha participação maior ou igual a
80%.
nota = float(input("Nota final: "))
participacao = float(input("Participação (%): "))
monitor = input("É monitor? (s/n): ")
if nota >= 9 and participacao >= 80 or monitor == "s":
 print("Certificado com destaque")
else:
 print("Certificado comum")
 """

nota = float(input("Nota final: "))
participacao = float(input("Participação (%): "))
monitor = input("É monitor? (s/n): ")
if nota >= 9 and participacao >= 80 or monitor == "s" and participacao >= 80:
 print("Certificado com destaque")
else:
 print("Certificado comum")
""" 10) O aluno estava recebendo certificado com destaque apenas sendo monitor de curso, independente da sua participação. """
