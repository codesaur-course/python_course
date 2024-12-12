# LENDO ARQUIVOS .CSV - COM STREAM

"""
Essa pode ser considerada uma segunda versão do exercício READ_CSV_FILE que criamos anteriormente, essa versão será
levemente otimizada utilizando STREAMING, que nada mais é do que a leitura sob demanda, na sua composição, como
veremos no exemplo abaixo.
"""

file_reader = open("./csv_files_dir/people.csv")
for file in file_reader:
    print("Nome: {}, Idade: {}".format(*file.split(','))) # Neste caso ele virá com quebra de linha
file_reader.close()

"""
O STREAMING neste caso acontece na linha 9, isso por que ao invés de armazenarmos uma quantidade X de dados
em uma variável o que estamos fazendo é uma leitura sob demanda como falamos anteriormente.
"""

"""
Se quiséssemos retirar a linhas da função anterior poderíamos usar o módulo .STRIP(), o que está função fará será
retirar espaços em branco no começo e no fim de uma STRING, como veremos no exemplo abaixo.
"""

file_reader_1 = open("./csv_files_dir/people.csv")
for file_1 in file_reader_1:
    print("Nome: {}, Idade: {}".format(*file_1.strip().split(','))) # O .STRIP() retira espaços em branco
file_reader_1.close()

"""
Seria possível fazemos de outro modo usando o END no final, mas neste caso não é a melhor opção mas vamos apresentar
o mesmo como exemplo abaixo.
"""

file_reader_2 = open("./csv_files_dir/people.csv")
for file_2 in file_reader_2:
    print("Nome: {}, Idade: {}".format(*file_2.split(',')), end="") # O END vazio retira as linhas em branco
