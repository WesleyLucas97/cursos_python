catetos = input('Informe quais são os catetos do triângulo: ').split()
cateto1 = float(catetos[0])
cateto2 = float(catetos[1])

hipotenusa = (cateto1 ** 2 + cateto2 ** 2)**(1/2)

print(f'O valor da hipotenusa é de {hipotenusa}.')