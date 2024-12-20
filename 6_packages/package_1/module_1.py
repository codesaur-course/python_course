# PACOTES EM PYTHON

"""
Pacotes podem ser usados para separar os arquivos de um projeto, o que definirá que um repositório ou pasta é um
pacote é o arquivo __INIT__.PY, esse arquivo mesmo vazio, ou seja, mesmo não havendo nenhuma linha de código nele ele
indicará ao Python que aquela pasta se trata de um pacote específico.
"""

print(f"Importado módulo: {__name__}. Do pacote: {__package__}") # Aqui pegamos os nomes do módulo e do pacote


def sum(x, y):
    return x + y
