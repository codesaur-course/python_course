# CALLABLE OBJECTS - INSTÂNCIAS | CHAMADAS

"""
Neste exercício iremos executar chamadas de objetos ( funções ), esse processo também é conhecido como INSTANCIAÇÃO.
Este processo ficará mais claro quando abordarmos POO ( PROGRAMAÇÃO ORIENTADA À OBJETOS ).
"""

class Potency:
    """ Calcular a potência """
    def __init__(self, exponent): # CONSTRUCTOR
        self.exponent = exponent

    def __call__(self, base):
        return base ** self.exponent


square = Potency(2) # Aqui estamos passando o expoente para o CONSTRUCTOR
cubed = Potency(3)

if callable(square) and callable(cubed):
    print(f"3 ao quadrado = {square(3)}") # Aqui estamos passando a base para o SQUARE
    print(f"5 ao cubo = {cubed(5)}")
    print(f"4 ao quadrado = {Potency(4)(2)}") # Aqui passamos na primeira chamada o EXPOENTE e na segunda a BASE
