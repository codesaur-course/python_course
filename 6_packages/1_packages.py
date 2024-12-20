# TRABALHANDO COM PACOTES - IMPORTAÇÃO DE MÓDULO

"""
Uma vez tendo criado o pacote e o módulo podemos importar o módulo para ser utilizado em outro lugar do sistema
aplicando assim a sua função designada. Para isso primeiramente precisamos importar o módulo chamando o pacote
como na linha abaixo, isso é feito através da chamada FROM <NOME_DO_PACOTE> IMPORT <NOME_DO_MÓDULO>, como vemos no
exemplo abaixo
"""

from package_1 import module_1


print(type(module_1))
print(module_1.sum(5, 8))
