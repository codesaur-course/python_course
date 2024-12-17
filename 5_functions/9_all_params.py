# TODOS OS PARÂMETROS - *ARGS | **KWARGS

"""
Neste exercício iremos criar uma função que receber ambos os tipos de parâmetros, sejam eles POSICIONAIS
( *ARGS | TUPLA ) ou NOMEADOS ( **KWARGS | DICIONÁRIO )
"""

def all_params(*args, **kwargs):
    print(f"ARGS: {args}")
    print(f"KWARGS: {kwargs}")

all_params("a", "b", "c")
all_params(1, 2, 3, cool=True, value=12.99)
all_params("Ana", False, [1, 2, 3], size="M", fragile=False)
