# ESTRUTURA DE REPETIÇÃO - FOR

"""
A estrutura de repetição em FOR diferentemente do WHILE, serve quando quando temos uma quantidade determinada de
repetições como o range de uma lista, um conjunto, entre outros. Como veremos nos exemplos abaixo.
"""

for i in range(1, 11): #  Lembrando que aqui estabelecemos de 1 à 10 sendo que o último valor, neste caso 11, não virá
    print(f"i = {i}")

for j in range(10): # Neste caso ele entende que fará 10 repetições, partindo do 0 e terminando antes do 10
    print(f"j = {j}")

"""
Assim como falamos anteriormente, o loop FOR pode percorrer uma série de estruturas de dados, como STRINGS, LISTAS,
CONJUNTOS, entre outros. Abaixo teremos alguns exemplos.
"""

word = "paralelepípedo"
for letter in word:
    print(letter, end=',')
print("Fim")

# Por padrão ele quebraria as linhas, porém o END faz com que o fechamento de cada letra seja uma vírgula.

"""
Abaixo dois exemplos de como percorrer ( ITERAR ) uma lista com uso do FOR
"""

list_example = ["Rafaela", "Pedro", "Renato", "Maria"]
for name in list_example:
    print(name)

for position, name in enumerate(list_example):
    print(f"{position + 1}", "- " + name) # Aqui estamos enmerando os itens mudando apenas o primeiro índice para 1

"""
Abaixo faremos o exemplo da ITERAÇÃO usando uma TUPLA
"""

week_days = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
for day in week_days:
    print(f"Hoje é {day}")

"""
Abaixo teremos dois exemplos de ITERAÇÃO usando um CONJUNTO ( SET )
"""

for letter in set("Ralph Santos Souza"):
    print(letter) # Lembrando apenas que um CONJUNTO deste modo não garante a ordenação das letras
print(" ")

set_example = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
for number in set_example:
    print(number) # Deste modo teremos uma ordenação dos valores
print(" ")

for number_set in {1, 2, 3, 4, 5}:
    print(number_set) # Deste modo também há ordenação
print(" ")

"""
Vale ressaltar que o que está acontecendo nos exemplos acima não é uma garantia de ordenação, mesmo por quê um 
CONJUNTO por natureza não garante ordenação, como dissemos anteriormente mas, como criamos o mesmo com uma ordem
específica o mesmo imprime deste modo.
"""

"""
Abaixo teremos alguns exemplos de como fazer a ITERAÇÃO usando FOR dentro de um dicionário.
"""

product = {
    "name": "CANETA",
    "price": 1.99,
    "imported": True,
    "stock": 793
}

for key in product:
    print(key) # Neste exemplo estamos adquirindo as CHAVES do produto
print(" ")

for value in product.values():
    print(value) # Neste caso estamos adquirindo apenas os VALORES do produto usando o módulo .VALUES()
print(" ")

for key, value in product.items():
    print(key, "=", value) # E neste exemplo estamos adquirindo tanto CHAVE quanto VALOR do produto usando .ITEMS()
print(" ")
