# PACOTES EM PYTHON

"""
Este modelo de importação que vemos abaixo possui uma distinção do anterior, se analisarmos o módulo_2 veremos que
ao final do arquivo temos a seguinte declaração:

IF __NAME__ == "__MAIN__":
    MAIN()

Isso dirá ao Python a seguinte mensagem:

'Só execute este código quando se o arquivo for executado diretamente, e não quando ele for importado do módulo.'

Diferente do módulo 1 que não possui tal declaração e por esta razão quando importado, dará acesso total ao módulo
pelo simples fato de IMPORTÁ-LO.
"""

from package_1 import module_2


module_2.main()
