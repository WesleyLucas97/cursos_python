soma = 0
n = 1

while n <= 10:
    numero = int(input('Digite um número inteiro: '))
    if numero > 0:
        n = n + 1
        soma = soma + numero
        print(soma)
    else:
        print('Digite um número POSITIVO, seu infeliz!!!!!')

media = soma / 10

print('A média desses números é {:.2f}'.format(media))