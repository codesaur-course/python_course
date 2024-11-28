# ESTRUTURAS DE DADOS - LISTAS

"""
Listas são estruturas de dados mutáveis e sua síntaxe se dá através da aplicação de colchetes ( [] )
"""

list_example = []
print(type(list_example))
print(dir(list_example))

"""
Caso tenhamos a necessidade de sabermos o tamanho da lista basta utilizarmos o módulo len(), como no exemplo abaixo.
"""

print(len(list_example))

"""
Para adicionarmos dados a lista podemos utilizar o módulo .append(), como no exemplo abaixo.
"""

list_example.append(1)
list_example.append(5)

print(list_example)
print(len(list_example))

"""
Agora vamos criar uma nova lista contendo dados distintos.
"""

new_list = [1, 5, "Ana", "Bia"]
print(new_list)
print(len(new_list))

"""
Ao trabalharmos com lista também é possível remover valores através da utilização do módulo .delete(), como no 
exemplo abaixo.
"""

new_list.remove(5)
print(new_list)

"""
Podemos inverter uma lista com o módulo .reverse() como no exemplo abaixo, porém diferente de STRINGS a lista é um
elemento mutável, ou seja, essa reversão da variável para que seja aplicada.
"""

new_list.reverse()
print(new_list)

"""
No caso das LISTAS, os elementos contido nela poderãos ser mapeados através de seu respectivos índices, como veremos 
no exemplo abaixo.
"""

index_list = [1, 5, "Rebecca", "Gustavo", 3.1415]
print(index_list)

print(index_list.index("Gustavo")) # Neste caso estamos verificando a qual índice pertence a STRING "Gustavo"

print(index_list[2]) # Neste caso acessamos o valor por meio do índice

"""
Também podemos usar operadores MEMBRO ao analisarmos os dados contidos na LISTA, como no exemplo abaixo.
"""

print(1 in index_list)
print("Rebecca" in index_list)
print("Gustavo" not in index_list)

"""
Também podemos acessar os dados contidos na LISTA partindo do último para o primeiro, como no exemplo abaixo.
"""

print(index_list[-1])

"""
Também é possível acessar valores dentro de uma LISTA com base em certos intervalos, ou RANGES, como veremos no 
exemplo abaixo.
"""

range_list = ["Ana", "Lia", "Rui", "Paulo", "Dani"]

print(range_list[1:3]) # Lembrando que o último índice não entra na resposta

print(range_list[1:-1]) # Aqui vai do um ( 1 ) até menos um ( -1 ) sem incluir o menos um

print(range_list[1:]) # Aqui vai do um ( 1 ) até o último

print(range_list[:-1]) # Aqui vai do zero ( 0 ) até menos um ( -1 ) sem incluir o menos um

print(range_list[:]) # Aqui vai do começo ao fim, é o mesmo que só printar a lista

print(range_list[::2]) # Aqui acessamos a lista inteira mas de duas em duas casas

print(range_list[::-1]) # Aqui nós invertemos a LISTA, o que poderia ser feito com o módulo .reverse()

del range_list[2] # Aqui estamos excluíndo um item pelo seu índice
print(range_list)
