# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V4

def fibonacci(limit):
    result = [0, 1]

    while result[-1] < limit:
        result.append(result[-2] + result[-1])
    return result


for fib in fibonacci(20000): # Usamos o FOR neste exemplo para que o mesmo mostrasse número a número
    print(fib)

"""
Neste exemplo usamos uma lista para criarmos a mesma função de cálculo da sequência Fibonacci
"""
