"""
Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado.
O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência igual a zero
                            R = (R1 * R2)/(R1 + R2)
"""
while True:
    r1 = float(input('Insira um valor para resistor: '))
    r2 = float(input('Insira um valor para resistor: '))
    if r1 > 0 and r2 > 0:
        r = (r1 * r2)/(r1 + r2)
        print(f'Esse é valor da resistência {r:.2f}')
    else:
        break
