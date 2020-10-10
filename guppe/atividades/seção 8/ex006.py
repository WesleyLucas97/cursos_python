"""
Faca uma funcao que receba 3 numeros inteiros como parametro, representando horas, minutos e segundos, e os converta
em segundos
"""
n1 = input('Digite a hora em formato "hora:minuto:segundo": ').split(':')
hora, minuto, segundo = int(n1[0]), int(n1[1]), int(n1[2])


def seg(a, b, c):
    hr = a * 3600
    min = b * 60
    return f'horas = {hr}, minutos = {min} e {c}'


print(seg(hora, minuto, segundo))
