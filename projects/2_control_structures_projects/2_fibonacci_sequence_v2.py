# PROJETO DE CÁLCULO DA SEQUÊNCIA FIBONACCI V2

def fibonacci(limit): # Nesta versão eu já preciso indicar um limite, por isso o parâmetro
    penultimate = 0
    last = 1

    print(f"{penultimate}, {last}", end=', ')

    while last < limit: # Se o último for menor que limit ele encerra
        next_one = penultimate + last
        print(next_one, end=', ')
        penultimate = last
        last = next_one


fibonacci(10000)
