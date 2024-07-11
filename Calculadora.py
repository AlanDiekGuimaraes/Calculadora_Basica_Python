print(50 * '=')
operacao = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação'
}

while True:
    contador = 0
    for operador, name in operacao.items():
        print(contador, ':', name)
        contador += 1

    try:
        operador = int(input('Escolha a operação que deseja realizar: '))
        if operador < 0 or operador >= len(operacao):
            raise ValueError
    except ValueError:
        print('Opção Invalida, tente novamente.')
        continue

    operador_string = list(operacao.keys())[operador]
    print(f'\nOperador selecionado: {operador_string}\n ')
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

    print(f'{valor_01} {operador_string} {valor_02} = {resultado}')

    while True:
        opcao = input("Deseja realizar outra operação? 1 = SIM, 2 = NÃO  ")
        if opcao != '1' and opcao != '2':
            print('Opção invalida, tente novamente')
        elif opcao == '1':
            break
        elif opcao == '2':
            exit()