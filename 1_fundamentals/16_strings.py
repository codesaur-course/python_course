# TIPO STRING

"""
STRINGS são textos convencionais, ou seja, o tipo de dado em texto. Assim como INT, FLOAT e os demais que temos visto
anteriormente, se usarmos o módulo dir() poderemos ver todas as funções builtins que compentem ao módulo STR, como
veremos abaixo.
"""
from cmath import phase

print(dir(str))

"""
Sempre que declaramos uma STRING usamos aspas duplas ( " ) ou aspas simples ( ' ), e tudo que estiver contido entre elas
será considerado como texto ( STRING ) pelo Python. Nós teremos alguns exemplos abaixo para estes casos também.
"""

nome = "Ralph Santos Souza"
print(nome)

"""
A STRING é constituída de indices assim como vimos nas listas, ou seja, cada caractere dentro do texto possui um 
índice que permite mapeá-lo, e assim como as listas o primeiro índice é sempre zero ( 0 ), o segundo um ( 1 ) e assim
por diante, e podemos adquiri-los como no exemplo abaixo.
"""

print(nome[1])

"""
Vale ressaltar que a STRING é imutável, ou seja, não há como fazer alterações na mesma. O que podemos fazer é alterar o
valor da variável que guarda a STRING.
"""

"""
Também conseguimos acessar os índices da STRING em uma escala decrescente, da última letra para a primeira como podemos 
ver no exemplo abaixo. A única diferença é que o primeiro sempre será -1.
"""

print(nome[-4])

"""
Se eu quiser usar um RANGE e acessar a STRING a partir de um índice específico eu uso dois-pontos ( : ) para isso
como no exemplo abaixo.
"""

print(nome[5:])

"""
Também é possível fazer o mesmo da direta para a esquerda como no exemplo abaixo.
"""

print(nome[-5:])

"""
Se eu quiser partir do início e ir até um índice específico também farei uso de dois-pontos ( : ), porém o mesmo virá
antes de índice desejado, como no exemplo abaixo. Porém vale ressaltar que neste caso o último índice não entrará
na resposta, ou seja, se eu coloco [-4] como índice minha resposta não será RALPH mas sim RALP.
"""

print(nome[:5])

"""
Se eu quiser algum valor entre índices basta usar o dois-pontos ( : ) entre os índices, lembrando que como no exemplo 
anterior, o último valor não será contado na resposta, como no exemplo abaixo.
"""

print(nome[3:8])

"""
Se eu quiser pegar casas específicas posso estabelecer um STEP, basta usar o dois-pontos ( : ) duas vezes ( :: ) e 
definir de quantas em quantas casas eu desejo receber, como veremos no exemplo abaixo.
"""
numbers = "1234567890"
print(numbers[::2])

"""
Também posso definir de onde desejo partir como no exemplo abaixo.
"""

print(numbers[1::2])

"""
Também é possível fazer a inversão da STRING usando o negativo ( - ) como no exemplo abaixo.
"""

print(nome[::-1])
print(numbers[::-1])

"""
Ou até mesmo pegar casa específicas da direita para a esquerda como no exemplo abaixo.
"""

print(numbers[::-2])

"""
Também podemos usar operadores membros para analisar uma STRING como veremos no exemplo abaixo, porém vale ressaltar
que quando executamos esse processo a diferença entre letras maiúsculas e minúsculas será considerada.
"""

phrase =  "Python é uma linguagem dinâmica!"
print("Py" in phrase)
print("py" not in phrase)

"""
Se quisermos saber o número de caracteres na frase usamos o módulo len() como no exemplo abaixo.
"""

print(len(phrase))

"""
Para converter tudo para minúsculo basta usarmos o módulo lower() como no exemplo abaixo.
"""

print(phrase.lower())

"""
O mesmo acontece para maiúsculo se usarmos o módulo upper() como no exemplo abaixo. Porém vale ressaltar que a frase
não mudou, ou seja, se printarmos apenas a variável phrase teremos a frase de sempre. Para mudar precisamos mudar o 
valor da variável.
"""

print(phrase.upper())

phrase = phrase.upper()
print(phrase)

"""
Se eu quiser quebra a frase por alguma razão farei uso do módulo split(). Contudo se eu não definir um valor padrão de
por onde eu desejo quebrar o mesmo usará os espaços em branco, como no exemplo abaixo.
"""

print(phrase.split())
