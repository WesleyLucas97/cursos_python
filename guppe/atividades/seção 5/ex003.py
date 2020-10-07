numero = float(input('Digite um número real: '))

if numero > 0:
    numero2 = numero ** (1/2)
    print('A raiz quadrada do número {} é {:.2f}.'.format(numero, numero2))
else:
    numero2 = numero ** 2
    print('O valor do quadrado do número {} é {:.2f}'.format(numero, numero2))
