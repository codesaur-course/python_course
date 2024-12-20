# PACOTES EM PYTHON - IMPORTAÇÃO DIRETA DA FUNÇÃO

"""
Neste exercício veremos como aplicar a importação direta da função sem necessariamente importarmos o módulo
"""

from package_1.module_1 import sum
from package_2.module_1 import subtraction


print(f"Soma: {sum(3, 2)}")
print(f"Subtração: {subtraction(5, 3)}")
