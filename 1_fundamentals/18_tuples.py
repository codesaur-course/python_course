# TUPLAS

"""
Tuplas são estruturas de dados imutáveis e sua sintaxe se define pelo uso de parênteses ().
"""

tuple_example = tuple()
print(type(tuple_example))

tuple_example = ()
print(type(tuple_example))

print(dir(tuple))

"""
Vale ressaltar que para criarmos uma tupla devemos utilizar o parênteses, porém se aplicarmos um item e utilizarmos
 as aspas ( " ) precisamos encerrar com uma vírgula ( , ) sempre, senão o mesmo não o interpretará como tupla e sim
 como STRING, abaixo demonstaremos um exemplo prático desta prática.
"""

tuple_one = ("um",)
print(tuple_one)
print(type(tuple_one))

"""
Tuplas são estruturas indexadas, ou seja, podemos acessar as informações contidas na mesma por meio de seus índices,
como no exemplo abaixo.
"""

print(tuple_one[0])

"""
Vamos ver um exemplo contendo mais valores abaixo.
"""

tuple_two = ("azul", "verde", "vermelho", "branco", "amarelo")
print(tuple_two[0])
print(tuple_two[1])
print(tuple_two[2])
print(tuple_two[3])
print(tuple_two[4])

"""
Também podemos acessar os mesmos do último para o primeiro.
"""
print("")
print(tuple_two[-1])
print(tuple_two[-2])
print(tuple_two[-3])

"""
Também podemos acessar por intervalos
"""

print(tuple_two[1:]) # A partir do índice 1 ( um ) até o último

"""
Podemos descobrir o índice dos elementos através do uso do módulo index() como no exemplo abaixo.
"""

print(tuple_two.index("vermelho"))

"""
Também é possível contar o número de elementos de mesmo valor existem dentro da TUPLA, como no exemplo abaixo.
"""

print(tuple_two.count("verde"))

"""
E podemos ver o tamanho da TUPLA usando o módulo len() como no exemplo abaixo
"""

print("")
print(len(tuple_two))
