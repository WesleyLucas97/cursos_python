"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
OBS: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
"""

entrada = input().split()

hora1 = int(entrada[0])
minuto1 = int(entrada[1])
hora2 = int(entrada[2])
minuto2 = int(entrada[3])

start = hora1*60 + minuto1
end = hora2*60 + minuto2
duracao = 0


if hora1 <= hora2:
    duracao = end - start
    if duracao == 0:
        print(f'O JOGO DUROU {24} HORA(S) E {0} MINUTO(S)')
    else:
        print(f'O JOGO DUROU {int((duracao - (duracao%60)) / 60)} HORA(S) E {duracao%60} MINUTO(S)')
else:
    duracao = end - (start + 60)
    print(f'O JOGO DUROU {int((duracao - (duracao%60)) / 60)} HORA(S) E {duracao%60} MINUTO(S)')
