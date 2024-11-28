# DICIONÁRIOS

"""
A principal diferença que veremos na estrutura de dicionários será o fato de a mesma utilizar CHAVE - VALOR,
a mesma pode usar índices, normalmente isso ocorre com o uso de STRINGS
"""

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

"""
Diferente das TUPLAS os DICIONÁRIOS são mutáveis, podemos através das chaves alterar seus valores ou adicionar
novos valores como veremos no exemplo abaixo.
"""

new_person = {
    "name": "Ralph dos Santos Souza",
    "age": 39,
    "courses": [
        "React",
        "Python",
        "Javascript"
    ]
}

print(new_person)

new_person["age"] = 40
print(new_person)

new_person["courses"].append("JAVA")
print(new_person)

"""
Podemos fazer a exclusão de valores de um dicionário utilizando o módulo .pop(), como no exemplo abaixo.
"""

new_person.pop("age")
print(new_person)

"""
Do mesmo modo podemos atualizar os valores dentro do dicionário utilizando o módulo .update(), como no exemplo abaixo.
"""

new_person.update({"age": 40, "gender": "Masculino"})
print(new_person)

"""
Se utilizarmos o módulo .clear() iremos limpar totalmente o nosso dicionário, como no exemplo abaixo.
"""

new_person.clear()
print(new_person)
