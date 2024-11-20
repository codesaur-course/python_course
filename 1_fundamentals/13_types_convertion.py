# CONVERSÃO DE TIPOS

"""
O Python trabalha, como já dito no ZEN OF PYTHON, com valores explicitos, já que explicito é melhor do que
implicito, ou seja, eu posso converter valores desde que eu deixe claro minhas intenções, diferente de outras
linguagens que podem presumir certas ações, como veremos no exemplo abaixo:
"""

a = 2
b = "3"

print(type(a))
print(type(b))

"""
O adendo acima irá mostra de maneira clara que os tipos dos valores de A são diferentes de B, mas podemos fazer a 
conversão dos mesmos da seguinte forma:
"""

print(a + int(b))
print(str(a) + b)

"""
Existem outros métodos viáveis mas aqui já da para entendermos que na primeira opção A é um inteiro e B uma string 
(texto) assim sendo para que possa fazer um cálculo dos valores eu precisei explicitar para o Python que B = "3"
deveria ser interpretado como um número inteiro, recebendo deste modo o valor 5 como resultado. Já na segunda eu 
explicitei que A = 2 deveria ser interpretado como texto assim sendo o que ocorre é uma concatenação o que me 
retornará o valor "23"
"""
