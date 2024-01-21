perguntas = [
    {
        'Pergunta': 'O que é melhor pra saude?',
        'Opções': ['Coca cola', 'Agua', 'Vodka'],
        'Resposta': 'Agua',
    },
    {
        'Pergunta': 'Quanto é 5*2?',
        'Opções': ['3', '7', '10'],
        'Resposta': '10',
    }
]

qtd_acertou = 0 

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)


    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes [escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertou += 1
        print('Acertou')
    else:
        print('Errou')

    print()
    
print('Você acertou', qtd_acertou)
print('de', len(perguntas), 'perguntas.')
