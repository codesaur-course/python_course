# OPERADORES TERNÁRIOS

"""
Operadores ternários como o próprio nome propõe estão relacionados a processo que utilizam 3 (três) operadores,
abaixo iremos ver duas possibilidade de aplicação sendo que uma está diretamente ligado ao uso do condicional ( IF )
o qual veremos mais a frente.
"""

"""
No exemplo abaixo teremos uma variável contendo um valor booleano, em seguida faremos um print contendo uma frase
a qual aplicará o valor da variável de acordo com a sua posição.
"""

raining = True
print("Hoje estou com as roupas " + ("secas.", "molhadas.")[raining])

"""
O que vemos aqui é que a opção que está mais próxima da variável é VERDADEIRA e a que está mais distante é FALSA. Também
poderíamos tratar este caso com um IF como vemos no exemplo abaixo:
"""

print("Hoje estou com as roupas " + ("molhadas." if raining else "secas."))
