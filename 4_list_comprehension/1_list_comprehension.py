# LIST COMPREHENSION

"""
LIST COMPREHENSION é uma forma mais concisa e robusta de criar listas. Basicamente a sintaxe se constrói assim:
[ EXPRESSÃO - FOR item IN lista IF CONDICIONAL ].
A mesma assim como uma LISTA comum terá sua contrução baseada no uso de COLCHETES e dentro eles você terá uma
EXPRESSÃO seguida de um LOOP FOR que irá iterar uma lista analisando item a item e se preciso você terá uma
condicional IF para tratar os casos.
"""

# EXEMPLO 1 - LIST
double_1 = []
for i in range(10):
    double_1.append(i * 2)
print(double_1)


# EXEMPLO 2 - LIST COMPREHENSION - [ EXPRESSÃO FOR item IN lista ]
double_2 = [i * 2 for i in range(10)]
print(double_2)

"""
No exemplo um temos a lista comum e no exemplo dois temos LIST COMPREHENSION, porém sem adição da CONDICIONAL.
"""

# EXEMPLO 3 - LIST
pair_doubles_1 = []
for i in range(10):
    if i % 2 == 0:
        pair_doubles_1.append(i * 2)
print(pair_doubles_1)


# EXEMPLO 4 - LIST COMPREHENSION - [( EXPRESSÃO ) FOR item IN lista IF ( CONDICIONAL )]
pair_doubles_2 = [i * 2 for i in range(10) if i % 2 == 0]
print(pair_doubles_2)

"""
No exemplo três acima temos a mesma LISTA na maneira convencional, por assim dizer, já no exmeplo quatro temos uma 
LIST COMPREHENSION utilizando CONDICIONAL.
"""
