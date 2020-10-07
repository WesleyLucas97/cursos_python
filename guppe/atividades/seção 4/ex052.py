apostas = input('Informe os valores que cada um vai apostar: ').split()
premio = float(input('Iforme o valor do prêmio: '))

aposta1 = float(apostas[0])
aposta2 = float(apostas[1])
aposta3 = float(apostas[2])
total_das_apostas = aposta1 + aposta2 + aposta3

por_aposta1 = ((aposta1 * 100) / total_das_apostas)
por_aposta2 = ((aposta2 * 100) / total_das_apostas)
por_aposta3 = ((aposta3 * 100) / total_das_apostas)

rec_apost1 = ((por_aposta1 * premio) / 100)
rec_apost2 = ((por_aposta2 * premio) / 100)
rec_apost3 = ((por_aposta3 * premio) / 100)

print(f'Com base nas apostas o primeiro deve receber {rec_apost1}, o segundo {rec_apost2} e o terceiro {rec_apost3}')