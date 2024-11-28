# CONJUNTOS - SET

"""
Conjuntos assim como dicionários faz uso em sua sintaxe das CHAVES ( {} ), porém os mesmos não fazem uso da
estrutura CHAVE / VALOR, um conjunto também não possui índices e não garantem ordenação dos seus valores.
"""

set_a = {1, 2, 3}
print(type(set_a))

"""
Podemos criar um conjunto ao utilizarmos o módulo .set(), como no exemplo abaixo.
"""

set_b = set("RALPH")
print(set_b) # Como veremos na resposta o mesmo não estará na ordem correta

"""
Além disso um CONJUNTO ( SET ), é uma estrutura que não aceita repetição, ou seja, se eu acrescentar uma letra
na minha STRING mais de uma vez o mesmo não trará a mesma repetidas vezes, como veremos no exemplo abaixo
"""

set_c = set("RRRRRALPH")
print(set_c)

"""
Também podemos utilizar os operadores de membro na estruturas SET, como no exemplo abaixo.
"""

set_d = set("RALPH")
print("R" in set_d, 2 in set_d)
print("r" in set_d) # Conjuntos são estruturas CASE SENSITIVE, ou seja, diferencia maiúsculo de minúsculo
print(4 not in set_d) # Também é possível fazermos uma verificação negativa

"""
Podemos criar a união de dois ( 2 ) conjuntos eliminando as repetições utilizando o módulo .union() como no 
exemplo abaixo.
"""

set_1 = {1, 2}
set_2 = {2, 3}

set_union = set_1.union(set_2)
print(set_union)

"""
Também podemos analisar quais membros são comuns aos dois conjuntos ( SET ) utilizando o módulo .intersection
como veremos no exemplo abaixo.
"""

set_intersection = set_1.intersection(set_2)
print(set_intersection)

"""
A atualização fará a 'união' entre os CONJUNTOS também eliminando duplicidades entre eles, também elimiando duplicidades
como no exemplo abaixo.
"""
set_1 = {1, 2}
set_2 = {2, 3}

set_1.update(set_2)

"""
O módulo .update() é um módulo que não retorna nada, ele modifica o objeto ( in place ), ou seja, se aplicarmos esta 
mesma ação dentro de uma variável a mesma retornará como None ( vazia ), isso por quê ele não retorna um novo objeto
atualizado, o que ele faz é alterar o CONJUNTO original diretamente, por esta razão aplicamos sem adicioná-lo a uma
variável
"""

print(set_1)

"""
Também podemos verificar se um CONJUNTO é sub-conjunto do outro, como no exemplo abaixo.
"""

sub_set = set_2 <= set_1

"""
Como fizemos um update anteriormente o resultado será verdadeiro ( TRUE ), porém se comentarmos o update o resultado 
será falso, isso por quê o SET_1 possui o elemento 1 ( um ) e o SET_2 possui o elemento 2 ( dois ) que destacam 
um do outro.
"""

print(sub_set)
