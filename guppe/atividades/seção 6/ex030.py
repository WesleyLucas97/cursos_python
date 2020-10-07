'''
Faça programas para calcular as seguintes sequências:
        1 + 2 + 3 + 4 + 5 + ... + n
        1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
        1 + 3 + 5 + 7 + 9 + ... + (2n - 1)
'''


n1 = int(input('Digite a porra do número: '))
som = 0

for x in range(1, n1+1):
    som += x
print(som)

som = 0

for x in range(1, 2*n1):
    if x % 2 == 0:
        som -= x
    else:
        som += x
print(som)

som = 0

for x in range(1, 2*n1, 2):
    som += x
print(som)
