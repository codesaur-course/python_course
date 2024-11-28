# INTERPOLAÇÃO

"""
O processo de INTERPOLAÇÃO ocorre quando alteramos valores dentro da STRING, basicamente existe uma série de
caracteres especiais que aplicaremos dentro da mesma e o Python por sua vez interpretará que àqueles valores
deverão ser substituídos por outros valores.
"""

# Vamos começar criando duas variáveis em uma mesma linha

name, age = "Ralph", 40

"""
A primeira forma de INTERPOLAÇÃO fará uso dos seguintes caracteres, ( %s ) que serve para substituir elementos do tipo 
STRING e ( %d ) que serve para substituir INTEIROS
"""

"""
O símbolo de porcento ( % ) no meio indica a separação entre STRING e valores a serem substituídos com base nas
variáveirs pré-estabelecidas
"""
print("Nome: %s, Idade: %d" % (name, age))

"""
Porém, se ao invés do valor idade que é um número INTEIRO, tivéssemos algum outro que contivesse um número 
real ( FLOAT ) deveríamos uso o caracter ( %f ) como no exemplo abaixo.
"""

height = 1.80

"""
Por padrão ele usaria 6 casa decimais após o ponto ( . ), porém o .2 antes do f define o número de casas decimais como
sendo apenas 2 ( duas ). O mesmo também aplicará a prática de arredondamento caso seja necessário.
"""

print("Nome: %s, Altura: %.2f" % (name, height)) # Versão de formatação antiga

"""
Podemos fazer INTERPOLAÇÃO utilizando o módulo .format() contido no Python como veremos no exemplo abaixo.
"""

print("Nome: {}, Altura: {:.2f}".format(name, height)) # Versão adequada para Python < 3.6

"""
Nas versões mais recentes do Python usamos a INTERPOLAÇÃO por meio do que chamamos de F STRING, como veremos no 
exemplo abaixo.
"""

print(f"Nome: {name}, Altura: {height:.2f}") # Versão adequada para Python > 3.6
