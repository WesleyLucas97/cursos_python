"""
Elabore uma funcao que receba tres notas de um aluno como parametros e uma letra.
Se a letra for A, a funcao devera calcular a media aritmetica das notas do aluno;
se for P, devera calcular a media ponderada, com pesos 5, 3 e 2.
"""
import random
nota = []
for x in range(3):
    nota.append(random.randint(0, 10))
letra = random.choice(['A', 'P'])


def media(lista_notas, letra_):
    if letra_ == 'A':
        media1 = sum(lista_notas) / len(lista_notas)
        return f'O aluno tem como media aritmetica {media1:.2f}, das notas {lista_notas}'
    elif letra_ == 'P':
        media2 = (nota[0] * 5 + nota[1] * 3 + nota[2] * 2) / (5 + 3 + 2)
        return f'O aluno tem como media ponderada {media2:.2f}, das notas {lista_notas}'


print(media(nota, letra))
