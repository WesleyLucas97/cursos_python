operacao = input('''
Escolha as seguintes operações:
Soma;
Subtração;
Multiplicação;
Divisão.
''').title()

if operacao == 'Soma':
    numeros = input('Digite os números: ').split()
    numero1 = float(numeros[0])
    numero2 = float(numeros[1])

    realizado = numero1 + numero2

    print('O valor da {} é {:.2f}'.format(operacao, realizado))
elif operacao == 'Subtração':
    numeros = input('Digite os números: ').split()
    numero1 = float(numeros[0])
    numero2 = float(numeros[1])

    realizado = numero1 - numero2

    print('O valor da {} é {:.2f}'.format(operacao, realizado))
elif operacao == 'Multiplicação':
    numeros = input('Digite os números: ').split()
    numero1 = float(numeros[0])
    numero2 = float(numeros[1])

    realizado = numero1 * numero2

    print('O valor da {} é {:.2f}'.format(operacao, realizado))
elif operacao == 'Divisão':
    numeros = input('Digite os números: ').split()
    numero1 = float(numeros[0])
    numero2 = float(numeros[1])

    realizado = numero1 / numero2

    print('O valor da {} é {:.2f}'.format(operacao, realizado))
