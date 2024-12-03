# ÁREA DA CIRCUNFERÊNCIA UTILIZANDO FUNÇÕES

"""
Aqui nós iremos escrever uma função específica para calcular a área de um círculo
"""

from math import pi

"""
Na função abaixo veremos que não há parâmetros, isso por quê a função possui todos os parâmetros necessários para o 
seu funcionamento dentro dela mesma, porém se a mesma precisar de valores externos então esses parâmetros deverão ser 
estipulados para que haja o seu funcionamento como veremo no exemplo 2 abaixo.
"""

def circle():
    radius = float(input("Informe o valor do raio da circunferência: "))
    result = pi * radius ** 2
    print(f"A área da circinferência é de: {result:.2f}")


circle() # Sempre que quisermos testar precisamos trazer a chamada da função como estamos fazendo aqui.


"""
Exemplo 2
"""

new_radius = float(input("Informe o valor do raio da circunferência: "))


def new_circle(new_radius):
    new_result = pi * new_radius ** 2
    print(f"A área da circinferência é de: {new_result:.4f}")


new_circle(new_radius)
