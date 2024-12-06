# ESTRUTURAS DE CONTROLE - ( BREAK | CONTINUE )

"""
O BREAK e CONTINUE fazem parte das estruturas de controle e estão intimamente ligadas ao controle de FLUXO, por mais
que vejamos com maior frequência as mesmas sendo utilizados dentro de ESTRUTURAS CONDICIONAIS, elas não são limitadas
a apenas este tipo de uso, podemos usá-las também fora de estruturas condicionais como o loop WHILE criando assim,
por exemplo, uma QUEBRA no fluxo do loop impedindo que o mesmo repita suas ações infinitamente.
"""

# CONTINUE

for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)
print(" ")

"""
Neste exemplo acima temos uma ITERAÇÃO usando o LOOP FOR e o que estamos fazendo é: Os números contidos em uma faixa 
de 1 à 10 ( lembrando que ao usarmos o RANGE() o último número estipulado na faixa não será apresentado ) que dividos
por 2 forem iguais à 0 ( ZERO ) o CONTINUE irá interromper a repetição, sem sair do laço ( LOOP ),
seguindo para o próximo número, ou seja, ele interrompe imediatamente e segue para o próximo e deste modo apresentando
apenas os números ÍMPARES.
"""

# BREAK

for x in range(1, 11):
    if x == 5:
        break
    print(x)

"""
Já neste exemplo estamos usando o BREAK em uma ITERAÇÃO com FOR na mesma faixa da anterior, ou seja, entre 1 e 10.
Neste caso o que o BREAK fará é o seguinte, quando a CONDIÇÃO estabelecida ( X igual à 5 ) for verdadeira o FLUXO será
imediatamente interromido trazendo apenas os números dentro da faixa que vêem antes do 5.
"""
