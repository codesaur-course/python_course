# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V1

def fibonacci():
    penultimate = 0
    last = 1

    print(f"{penultimate}, {last}", end=", ")

    while True:
        next  = penultimate + last
        print(next, end=', ')
        penultimate = last
        last = next


fibonacci()
