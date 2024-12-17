# CALLABLE COM PACKING | UNPACKING (*ARGS)

"""
Neste exercício criaremos uma função que deverá calcular o valor final de um produto através da CHAMADA ( callable )
de outras funções para calcular o valor final de um produto, este modelo usará a estrutura de PACKING e UNPACKING em
TUPLA (*args) com o uso de 1 ( um ) asterísco.
"""

def final_gross_price(price_param, tax_calculation_func, *params): # PACKING acontece no parâmetros
    """ Nesta linha acima definimos que o segundo parâmetro será uma função e a mesma receberá parâmetros variáveis """
    if callable(tax_calculation_func): # Testando SE a mesma é uma função passível de ser CHAMADA
        return price_param + price_param * tax_calculation_func(*params) # UNPACKING acontece no RETORNO da função


def tax_x(imported): # Parâmetro BOOLEANO ( True | False )
    return 0.22 if imported else 0.13


def tax_y(flammable, multiplication_factor=1): # Parâmetro BOOLEANO mais parâmetro NOMEADO
    return 0.11 * multiplication_factor if flammable else 0


gross_price = 134.98
final_price = final_gross_price(gross_price, tax_x, True)
final_price = final_gross_price(final_price, tax_y, True, 1.5)
print(f"Preço final de R${final_price:.2f}")
