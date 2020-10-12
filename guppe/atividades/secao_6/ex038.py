"""
Faça um programa que calcule o termo pitagórico a, b, c = 1000. Um termo pitagórico é um conjunto de três números
naturais, a, b, c, para qual,
                    a² + b² = c²
Por exemplo,
                    3² + 4² = 9 + 16 = 25 = 5²
"""
for a in range(1000):
    for b in range(1000):
        c2 = a ** 2 + b ** 2
        c = c2 ** 0.5
        if a + b + c == 1000:
            print(f'{a} + {b} + {c:.0f} = 1000')
