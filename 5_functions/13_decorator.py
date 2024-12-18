# DECORATOR

"""
Neste exercício iremos aprender o que é um DECORATOR.
DECORATOR é um padrão que permite extender o objeto, fazendo novas adições ao objetos sem a necessidade de herança.
Quando nos deparamos com a possibilidade de reuso por herança ou por composição o melhor seria priorizarmos o reuso por
composição ( DECORATOR ).
"""

def log(function):
    def decorator(*args, **kwargs): # INNER FUNCTION
        print(f"Início da chamada da função: {function.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = function(*args, **kwargs)
        print(f"Resultado da chamada: {result}")
        return result
    return decorator


@log # DECORATOR
def sum_example(x, y):
    return x + y


@log
def subtract_example(x, y):
    return x - y


print(sum_example(5, 7))
print(subtract_example(5, y=7))

"""
Basicamente criamos um LOG que mostra informação sobre a execução das funções de SOMA e SUBTRAÇÃO
"""
