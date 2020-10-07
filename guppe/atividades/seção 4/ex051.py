from math import sqrt

coordenadas = input('Informe as coordenadas do ponto: ').split(', ')
coordenada1 = float(coordenadas[0])
coordenada2 = float(coordenadas[1])

distancia = sqrt(coordenada1 ** 2 + coordenada2 ** 2)

print(f'A distancia da origem é de {distancia}.')