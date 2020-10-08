"""
Funcoes com Parametro (de entrada)

    - Funcoes que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos;

entrada -> processamente -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:
    - Nao possuem entrada;
    - Nao possuem saida;
    - Possuem entrada mas nao possuem saida;
    - Nao possuem entrada mas possuem saida;
    - Possuem entrada e saida;

"""

# Refatorando uma funcao

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())

for x in range(20):
    print(x)
    
