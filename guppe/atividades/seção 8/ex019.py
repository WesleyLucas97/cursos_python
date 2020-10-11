"""
Faca uma funcao que retorne o maior fator primo de um numero.
"""
from random import randint
n = randint(10, 1000)


def primo(x):
    # um vetor com os numeros primos, poderia chamar de primos, mas tem a funcao primo ja
    vector = [2, 3, 5]

    for i in range(7, x + 1):
        # n1 vai ser o parametro para dividir os primos dos nao primos
        n1 = 0
        # verificar se o numero eh divisivel por 2 ou 3, onde eu ja retiro a maioria dos numeros nao primos
        if i % 2 == 0 or i % 3 == 0:
            n1 += 1
        else:
            n2 = 0
            # um loop pegando cada um dos numeros primos da lista
            while n2 <= len(vector):
                # verificando se o numero tem divisor dentro da lista de primos, em caso positivo, nao eh primo
                if i % vector[n2] == 0:
                    n1 += 1
                # um parametro matematico para definir se o numero eh primo, o quociente < divisor
                elif int(i / vector[n2]) < vector[n2]:
                    break
                n2 += 1
        # verificando o parametro para determinar se eh primo e adicionar na lista dos primos
        if n1 == 0:
            vector.append(i)

    # verificar se o numero informado ja nao eh primo
    if x in vector:
        return f'O numero {x} eh primo!'
    # finalmente verificando oq me pede, saber qual que eh o maior fator primo
    else:
        for j in vector[::-1]:
            if x % j == 0:
                break
        return f'O maior primo do numero {x} eh {j}'


print(primo(n))
