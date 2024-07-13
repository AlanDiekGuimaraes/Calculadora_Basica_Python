
operacao = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação',
    'Sair': 'Sair'
}

while True:
    print(50 * '=')
    contador = 0
    nome = ''
    for operador, nome in operacao.items():
        print(contador, ':', nome)
        contador += 1
    print(50 * '=')
    try:
        operador = int(input('Escolha a operação que deseja realizar: '))
        if operador < 0 or operador >= len(operacao):
            raise ValueError
    except ValueError:
        print('Opção Invalida, tente novamente.')
        continue
    try:
        operacao_selecionada = list(operacao.values())[operador]
        operador_string = list(operacao.keys())[operador]
        print(f'\nOperação selecionado: {operacao_selecionada}\n ')
        resultado = 0
        valor_01 = float(input('Digite o primeiro valor: '))
        valor_02 = float(input('Digite o segundo valor: '))
        if operador == 0:
            resultado = valor_01 + valor_02
        elif operador == 1:
            resultado = valor_01 - valor_02
        elif operador == 2:
            resultado = valor_01 * valor_02
        elif operador == 3:
            if valor_01 == 0:
                print('Não é possível dividir por 0')
            else:
                resultado = valor_01 / valor_02
        elif operador == 4:
            resultado = valor_01 ** valor_02
        elif operador == 5:
            exit()

        print(f'{valor_01} {operador_string} {valor_02} = {resultado}')

        while True:
            opcao = input("Deseja realizar outra operação? 1 = SIM, 2 = NÃO  ")
            if opcao != '1' and opcao != '2':
                print('Opção invalida, tente novamente')
            elif opcao == '1':
                break
            elif opcao == '2':
                exit()
    except ValueError:
        print('Você digitou algum valor invalido, tente novamente.')


