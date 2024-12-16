#  PACKING NOMEADO

"""
Neste exercício veremos a construção de um PACKING NOMEADO utilizando 2 ( dois ) asteríscos para isso, e o resultado do
mesmo, diferentemente dos anteriores é que o RETORNO do mesmo será um DICIONÁRIO e não uma TUPLA, como veremos
abaixo.
"""

# PACKING
def result_f1(**podium):
    for position, pilot in podium.items():
        print(f"{position} -> {pilot}")


result_f1(
    first="L. Hamilton",
    second="M. Verstappen",
    third="S. Vettel"
)

"""
Este processo é o mesmo que acontece quando usamos o parâmetro opcional **KWARGS ( KEY WORD ARGUMENTS ). Este, assim
como o *ARGS serve para capturar um número variável de parâmetros além de trabalhar no processo de PACKING contudo, 
*ARGS transforma os parâmetros em uma LISTA enquanto que o **KWARGS trabalha com um número variável de parâmetros 
contendo CHAVE e VALOR, assim como um DICIONÁRIO.
"""

# UNPACKING
def result_f1_v2(first, second, third):
    print(f"1) {first}")
    print(f"2) {second}")
    print(f"3) {third}")


podium_v2 = {
    "first": "L. Hamilton",
    "second": "M. Verstappen",
    "third": "S. Vettel"
}

result_f1_v2(**podium_v2)
