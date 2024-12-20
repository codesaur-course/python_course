# PACOTE EM PYTHON - LIDANDO COM MÓDULOS DE MESMO NOME

"""
Neste exemplo teremos módulos de mesmo nome importados de pacotes diferentes, isso gerará conflito. Para que o mesmo
não ocorra damos a um dos módulos um ALIAS, ou seja, um apelido, como vemos abaixo no IMPORT do package_2. Isso é
feito através da utilização do AS, assim podemos renomear o módulo em questão evitando o conflito
"""

from package_1 import module_1
from package_2 import module_1 as mod_sub


print(f"Soma: {module_1.sum(2, 3)}")
print(f"Subtração: {mod_sub.subtraction(5, 3)}")
