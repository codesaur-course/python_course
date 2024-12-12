# LENDO ARQUIVOS .CSV - TRY | FINALLY ( TRATAMENTO DE EXCEÇÕES )

"""
Neste exemplo nós iremos abordar utrilizando o mesmo sistema de leitura de arquivos um tratamento de exceções ( erros ),
para isso iremos utilizar o TRY | FINALLY, como veremos no exemplo abaixo.
"""

try: # Tente executar este bloco
    file_reader = open("./csv_files_dir/people.csv")

    for file in file_reader:
        print("Nome: {}, Idade: {}".format(file.strip().split(','))) # Tirar o asterísco trará um erro

except IndexError: # Aqui validamos e erro
    pass # PASS indica um bloco vazio

finally: # Executa a última linha (fechamento) mesmo que dê erro
    print("FINALLY")
    file_reader.close() # Essa linha não será executada quando o erro surgir

"""
Mesmo usando o EXCEPT estando aqui aqui o objetivo é entender o tratamento com o uso do TRY | FINALLY
"""
