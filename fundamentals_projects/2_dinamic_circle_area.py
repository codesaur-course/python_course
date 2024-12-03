# ÁREA DA CIRCUNFERÊNCIA DINÂMICA

"""
No projeto anterior estávamos aplicando a área da circunferência no código, porém e se quiséssemos que o valor fosse
inserido pelo usuário? É isso que veremos no exemplo abaixo
"""

from math import pi # Quando fazemos deste modo estamos apenas importando a função desejado dentro de math


radius = input("Informe o raio: ")

"""
Abaixo vemos que foi necessário converter o valor do raio para float, isso por quê sem a conversão o valor que seria 
retornado seria uma STRING, e um erro informando que não há como aplicar potência à uma STRING apareceria, por esta
razão convertemos o dado antes da operação ser executada.
"""

result = pi * float(radius) ** 2

print(f"O raio da circunferência é de: {result:.2f}")
