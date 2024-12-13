# GENERATORS

"""
GENERATORS diferentemente da LIST COMPREHENSION utiliza na sua base PARÊNTESES, além disso o GENERATOR diferentemente do
LIST COMPREHENSION irá gerar os valores por demanda, enquanto que o LIST COMPREHENSION gera a lista completa, isso
torna o uso do GENERATOR mais leve, em questões de processamento.
"""

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator)) # Saída será 0
print(next(generator)) # Saída será 4
print(next(generator)) # Saída será 16
print(next(generator)) # Saída será 36
print(next(generator)) # Saída será 64
print(next(generator)) # ERRO!

"""
Como vemos no exemplo acima utilizamos o NEXT() para gerar os próximos valores quando se tratando do uso de GENERATORS
"""
