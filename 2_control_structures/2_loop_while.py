# ESTRUTURA DE REPETIÇÃO - WHILE

"""
Uma estrutura de repetição visa, como o próprio nome implica, repetir um bloco de código enquanto a condição
apresentada não for atendida, nós veremos um exemplo abaixo no qual; usaremos a primeira estrutura de repetição com
o módulo WHILE.
"""

from random import randint # Pega um número aleatório entre uma faixa específica, neste caso 0 e 9


number = -1
secret_number = randint(0, 9)

while number != secret_number:
    number = int(input("Informe um número entre 0 e 9: "))

print(f"O número secreto {number} foi encontrado!")

"""
O loop WHILE é usado quando não temos uma ideia de repetições a serem executadas, ele irá repetir a ação até que o
valor da condição seja atendido.
"""
