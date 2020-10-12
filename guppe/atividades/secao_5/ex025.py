from math import sqrt
fun = input('''
Digite uma equação de segundo grau, exemplo: ax² + bx + c = 0
''')
funcao = fun.split()
a = (funcao[0]).split('x²')
a = float(a[0])
b = (funcao[2]).split('x')
b = float(b[0])
c = float(funcao[4])

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print('A raiz não existe.')
elif delta == 0:
    x = (-b) / (2 * a)
    print('A raiz é única e vale {:.2f}'.format(x))
else:
    x1 = ((-b) + sqrt(delta)) / (2 * a)
    x2 = ((-b) - sqrt(delta)) / (2 * a)
    print('O valor da primeira raiz é {:.2f} e da segunda é {:.2f}.'.format(x1, x2))