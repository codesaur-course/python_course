# ESTRUTURA DE CONTROLES - CONDICIONAIS ( IF, ELIF, ELSE )

"""
Estruturas de controles, ou como são mais conhecidas, condicionais são estruturas que visam validar a veracidade de
uma condição no momento da execução de um bloco de código, elas são descritas como ( IF ) 'SE', ( ELIF ) 'SE, SENÃO',
( ELSE ) 'SENÃO'. Basicamente o que fazemos é validar SE ( IF ) uma condição está sendo atendida, caso ela não seja e
haja ainda mais de uma validação possível usamos o SE, SENÃO ( ELIF ), conduto se houver apenas uma última opção
disponível para validar usamos o SENÃO ( ELSE ) para fechar as condições. Nós veremos isso no exercício abaixo que irá
validar notas de alunos utilizando as condicionais.
"""

# REQUISITOS

# CONCEITOS    NOTAS

# A            DE 9.1 À 10.0
# A -          DE 8.1 À 9.0
# B            DE 7.1 À 8.0
# B -          DE 6.1 À 7.0
# C            DE 5.1 À 6.0
# C -          DE 4.1 À 5.0
# D            DE 3.1 À 4.0
# D -          DE 2.1 À 3.0
# E            DE 1.1 À 2.0
# E -          DE 0.0 À 1.0

# ALÉM DISSO PARA NOTAS > QUE 10 E MENORES QUE ZERO DEVEMOS IMPRIMIR O SEGUINTE TEXTO "NOTA INVÁLIDA!"


grade = float(input("Informe a nota do aluno: "))


def student_situation(grade) -> str:
    if grade > 10:
        return "NOTA INVÁLIDA!"
    elif grade >= 9.1:
        return "CONCEITO: A"
    elif grade >= 8.1:
        return "CONCEITO: A-"
    elif grade >= 7.1:
        return "CONCEITO: B"
    elif grade >= 6.1:
        return "CONCEITO: B-"
    elif grade >= 5.1:
        return "CONCEITO: C"
    elif grade >= 4.1:
        return "CONCEITO: C-"
    elif grade >= 3.1:
        return "CONCEITO: D"
    elif grade >= 2.1:
        return "CONCEITO: D-"
    elif grade >= 1.1:
        return "CONCEITO: E"
    elif grade >= 0:
        return "CONCEITO: E-"
    else:
        return "NOTA INVÁLIDA!"


result = student_situation(grade)
print(result)

"""
No exemplo acima acima validamos automaticamente tudo aquilo que for >= que a nota descrita, e apenas invalidamos 
quaisquer notas que sejam discrepantes das demais, porém se precisarmos validar valores distintos podemos fazer como 
no exemplo abaixo:
"""


age = int(input("Informe a idade: "))

def age_group(age):
    if 0 <= age < 18: # Aqui estamos comparando se IDADE for menor ou igual ( <= ) e também se é menor que ( < )
        return "MENOR DE IDADE"
    elif age in range(18, 64): # Aqui estamos estabelecendo uma faixa de comparação através do módulo range()
        return "ADULTO"
    elif age in range(65, 100):
        return "TERCEIRA IDADE"
    elif age > 100:
        return "CENTENÁRIO"
    else:
        return "IDADE INVÁLIDA!"


age_result = age_group(age)
print(f"A classificação para {age} anos de idade é de: {age_result}")
