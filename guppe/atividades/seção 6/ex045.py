"""
Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar um menu com as
duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar,
sendo que o programa só será finalizado quando a opção de finalizar for escolhida.
"""

while True:
    n1 = int(input("""
Escolha uma das opções a baixo:
1_ Conversão de km/h para m/s;
2_ Conversão de m/s para km/h;
3_ Sair do programa.
"""))
    if n1 == 1:
        n2 = float(input('Digite a velocidade em km/h: '))
        n3 = n2 / 3.6
        print(f'A velocidade é de {n3:.2f} m/s')
    elif n1 == 2:
        n2 = float(input('Digite a velocidade em m/s: '))
        n3 = n2 * 3.6
        print(f'A velocidade é de {n3:.2f} km/h')
    elif n1 == 3:
        print('Obrigado por usar nosso programa!')
        break
