# PROBLEMA DO PARÂMETRO PADRÃO MUTÁVEL

"""
Neste exercício falaremos sobre o problema de utilizarmos como parâmetro uma estrutura mútavel, como veremos a
utilização de uma lista no exemplo abaixo.
"""

def fibonacci(sequence=[0, 1]):
    """ Armadilha do uso de um valor DEFAULT mutável"""
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


start = fibonacci()
print(start, id(start))
print(fibonacci(start))

restart = fibonacci()
print(restart, id(restart))

"""
O que acontece é que eu supostamente tenho 2 ( duas ) variáveis ( START | RESTART ), porém o uso pd parâmetro mutável 
faz com que o Python aloque os dois valores em uma mesma variável, ou seja, ao invés de eu ter 2 ( dois ) resultados 
distintos eu terei apenas 1 ( um ).
"""

# CORREÇÃO DO PROBLEMA DO PARÂMETRO PADRÃO MUTÁVEL

"""
Nesta etapa veremos como podemos corrigir o PROBLEMA DO PARÂMETRO PADRÃO MUTÁVEL
"""

def fibonacci(sequence=None): # Por padrão estamos dizendo com uso de NONE que o resultado é FALSE
    sequence = sequence or [0, 1] # Se SEQUENCE for FALSE ele atribuirá automaticamente a LISTA [0, 1]
    sequence.append(sequence[-1] + sequence[-2])
    return sequence


start = fibonacci()
print(start, id(start))
print(fibonacci(start))

restart = fibonacci()
print(restart, id(restart))

"""
Basicamente ao passarmos um valor FALSE com o uso de NONE e validando o mesmo posteriormente poderemos usar um 
parâmetro mutável e assim corrigir o problema anterior tendo os RETORNOS alocados cada qual em uma variável específica.
"""
