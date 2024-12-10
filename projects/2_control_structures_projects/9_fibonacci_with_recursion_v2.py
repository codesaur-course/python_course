#  PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI - COM RECURSIVIDADE

"""
Neste exemplo faremos uma aplicação com operadores ternários
"""

def fibonacci(quantity, sequence=(0, 1)):
    return sequence if len(sequence) == quantity else \
        fibonacci(quantity, sequence + (sum(sequence[-2:]),))


for fib in fibonacci(20):
    print(fib)
