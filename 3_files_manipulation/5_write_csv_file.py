# ESCREVENDO ARQUIVOS .CSV

"""
Neste exercício iremos ver como podemos criar arquivos .CSV também com WITH.
"""

with open("./csv_files_dir/people.csv") as file_reader:
    with open("people.txt", "w") as final_file: # O "w" dentro do OPEN() define o modo de ESCRITA ( WRITE )
        for single_file in file_reader:
            person = single_file.strip().split(',')
            print("Nome: {}, Idade: {}".format(*person), file=final_file)

if file_reader.closed:
    print("Arquivo fechado com sucesso!")

if final_file.closed:
    print("Arquivo final fechado!")
