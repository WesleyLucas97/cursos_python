from random import randint
n = 1

while n <= 5:
    a = randint(0, 100)
    b = randint(0, 100)
    soma = a + b
    print('Qual a soma entre {} e {}.'.format(a, b))
    resultado = int(input())
    if resultado == soma:
        print('Você acertou!')
    else:
        print('Você errou infeliz das costas oca.')
    n += 1
