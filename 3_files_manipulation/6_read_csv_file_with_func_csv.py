# LENDO ARQUIVOS .CSV COM USO DE MÓDULO CSV

"""
Neste exercício iremos aprender como fazer a leitura de arquivos .CSV com a utlização do módulo CSV() nativo do Python
"""

import csv


with open("./csv_files_dir/people.csv") as file_read:
    for person in csv.reader(file_read): # Neste processo ele já faz o STRIP e o SPLIT por ser um CSV
        print("Nome: {}, Idade: {}".format(*person))
