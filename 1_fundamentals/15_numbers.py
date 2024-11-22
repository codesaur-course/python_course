# TIPOS NUMÉRICOS

"""
Tipos numéricos nós já vimos o INT ( inteiro ) e o FLOAT ( ponto flutuante / número real ), se por acaso acessarmos o
SHELL do Python e digitarmos dir() e o tipo, ou então como veremos no exemplo abaixo veremos todos os módulos builtins
atrelados àquela função.
"""

print(dir(int))
print(dir(float))

"""
Também podemos falar sobre os números decimais, quando queremos um maior nível de precisão no nosso processo, para
isso precisamos importar a biblioteca específica que lida com decimais, visto que a mesma não é uma função builtin
e juntamente importaremos a biblioteca getcontext pata ajustarmos o nível de precisão.
"""

from decimal import Decimal, getcontext

decimal = Decimal(1) / Decimal(7)
print(decimal)

"""
Utilizando o getcontext() podemos usar o prec e definir o valor de casas decimais antes de executar a função
"""

getcontext().prec = 4
decimal_result = Decimal(1) / Decimal(7)
print(decimal_result)

"""
Ao executarmos o dir() para a função Decimal() veremos todas as funções que podemos usar para enriquecer a mesma
"""

print(dir(Decimal))
