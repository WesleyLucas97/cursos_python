"""
Saindo de loops com break

Funciona da mesma forma que nas línguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saiu do loop.')
print(' ')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ").title()
    if comando == 'Sair':
        print('Bom Garoto.')
        break
    else:
        print("Eu mandei digitar 'sair' seu animal. ")