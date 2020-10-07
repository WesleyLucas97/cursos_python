numeros = input('Digite dois números: ').split()
numero1 = numeros[0]
numero2 = numeros[1]

if numero1 > numero2:
    print('O número {} é maior que o número {}.'.format(numero1, numero2))
else:
    print('O número {} é maior que o número {}.'.format(numero2, numero1))