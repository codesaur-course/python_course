# SIMULANDO SWITCH

"""
Neste exercício iremos fazer uma simulação utilizando SWITCH
"""

def get_day_type(day):
    days = {
        (1, 7): "FIM DE SEMANA",
        tuple(range(2, 7)): "DIA DE SEMANA",
    }

    chosen_day = (day_type for numbers, day_type in days.items() if day in numbers)
    return next(chosen_day, "** DIA INVÁLIDO! **")


for day in range(0, 9):
    print(f"{day}: {get_day_type(day)}")
