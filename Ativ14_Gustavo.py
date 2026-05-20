def formValue(value):
    return f'{value: .2f}'.replace('.', ',')

""" 
1. Escreva um algoritmo que imprima os números de 1(inclusive) a 10(inclusive) em
ordem decrescente. """

# for i in range(10, 0, -1):
#     print(i)

""" -----------------------------------------------------------------------------------
2. Escreva um algoritmo que imprima os números os números menores que 100, de 10
em 10."""

# for i in range(90, -1, -10):
#     print(i)

""" -----------------------------------------------------------------------------------
3. Escreva um algoritmo para imprimir 10 números pares que sejam menores que 20. """

# for i in range(0, 20, 2):
#     print(i)

""" -----------------------------------------------------------------------------------
4. Escreva um algoritmo para imprimir a tabuada do 4 (1 a 10). """

# num = 4

# for i in range(1, 11):
#     print(f'{num} x {i} = {num * i}')

""" -----------------------------------------------------------------------------------
5. Escreva um algoritmo para ler 10 valores, calcular e escrever a média aritmética
desses valores. """

# sum = 0

# for i in range(1, 11):
#     sum += int(input(f'Digite o {i}º numero: '))
# avg = sum / i

# print(f'Media:{formValue(avg)}')

""" -----------------------------------------------------------------------------------
6. Ler o número de alunos de uma turma, ler as notas destes alunos e calcular a média
aritmética destes alunos. """

# qntAlunos = int(input('Digite o a quantidade de alunos da turma: '))
# somaNotas = 0

# for i in range(1, qntAlunos + 1):
#     somaNotas += float(input(f'Digite a nota do {i}º aluno: '))
# avg = somaNotas / qntAlunos

# print(f'Media das notas dos {qntAlunos} alunos:{formValue(avg)}')