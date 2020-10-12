from math import pi

coisas = input('Informe a altura e o raio do Cilindro nessa mesma ordem: ').split()
altura = float(coisas[0])
raio = float(coisas[1])

volume = pi * (raio ** 2) * altura

print(f'O volume desse Cilindro é de {volume}cm².')