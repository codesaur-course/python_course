# LENDO ARQUIVOS .CSV COM WITH

"""
Neste exercício faremos a leitura do arquivo .CSV utilizando o WITH.
"""

with open("./csv_files_dir/people.csv") as file_reader: # Neste caso criamos um ALIAS para a abertura do arquivo
    for file in file_reader:
        print("Nome: {}, Idade: {}".format(*file.strip().split(',')))

if file_reader.closed: # Verificamos se o mesmo foi fechado
    print("Arquivo fechado com sucesso!")


"""
Fazer a leitura do arquivo com WITH tira a necessidade de fechamento manula do arquivo com .CLOSE(), isso porquê o
Python entende, através do uso de WITH, que o arquivo uma vez lido deve ser fechado, isso aumenta a segurança de 
funcionamento da função.
"""
