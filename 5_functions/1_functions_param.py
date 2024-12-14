# FUNÇÕES - TIPOS DE PARÂMETROS

"""
FUNÇÃO é uma sequêcnia de passos com o propósito de realizar alguma ação específica, elas podem ou não retornar algum
valor, do mesmo modo elas podem ou não depender de dados externos para realizar suas ações os quais são atribuidos as
FUNÇÕES por meio de parâmetros, uma função em Python é um objeto e um objeto pode se comportar como FUNÇÃO.
Dentro do Python nós temos dois tipos de parâmetro, são eles POSICIONAL ou NOMEADO.

Parâmetros POSICIONAIS são àqueles que nós já esperamos, por exemplo:

def func_example(p1, p2, p3):
                 ^   ^   ^
    func_example(2, 3, 4)

Como vimos no exemplo acima qaundo chamamos a FUNÇÃO devemos passar os parâmetros necessários neste caso 2 é o valor
correspondente ao P1, 3 é o valor correspondente ao parâmetro P2 e 4 será o valor correspondente ao parâmetro P3.

Parâmetros NOMEADOS são àqueles que recebem, como o próprio nome diz, uma NOMENCLATURA, como veremos no exemplo abaixo:

def func_example(p1, p2, p3):
                 ^
    func_example(2, p3=1, p2=2)

Neste caso estamos passando os parâmentros mas através da NOMENCLATURA definimos quais deles receberão quais valores.

Além disso existem dois tipos de parâmetros especiais que chamamos de *ARGS e **KWARGS, sendo que:

*ARGS     -> irá gerar uma TUPLA ( Tuple )
**KWARGS  -> irá gerar um DICIONÁRIO ( Dict )

Quando falamos do RETORNO de uma FUNÇÃO devemos entender que esse único RETORNO que o Python nos dá pode ser uma série
de coisas, como por exemplo:

- Uma TUPLA
- Uma LISTA
- Um DICIONÁRIO
- Um valor numérico
- Uma STRING
- Entre outros
"""

def tag_block(text, success_class='success'):
    return f"<div class='{success_class}'>{text}</div>"


assert tag_block("Incluído com sucesso!") == \
    "<div class='success'>Incluído com sucesso!</div>"

# assert tag_block("Impossível excluir!", 'error') == \
#     "<div class=error>Impossível excluir!</div>"

print(tag_block("bloco"))

"""
Neste exemplo acima temos um parâmetro opcional, (success_class='success'), isso que significa que se o parâmetro não
receber nenhum outro valor então por DEFAULT ele receberá a STRING "SUCCESS". Além disso, faremos um teste usando 
o módulo ASSERT, uma assertion basicamente verifica uma CONDIÇÃO e valida, se a mesma for VERDADEIRA ( True ) ele
passa, porém caso não seja VERDADEIRA ele trará um erro.
"""

def tag_block(text, success_class='success', inline=False):
    tag = 'span' if inline else 'div'
    return f"<{tag} class='{success_class}'>{text}</{tag}>"


print(tag_block("inline e classe", "info", True))
print(tag_block('inline', inline=True)) # uso do parâmetro NOMEADO ( inline=True )
print(tag_block(text='inline', inline=True)) # uso de dois ou mais parâmetros NOMEADOS
print(tag_block('falhou!', success_class='error')) # uso do parâmetro NOMEADO ( success_class='error' )
