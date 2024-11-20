# MAIS OPERADORES ( MEMBRO | IDENTIDADE )

"""
Operadores membros ( IN ) e ( NOT IN ) servem para verificarmos se um MEMBRO específico integra um grupo, já os
operadores de identidade ( IS ) e ( IS NOT ) servem para verificarmos a identidade de um item.
Veremos um pouco mais nos exemplos abaixo:
"""

# OPERADOR MEMBRO

list_example = [1, 2, 3, "Ana", "Carla"]
print(2 in list_example)
print("Ana" not in list_example)

"""
Quando executamos o método vemos que no primeiro caso recebemos TRUE e no segundo caso FALSE isso por quê no primeiro
caso 1 está na lista e no segundo caso 'Ana' também está mas eu fiz o processo de verificação do membro de forma
negativa, como se estivesse alegando que a mesma não fazia parte, mas se olharmos a lista veremos que a mesma faz sim
parte do grupo.
"""

# OPERADORES DE IDENTIDADE

x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(x is not z)

"""
Neste caso teremos TRUE para os dois primeiros valores e FALSE para o terceiro, isso por quê estamos verificando valores
simples contidos nas variáveis, ou seja, por mais que seja espaços distinto os valores são iguais.
"""

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b)
print(list_b is list_c)
print(list_a is not list_c)

"""
Já neste caso teremos uma sequência de TRUE, FALSE, TRUE, isso por quê as listas A e C, por mais que tenham os mesmos
valores, usam estruturas de dados mais complexas, as listas neste exemplo, e possuem identidades distintas
e por esta razão não são as mesmas.
"""
