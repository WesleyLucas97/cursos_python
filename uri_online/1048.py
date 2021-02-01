entrada = float(input())

if 0 < entrada <= 400:
    reajuste = (entrada * 15) / 100
    print(f'Novo salario: {(entrada + reajuste):.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 15 %')
elif 400 < entrada <= 800:
    reajuste = (entrada * 12) / 100
    print(f'Novo salario: {(entrada + reajuste):.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 12 %')
elif 800 < entrada <= 1200:
    reajuste = (entrada * 10) / 100
    print(f'Novo salario: {(entrada + reajuste):.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 10 %')
elif 1200 < entrada <= 2000:
    reajuste = (entrada * 7) / 100
    print(f'Novo salario: {(entrada + reajuste):.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual:  7%')
elif 2000 < entrada:
    reajuste = (entrada * 4) / 100
    print(f'Novo salario: {(entrada + reajuste):.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print('Em percentual: 4 %')
