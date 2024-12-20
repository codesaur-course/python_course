# PACOTES EM PYTHON

"""
Apesar de acessarmos todos os módulos pela aplicação este não é um processo ou modelo padrão. No exemplo abaixo
veremos que essa função pode ser chamada através do módulo principal, porém para isso precisamos identificar o nome
do módulo e em seguida chamar a função como podemos ver especificamente nas linhas 13 e 14.
"""

def main():
    print(f"Rodando o main() no módulo {__name__}")


if __name__ == '__main__':
    main()

"""
Esse módulo será IMPORTADO no arquivo 2_packages.py
"""
