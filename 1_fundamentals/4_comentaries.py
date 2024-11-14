# COMENTÁRIOS

"""
Criar comentários em Python é simples como podemos ver nesses textos e os métodos já estão sendo apresentados aqui
por exemplo, comentário de uma linha são feitos com uso da hashtag ( # ) com tudo o uso de aspas triplas, como estamos
usando aqui nesta explicação, permite a você escrever comentários com múltiplas linhas.
O uso de comentário em códigos Python deve ser feito com certa cautela, comentários demais podem poluir o
código, além disso é uma convenção na programação que códigos bem escritos dispensam comentários, assim sendo,
use-os apenas quando forem indispensáveis.
Vamos aos exemplos abaixo:
"""

# EXEMPLO DE DESCRIÇÃO COM UMA LINHA

# Minhas Variáveis
salario = 3450.45
despesas = 2456.02

resultado = salario - despesas

# EXEMPLO DE DESCRIÇÃO COM MÚLTIPLAS LINHAS

"""
A ideia é calcular o quanto vai sobrar 
no final do mês.
"""

# Aspas duplas ou simples usadas 3 (três) vezes são válidas na criação de comentários de múltiplas linhas

'''
A ideia é calcular o quanto vai sobrar 
no final do mês.
'''

print(f"O remanescente do seu salário este mês é de: {resultado:.2f}")
print("FIM") # Comentários também cabem após um bloco de código

"""
Vale ressaltar que comentários são trechos que ao executarmos nossa aplicação são ignorados pelo sistema
"""
