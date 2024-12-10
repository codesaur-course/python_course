# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V6

"""
Neste exemplo ao invés de estabelecermos um LIMITE nós iremos pedir uma quantidade específica de números a serem
apresentados no resultado final.
"""

def fibonacci(quantity):
    result = [0, 1]
    while True:
        result.append(sum(result[-2:]))
        if len(result) == quantity: # Quando a LISTA tiver o tamanho estipulado por QTIDADE o LOOP irá parar
            break
    return result


# Listar os 20 primeiros números da sequência de Fibonacci
for fib in fibonacci(20):
    print(fib)
