# PACKING | UNPACKING

"""
O conceito de PACKING refere-se ao uso do asterísco ( * ) em frente a um parâmetro para que o mesmo seja encapsulado,
em um cenário específico.
"""

def sum_2(a, b):
    return a + b

result = sum_2(2, 3)
print(result)


def sum_3(a, b, c):
    return a + b + c

result = sum_3(2, 3, 5)
print(result)


def sum_n(*numbers): # neste exemplo de PACKING o parâmetro NUMBERS se tornará uma TUPLA
    print(type(numbers))
    sum_test = 0
    for n in numbers:
        sum_test += n
    return sum_test

print(sum_n(1, 1, 1, 1, 1, 1, 1)) # Exemplo de PACKING


"""
Já o conceito de UNPACKING seria usado quando possuo o valor dentro de uma estrutra específica e da qual eu desejo
extrair os valores, isso é feito através do uso do asterísco ( * ) como veremos no exemplo abaixo.
"""

tuple_nums = (1, 2, 3) # UNPACKING de TUPLA
print(sum_3(*tuple_nums))

list_nums = [1, 2, 3] # UNPACKING de LISTA
print(sum_3(*list_nums))
