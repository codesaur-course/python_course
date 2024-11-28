# DICIONÁRIOS

"""
A principal diferença que veremos na estrutura de dicionários será o fato de a mesma utilizar CHAVE - VALOR,
a mesma pode usar índices, normalmente isso ocorre com o uso de STRINGS
"""
from os import pipe2

person = {
    "name": "Ralph dos Santos Souza",
    "age": 39,
    "courses": [
        "Inglês",
        "Português"
    ]
}

print(type(person))
print(person)

"""
Podemos ver mais informações sobre o DICIONÁRIO através o módulo dir() como no exemplo abaixo.
"""

print(dir(dict))

"""
Para acessar os valores podemos usar as chaves como no exemplo abaixo.
"""

print(person["name"])
print(person["age"])
print(person["courses"])

"""
E no caso do campo cursos, já que o mesmo é uma LISTA podemos acessar cada valor pelo seu índice, 
como no exemplo abaixo.
"""

print(person["courses"][0])
print(person["courses"][1])

"""
Podemos identificar separadamente CHAVES e VALORES se usarmos os módulo keys() e values() como no exemplo abaixo.
"""

print(person.keys())
print(person.values())

"""
Porém se usarmos o módulo items() teremos os itens contendo CHAVE e VALOR como no exemplo abaixo.
"""

print(person.items())

"""
Também podemos pegar VALORES específicos pela CHAVE, como no exemplo abaixo
"""

print(person.get("name"))

"""
Caso eu chame uma CHAVE inexistente eu posso definir um valor default de resposta, com no exemplo abaixo.
"""

print(person.get("tags", [])) # Neste caso ele trará uma lista vazia
