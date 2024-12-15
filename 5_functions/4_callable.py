# CALLABLE

"""
Lembrando que toda função é um objeto que possui certas características podemos dize que um CALLABLE, é um objeto que
que pode ser evocado, ou chamado. Basicamente quando usamos <NOME_DA_FUNÇÃO>() nós estamo chamando a mesma, no exemplo
abaixo chamamos as funções GOOD_MORNING | AFTERNOON | NIGHT() dentro de FUNC_EXECUTE() nós estamos chamando as mesmas
para que essas executem seus objetos, que neste caso nada mais é do que IMPRIMIR as frases BOM DIA | TARDE | NOITE.
"""

def func_execute(function_param):
    if callable(function_param): # O CALLABLE() apenas verifica se FUNC_PARAM é um CALLABLE ou não
        function_param()


def good_morning():
    print("BOM DIA!") # a falta de um valor explícito de RETORNO trará um None por DEFAULT


def good_afternoon():
    print("BOA TARDE!") # Aqui é só um PRINT sem RETORNO e gera NONE por padrão


def good_night():
    print("BOA NOITE!") # Aqui é só um PRINT sem RETORNO e gera NONE por padrão


print(func_execute(good_morning)) # Aqui estamos chamando GOOD_MORNING através da função FUNC_EXECUTE()
print(func_execute(good_afternoon))
print(func_execute(good_night))

"""
Basicamente o que estamos vendo aqui é a capacidade de se invocar uma função dentro de outra e assim trabalhar o
retorno da mesma, isso permite criar funções robustas como veremos mais à frente, além disso vale ressaltar que esta
é uma das características fundamentais do que chamamos de PROGRAMAÇÃO FUNCIONAL E PROCEDURAL.
"""
