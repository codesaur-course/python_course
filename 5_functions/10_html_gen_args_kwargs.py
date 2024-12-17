# GERADOR HTML COM PARÂMETROS POSICIONAIS E NOMEADOS ( PACKING | UNPACKING )

"""
Neste exercício iremos aprimorar nosso gerador HTML que demos início no exercício 5, porém desta vez iremos passar
argumentos POSCIONAIS ( *ARGS ) e argumentos NOMEADOS ( **KWARGS ).
"""

attrib_block = ("block_accesskey", "block_id",)
attrib_ul = ("ul_id", "ul_style",)

def get_attrib(informed, supported):
    return ' '.join(f"{k.split('_')[-1]}='{v}'" for k, v in informed.items() if k in supported)

"""
O .join() serve para juntar uma sequência de STRINGS e neste caso definimos antes de mais nada o DELIMITADOR antes do
mesmo, no exemplo acima um STRING com um caracter VAZIO. O .join() acontece no fim do processo, por exemplo primeiro 
ele executa o LOOP do DICIONÁRIO ( informed.items() ) depois verifica a condição IF para ver se a CHAVE encontra-se
dentro do SUPPORTED, neste caso as TUPLAS acima, depois executa o .split() usando como parâmetro o UNDELINE ( _ ) 
de cada CHAVE e pegando o último valor ( [-1] ), depois forma a STRING com CHAVE = VALOR e só então faz o .join()
resultando em algo assim:
( accesskey='m', id='conteúdo' )
Removendo a palavra BLOCK de cada uma das CHAVES.
"""


def block_tag_generator(text_param, *args, class_param='success', inline_param=False, **new_attrib):
    tag = 'span' if inline_param else 'div'
    html = text_param if not callable(text_param) else text_param(*args, **new_attrib)
    attrib = get_attrib(new_attrib, attrib_block) # Aqui eu passo o INFORMED e o SUPPORTED nesta ordem
    return f"<{tag} {attrib} class={class_param}>{html}</{tag}>"


def tag_list_generator(*items, **new_attrib):
    list_model = ''.join(f"<li>{item}</li>" for item in items)
    return f"<ul {get_attrib(new_attrib, attrib_ul)}>{list_model}</ul>" # Passando o INFORMED e o SUPPORTED nesta ordem

"""
Em ambas funções block_tag_generator() e na tag_list_generator() estou passando os parâmetros INFORMED e SUPPORTED
exatamente nesta sequência, onde SUPPORTED vem das TUPLAS acima e o INFORMED vem dos parâmetros NOMEADOS no print()
abaixo, sendo que a função get_attrib() receberá ambos mas é são as outras duas funções quem farão a leitura do tipo
de atributos isso por quê quando especifico em get_attrib() que a primeira é **new_attrib ele trará o DICIONÁRIO 
enquanto que attrib_block é uma TUPLA (linha 18). **new_attrib passa a ser equivalente a INFORMED em get_attrib()
"""

print(block_tag_generator(tag_list_generator, "Sábado", "Domingo", class_param="info", inline_param=True))
print(block_tag_generator(
    tag_list_generator,
    "Item 1",
    "Item 2",
    class_param="info",
    block_accesskey="m",
    block_id="conteúdo",
    ul_id="lista"
    )
)