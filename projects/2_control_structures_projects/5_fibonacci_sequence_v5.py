# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V5

"""
Neste exemplo iremos usar a função .sum() do Python para realizar a soma.
"""

def fibonacci(limit):
    result = [0, 1]
    while result[-1] < limit:
        result.append(sum(result[-2:])) # Aqui nós já estamos 'pegando' os dois último resultados e somando
    return result


for fib in fibonacci(20000):
    print(fib)
