"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20. Ex: 2520 é o menor número
que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.
"""

n1 = 1

while True:
    print(n1)
    check = 0
    for x in range(1, 21):
        check += n1 % x

    if check == 0:
        print(f'O menor divisivel é : {n1}.')
        break
    n1 += 1
