# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI - COM RECURSIVIDADE

"""
Neste exemplo iremos aplicar RECURSIVIDADE ao projeto de cálculo da sequência Fibonacci
"""

def fibonacci(quantity, sequence=(0, 1)): # Neste caso o parâmetro SEQUÊNCIA possui valores por padrão
    # IMPORTANTE: CONDIÇÃO DE PARADA
    if len(sequence) == quantity: # Aqui estbelecemos a condição de parada, sequência igual a quantidade estipulada
        return sequence
    return fibonacci(quantity, sequence + (sum(sequence[-2:]),)) # Aqui aplicamos a recursividade
"""
Nesta linha acima estamos somando duas TUPLAS, essa soma irá gerar uma única TUPLA com os valores da escala Fibonacci.
Isso que está acontecendo acima também pode ser reconhecido como sobrecarga de operadores.
"""


for fib in fibonacci(20): # Aqui não precisamos passar SEQUÊNCIA visto que já existem valores por padrão
    print(fib)
