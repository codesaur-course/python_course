# DESAFIO 1

"""
Crie as variáveis salário e despesa, e descubra quantos porcento do seu salário está comprometido com as despesas.
"""

income = float(input("Qual o valor do seu salário: R$"))
outgoing = float(input("Qual o valor total das suas despesas: R$"))

percentage = (outgoing / income) * 100

print(f"O percentual do seu salário que está comprometido com suas despesas é de: {percentage:.2f}%")
