# OPERADORES LÓGICOS

"""
No caso dos Operadores Lógicos nós iremos analisar uma ou mais condições para determinar a veracidade  dos dados, ou
seja, estamos falando de um operador binário, que lida com dois operandos na sua avaliação, como veremos nos
exemplos abaixo:
"""

# OPERADOR LÓGICO ( AND )
"""
Operadores Lógicos atuam através de algo que chamamos de TABELA VERDADE, no caso do AND ambas as condições devem
ser verdadeiras, se uma delas não for o resultado será sempre falso.
"""

print(2 < 5 and 9 < 11) # True
print(2 < 5 and 9 < 8) # False
print(5 < 2 and 9 < 8) # False
print(5 < 2 and 9 < 11) # False

print(True and True)
print(True and False)
print(False and False)
print(False and True)

"""
Como é possível ver apenas a primeira opção atende como verdade na análise dos dois operandos apresentados, assim sendo,
esta a única verdadeira.
"""

# OPERADOR LÓGICO ( OR )
"""
Já no caso do OR desde que uma das consições apresentadas seja verdade o resultado será verdadeiro.
"""

print(5 > 2 or 9 > 11) # True
print(2 < 5 or 9 < 11) # True
print(2 > 5 or 9 > 11) # False
print(2 > 5 or 9 < 11) # True

print(True or False)
print(True or True)
print(False or False)
print(False or True)

# OPERADOR LÓGICO ( XOR )
"""
No caso do XOR também conhecido como OU EXCLUSIVO preciso que obrigatoriamente um dos dois operadores seja diferente,
por exemplo:
"""

print(True != True) # False
print(True != False) # True
print(False != False) # False
print(False != True) # True

"""
Podemos entender que neste caso é uma análise negativa ou de diferença, se acaso algo não for 'igual à' alguma coisa.
"""

# OPERADOR LÓGICO DE NEGAÇÃO ( NOT )
"""
Diferente dos demais acima o NOT é um operador UNÁRIO, ou seja, ele trata a veracidade analisando um operadorando.
"""

print(not True) # False
print(not False) # True

# OPERADORES LÓGICOS BIT A BIT ( &, |, ^ )
"""
O que esses operadores fazem é analisar o operandos BIT-A-BIT e assim verificar sua veracidade.
"""

print(True & True) # Similar ao AND
print(True | False) # Similar ao OR
print(False ^ True) # Similar ao XOR

"""
Supondo que em binário o número 3 seja igual a 11 (em binário) e 2 seja igual a 10 (também em binário) o que esses 
operadores fazem é analisar os 1(uns) e 0(zeros) de cada operando.
"""

# AND BIT-A-BIT
# 3 = 11
# 2 = 10
# _ = 10

print(3 & 2)

# OR BIT-A-BIT
# 3 = 11
# 2 = 10
# _ = 11
print(3 | 2)

# XOR BIT-A-BIT
# 3 = 11
# 2 = 10
# _ = 01
print(3 ^ 2)

"""
Lembrando que no caso do XOR é obrigatoriamente um ou outro. por isso dará 1
"""
