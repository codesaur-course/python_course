# DICT COMPREHENSION

"""
Neste exercício iremos fazer aprender a usar DICIONÁRIOS com a mesma síntaxe do LIST COMPREHENSION, com exceção do uso
de COLCHETES, visto que DICIONÁRIOS fazem, em sua construção, o uso de CHAVES e VALORES.
"""

dict_comprehension = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dict_comprehension)

for number, double in dict_comprehension.items():
    print(f"{number} X 2 = {double}")
