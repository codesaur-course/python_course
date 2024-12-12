# DESAFIO 5

"""
Neste desafio o faremos será ler um arquivo em um determinada URL e iremos imprimir duas colunas específicas deste
arquivo o qual contêm informações de cidades coletadas pelo IBGE
"""

import csv

from urllib import request


def read(url):
    with request.urlopen(url) as income_file:
        print("Baixando o arquivo .CSV...")

        data = income_file.read().decode('latin1')
        print("Download completo!")

        for city in csv.reader(data.splitlines()):
            print(f"{city[8]}: {city[3]}")


read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

"""
O R significa RAW, neste caso analisa a URL sem alterar os caracteres especiais
"""
