# CALLABLE COM PACKING | UNPACKING (*KWARGS)

"""
Neste exercício criaremos uma função que deverá calcular o valor final de um produto através da CHAMADA ( callable )
de outras funções para calcular o valor final de um produto, este modelo usará a estrutura de PACKING e UNPACKING em
DICIONÁRIO (**kwargs) com o uso de 2 ( dois ) asteríscos.
"""

def final_gross_price(price_param, tax_calculation_func, **params):
    """ Nesta linha acima definimos que o segundo parâmetro será uma função e a mesma receberá parâmetros variáveis """
    if callable(tax_calculation_func):
        return price_param + price_param * tax_calculation_func(**params)


def tax_x(imported):
    return 0.22 if imported else 0.13


def tax_y(flammable, multiplication_factor=1):
    return 0.11 * multiplication_factor if flammable else 0


gross_price = 134.98
final_price = final_gross_price(gross_price, tax_x, imported=True) # Após o **KWARGS uso apenas de parâmetros NOMEADO
final_price = final_gross_price(final_price, tax_y, flammable=True, multiplication_factor=1.5)
print(f"Preço final de R${final_price:.2f}")

"""
Basicamente neste formato estou FORÇANDO a explicitude dos valores ao utilizar **KWARGS para realização do UNPACKING
"""
