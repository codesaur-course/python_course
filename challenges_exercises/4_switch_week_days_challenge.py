# DESAFIO 4

"""
Criar uma função que verifique os dias e determine se os mesmos são dias da semana ou se pertencem ao fim de semana
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
