# LENDO ARQUIVO .CSV

"""
Nesta etapa iremos abordar a criação de arquivos utilizando Python, neste primeiro exercício iremos aprender a
trabalhar com arquivos no formato .CSV ( COMMA SEPARATED VALUES ).
"""

file_reader = open('./csv_files_dir/people.csv') # Abre o arquivo .csv
csv_data = file_reader.read() # Lê o arquivo .csv
file_reader.close() # Uma vez armazenada a informação em um variável eu fecho o arquivo

for person in csv_data.splitlines(): # .SPLITLINES() separa STRING em uma LISTA usando a quebra de linha como parâmetro
    data = person.split(',') # Para usar o F STRING foi preciso separar os itens da lista usando .SPLIT()
    print(f"Nome: {data[0]}, Idade: {data[1]}") # Pega cada um dos itens pelo seu índice


"""
Também seria possível fazer com .FORMAT() como veremos no exemplo abaixo.
"""

file_reader_1 = open("./csv_files_dir/people.csv")
csv_data_1 = file_reader_1.read()
file_reader_1.close()

for person_1 in csv_data_1.splitlines():
    print("Nome: {}, Idade: {}".format(*person_1.split(','))) # O asterísco extrai os dados da lista
