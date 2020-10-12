nota = input('Digite as duas notas obtidas: ').split()
nota1 = float(nota[0])
nota2 = float(nota[1])

if 0 < nota1 <= 10 and 0 < nota2 <= 10:
    media = (nota1 + nota2) / 2
    print('A média obtida é de {:.2f}'.format(media))
else:
    print('As notas informadas não são válidas, seu animal do caralho.')
