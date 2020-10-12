'''
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de
notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética.
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando
for introduzido um valor que não seja válido como nota de aprovação.
'''

soma = 0
soma2 = 0


while True:
    n1 = float(input('Insira uma nota no intervalo de 10 a 20: '))
    if 10 > n1 or n1 > 20:
        break
    else:
        soma += n1
        soma2 += 1

media = soma / soma2

print(f'A tua média é de {media:.1f}')
