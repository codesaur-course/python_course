# GENERATOR WITH FOR

"""
Neste exercício veremos o uso de GENERATOR com FOR, diferente da versão anterior por possuir um LOOP FOR que irá iterar
a LISTA e interromper ao final não precisaremos do uso do NEXT()
"""

generator = (i ** 2 for i in range(10) if i % 2 == 0)

for number in generator:
    print(number)
