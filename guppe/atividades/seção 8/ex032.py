"""
Faca uma funcao chamada 'simplifica' que recebe como parametro o numerador e o denominador de uma fracao. Esta funcao
deve simplificar a fracao recebida dividindo o numerador e o denominador pelo maior fator possivel. Por exemplo, a
fracao 36/60 simplificada para 3/5 dividindo o numerador e o denominador por 12. A funcao deve modificar as variaveis
passadas como parametro.
"""
from random import randint


def simplifica(x):
    n1 = x.split('/')
    a, b = int(n1[0]), int(n1[1])
    if a > b:
        for i in range(a - 1, 1, -1):
            if a % i == 0 and b % i == 0:
                simp = str(int(a/i)) + ' / ' + str(int(b/i))
                if simp == x:
                    return f'A fracao {x} ja esta simplificada'
                else:
                    return f'A fracao {x} pode ser simplificada por {i} retornando {simp}'

    else:
        for i in range(b, 0, -1):
            if a % i == 0 and b % i == 0:
                simp = str(int(a / i)) + ' / ' + str(int(b / i))
                if simp == x:
                    return f'A fracao {x} ja esta simplificada'
                else:
                    return f'A fracao {x} pode ser simplificada por {i} retornando {simp}'
    return f'A fracao {x} ja esta simplificada'


num = str(randint(0, 1000)) + ' / ' + str(randint(0, 1000))
print(num)
print(simplifica(num))
