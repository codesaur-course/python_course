# PROEJTO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V7

"""
Neste exemplo iremos usar um LOOP FOR ao invés do WHILE, assim como faremos uso do RANGE() para partimos do índice 2
até o valor estipulado em QUANTIDADE, porém vale ressaltar que o módulo RANGE() não trará o último, sendo no fim
QUANTIDADE - 1
"""
from unittest import removeResult


def fibonacci(quantity):
    result = [0, 1]
    for _ in range(2, quantity): # Como já temos 2 elementos na LISTA iremos partir do segundo
        # O uso do UNDERLINE define uma variável que não está sendo usada, porém a sintaxe do FOR exige a mesma
        result.append(sum(result[-2:]))
    return result


for fib in fibonacci(20):
    print(fib)
