# ESTRUTURA DE CONTROLE - SWITCH

"""
O SWITCH é uma estrutura de escolhas nativa de outras linguagens, porém a mesma não existe no Python, o que podemos
fazer é simular a mesma usando funcções e no caso abaixo a estrutura de um dicionário, vejamos abaixo.
"""

def get_week_day(day):
    days = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }

    return days.get(day, "** Dia Inválido! **")


def get_day():
    for day in range(0, 9):
        print(f"{day}: {get_week_day(day)}")


get_day()

"""
A partir do Python 3.10 foi implementado a estrutura MATCH | CASE cuja estrutura veremos no exemplo abaixo:
"""

def get_week_day_with_match(day):
    match day:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "DIA INVÁLIDO!"


def describe_day(day):
    days_names = get_week_day_with_match(day)

    if days_names == "DIA INVÁLIDO!":
        print(f"{day}: {days_names}")
        return

    if days_names in [1, 7]:
        print(f"{days_names}: FIM DE SEMANA!")

    else:
        print(f"{days_names}: DIA DE SEMANA!")


describe_day(2)
describe_day(7)
describe_day(9)

"""
Abaixo temos um exemplo sem o MTACH | CASE.
"""

def days_week(day):
    days = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }

    return days.get(day, '** DIA INVÁLIDO **') # Retorna o valor do dicionário


def week_or_weekend(day):
    day_name = days_week(day) # STRING nome do dia
    if day_name == "** DIA INVÁLIDO **":
        print(f"{day}: {day_name}")
        return

    if day in [1, 7]:
        print(f"{day_name}: FIM DE SEMANA!")

    else:
        print(f"{day_name}: DIA DE SEMANA!")


week_or_weekend(7)
week_or_weekend(2)
week_or_weekend(9)
