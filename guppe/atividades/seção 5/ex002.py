numero = float(input('Digite um número qualquer: '))

if numero > 0:
    numero = numero ** (1/2)
    print('O valor da raiz quadrada do número é {:.2f}'.format(numero))
else:
    print('O número digitado não tem uma raíz quadrada, pois é negativo.')
