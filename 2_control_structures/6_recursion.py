# RECURSIVIDADE

"""
RECURSIVIDADE nada mais é do a capacidade de um módulo chamar a si mesmo para solucionar um problema
"""

def create_print(maximum, current):
    if current >= maximum:
        return # O RETURN vazio encerra o processo sem retornar nada
    print(current)
    create_print(maximum, current + 1) # O valor máximo será sempre o mesmo enqto que o atual receberá + 1 a cada ciclo


create_print(10, 1) # Aqui o módulo irá repetir a si mesmo algumas vezes até atender a condição

"""
Um ponto importante quando falamos sobre RECURSIVIDADE é o estabelecimento da condição de parada.
"""
