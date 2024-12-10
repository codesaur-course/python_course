# ÁREA DA CIRCUNFERÊNCIA COM APLICAÇÃO DE RETORNO

"""
Nos modelos anteriores do projeto apenas apresentávamos uma impressão dos valores, neste modelo atual iremos
aplicar o RETORNO dos valores como veremos no exemplo abaixo.
"""

from math import pi


circle = float(input("Informe o valor da circunferência: "))


def circle_radius(circle) -> float: # O TYPE HINT, o mesmo serve como uma documentação do tipo de valor retornado.
    computation = pi * circle ** 2
    return computation


radius = circle_radius(circle)
print(f"O raio da circunferência é de: {radius:.2f}")

"""
Agora que a função retorna um valor específico podemos usar o mesmo para outros fins como por exemplo calcular
outros valores que possam depender do valor do raio. podemos fazer isso apenas invocando a função a qual já
sabemos que trará um valor do tipo FLOAT.
"""

def radius_times_two():
    return circle_radius(circle) * 2


times_two = radius_times_two()
print(f"O valor do raio multiplicado por dois é de: {times_two:.4f}")

"""
Neste exemplo vemos como podemos multiplicar o valor do raio por dois criando uma função específica para isso e 
instanciando a função CIRCLE_RADIUS.
"""
