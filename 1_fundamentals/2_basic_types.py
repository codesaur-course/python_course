# TIPOS BÁSICOS

"""
Estrutura de dados é basicamente a forma como você armazena e processa os dados no seus sistema e/ou aplicação.
Existem alguns tipos básicos que iremos tratar aqui, como por exemplo:
"""

# BOOLEANOS -  (VERDADEIRO E FALSO)
"""
Bool ou Booleanos se resumem a valores VERDADEIROS e FALSOS, eles atuam através de uma tabela VERDADE que testa
condições específicas as quais veremos mais para a frente. Sempre escrevemos ambos com a primeira letra maiúscula,
de outro modo o Python não processará.
"""

print(True)
print(False)

# NÚMEROS INTEIROS
"""
São números inteiros número que não possuem quebra por ponto (.) e/ou vírgula (,), dados como ano e idade são bons 
exemplos de números inteiros.
"""

print(1 + 3)

# FLOAT (NÚMEROS REAIS OU PONTO FLUTUANTE)
"""
São considerados números reais (Ponto Flutuante), àqueles que possuem quebra por ponto (.), e/ou vírgula (,).
Como Python usa como base a língua inglesa devemos considerar ponto (.) sempre que trabalharmos com  dados tipo FLOAT.
"""

print(2.5 + 3.7)

# STRINGS (TEXTOS)
"""
STRINGS são os textos, para que o Python reconheça os mesmos usamos as aspas, podendo ser duplas (") ou simples (').
Tudo que estiver registrado entre aspas passa a ser interpretado como texto.
"""

print("Aqui eu escrevo meus textos!")
print('Com aspas simples também funciona!')

# CONCATENAÇÃO DE DADOS
"""Concatenação """

print("Você é " + 3 * "muito " + "legal!!!")

# LISTAS
"""
Listas em Python são grupos de dados mutáveis que são mapeados por índices que tem início no 0 (zero), ou seja, 
o primeiro dado de uma lista possui índice zero (0), o segundo possui índice um (1), o terceiro possui índice dois (2)
e assim por diante, em uma lista podemos adicionar novos dados, alterar ou remover, e sua sintaxe é determinada
através do uso de colchetes [] 
"""
print([1, 2, 3, "Carro", "Osso", "Cachorro", True, False])

# DICIONÁRIOS
"""
Dicionários assim como listas são grupos de dados, porém a principal diferença neste caso está na forma como 
consumimos os dados, um dicionário fucniona com a estrutura de chave e valor, e neste caso teremos acesso aos 
dados sempres que consultarmos uma chave, na sintaxe os dcionários são criados através do uso de chaves {}, onde o 
primeiro dado é a chave e o segundo o valor da chave: '{"chave": "valor"}'.
"""

print({"nome": "Ralph", "sobrenome": "Souza", "idade": 39, "gênero": "Masculino"})

# TUPLAS
"""
Tuplas são grupos imutáveis de dados e sua sintaxe é constituída pelo uso de parênteses (). Podemos consumir os dados
por meio de índices, por desempacotamento, por iteração, assim como fazemos com uma lista por exemplo.
"""

print(("Ralph", "Souza", 39, "Masculino"))

# NONE (VAZIO)
"""
NONE é utilizado para expressar a ausência de valores, um exemplo simples é quando queremos que uma variável 
esteja por default, vazia, para que venha a receber novos dados posterimente. 
"""

print(None)
