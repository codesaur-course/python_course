# CÁLCULO DO RAIO DA CIRCUNFERÊNCIA

pi = 3.1415
radius = 15.3

result = pi * radius ** 2

print(f"{result:.4f}")

"""
Quando trabalhamos com projetos específicos é comum nos depararmos com problemas comuns a todos os programadores,
o fato de problemas comuns existirem é bom pelo seguinte, a necessidade do grupo faz com que melhorias sejam
desenvolvidas para facilitar o dia-a-dia, por esta razão criam-se bibliotecas com funções específicas e aqui nós iremos
importar e usar uma delas, a biblioteca Math, como podemos ver abaixo.
"""

import math # Importando a biblioteca matemática

print("π = ", math.pi)

# Isso permite que nosso pcódigo seja mais limpo e de fácil manutenção, como veremos abaixo.

new_radius = 15.3

new_result = math.pi * new_radius ** 2

print(f"O raio da circunferência é de: {new_result:.2f}")
