print('Opção 1 - Lógica de Programação')
print('Opção 2 - Estrutura de Dados')
print('Opção 3 - Banco de Dados')
print('Opção 4 - Desenvolvimento Web')
print('Opção 5 - Inteligência Artificial')

opcao = int(input('Escolha a opção de livro desejado (1 a 5): '))
num_formato = int(input('Escolha o formato (1 para Impresso ou 2 para Digital): '))
quantidade = int(input('Informe a quantidade de livros que deseja comprar: '))
formato = 'Impresso' if num_formato == 1 else 'Digital'

if opcao not in range(1,6) or num_formato not in (1,2) or quantidade <= 0:
    print('Ocorreu um erro, por favor tente novamente.')
else:
    match opcao:
        case 1:
            categoria = 'Lógica de Programação'
            sigla = 'LP'
            valor_un = 65 if num_formato == 1 else 45 * 0.95
            valor_ttl_s_desc = 65 * quantidade if num_formato == 1 else 45 * quantidade
        case 2:
            categoria = 'Estrutura de Dados'
            sigla = 'ED'
            valor_un = 80 if num_formato == 1 else 60 * 0.95
            valor_ttl_s_desc = 80 * quantidade if num_formato == 1 else 60 * quantidade
        case 3:
            categoria = 'Banco de Dados'
            sigla = 'BD'
            valor_un = 75 * 0.9 if num_formato == 1 else 55 * 0.95
            valor_ttl_s_desc = 75 * quantidade if num_formato == 1 else 55 * quantidade
        case 4:
            categoria = 'Desenvolvimento Web'
            sigla = 'DW'
            valor_un = 70 if num_formato == 1 else 50 * 0.95
            valor_ttl_s_desc = 70 * quantidade if num_formato == 1 else 50 * quantidade
        case 5:
            categoria = 'Inteligência Artificial'
            sigla = 'IA'
            valor_un = 90 if num_formato == 1 else 70 * 0.95
            valor_ttl_s_desc = 90 * quantidade if num_formato == 1 else 70 * quantidade
    if valor_ttl_s_desc > 300:
        valor_final = valor_un * quantidade * 0.85
    else:
        valor_final = valor_un * quantidade

    print(f'\nLivro: {categoria} ({sigla})\n'\
          f'Formato: {formato}\n'\
          f'Quantidade: {quantidade}\n'\
          f'{f'Valor total sem desconto: R${valor_ttl_s_desc: .2f}\n' if valor_ttl_s_desc != valor_final else ''}\n'\
          f'{f'Valor final com descontos aplicados: R${valor_final: .2f}' if valor_ttl_s_desc != valor_final else f'Nenhum desconto aplicado, valor final: R${valor_final: .2f}'}')
