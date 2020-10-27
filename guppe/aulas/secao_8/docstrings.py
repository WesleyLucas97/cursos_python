"""
Documentando funcoes com Docstrings

OBS: Podemos ter acesso a documentacao de uma funcao em Python utilizando a propriedade especial __doc__

Podemos aind fazer acesso a documentacao com a funcao help()
"""

def diz_oi():
    """Uma funcao simples que retorna a string 'Oi!'"""
    return 'Oi!'


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Ptencia que queremos gerar o exponencial. Por Padrao e 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """

    return numero ** potencia

print(help(exponencial))
