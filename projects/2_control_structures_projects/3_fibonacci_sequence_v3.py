# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V3

def fibonacci(limit):
    penultimate = 0
    last = 1

    print(f"{penultimate}, {last}", end=', ')

    while last < limit:
        penultimate, last = last, penultimate + last # O que estamos fazendo aqui chamasse ATRIBUIÇÃO MÚLTIPLA
        print(f"{last}", end=', ')


fibonacci(20000)

"""
Nesta versão podemos notar que armazenamos nas variáveis PENULTIMATE e LAST ( linha 10 ), os valores de LAST na 
PENULTIMATE e a soma entre PENULTIMATE e LAST na variável LAST, deste modo decartando a necessidade de criar uma 
variável que receba o próximo valor.
"""
