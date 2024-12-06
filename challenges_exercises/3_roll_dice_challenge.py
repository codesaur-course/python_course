# DESAFIO 3

"""
Etapas do desafio:
1 - Criar uma funcão para sortear um número aleatoriamente um número de 1 a 6
2 - Criar um FOR com range() entre 1 e 6
3 - Analisar, se for ímpar CONTINUE
4 - Se o número for par e igual ao sorteado imprimir 'VOCÊ ACERTOU!'
5 - Se não acertar chamar um ELSE com o seguinte retorno 'VOCÊ NÃO ACERTOU!'
"""

from random import randint


def roll_dices():
    return randint(1, 6)


def game():
    random_number = roll_dices() # Sorteia o número aleatório uma vez
    number = int(input("CHUTE um número de 1 à 6: "))

    for i in range(1, 7): # Loop de 1 a 6
        if i % 2 == 1: # Se for ímpar contínua
            continue

        if i == random_number and i == number: # Se for par e igual ao sorteado
            print(f"Você ACERTOU!")
            break # Sai do loop imediatamente

    else: print("Você NÃO ACERTOU!") # Executado somente quando o LOOP terminar sem BREAK


game()
