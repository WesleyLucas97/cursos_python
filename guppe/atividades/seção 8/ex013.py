"""
Faca uma funcao que receba dois valores numericos e um simbolo. Este simbolo representara a operacao que se deseja
efetuar com os numeros. Se o simbolo for + devera ser realizada uma adicao, se for - uma subtracao, se for / uma
divisao e se for * sera efetuada uma multiplicacao.
"""
import random
n1 = random.randint(0, 1000)
n2 = random.randint(0, 1000)
n3 = random.choice(['+', '-', '*', '/'])


def calculadora(a, b, c):
    if c == '+':
        return f'{a} {c} {b} = {a + b}'
    elif c == '-':
        return f'{a} {c} {b} = {a - b}'
    elif c == '*':
        return f'{a} {c} {b} = {a * b}'
    return f'{a} {c} {b} = {a / b}'


print(calculadora(n1, n2, n3))
