# PARÂMETROS OPCIONAIS E (UN)PACKING

"""
Neste exercício de geração de HTML iremos prosseguir com a explicação do PACKING e do UNPACKING além dos parâmetros
OPCIONAIS. Para isso iremos criar um GENERATOR como fizemos em exercícios anteriores, mas antes vale ressaltar o que é
um GENERATOR.
GENERATORs são funções especiais que RETORNAM um OBJETO ITERADOR, onde os valores são 'gerados' sob demanda, ao invés
de serem calculados e armazenados todos juntos de uma só vez.
"""

def block_tag_generator(text_param, *args, class_param='success', inline_param=False):
    """ Vale ressaltar que a ordem do posicionamento do *ARGS afeta o resultado """
    tag = 'span' if inline_param else 'div'
    html = text_param if not callable(text_param) else text_param(*args)
    return f"<{tag} class={class_param}>{html}</{tag}>"


def tag_list_generator(*items):
    list_model = ''.join(f"<li>{item}</li>" for item in items)
    return f"<ul>{list_model}</ul>"

print(block_tag_generator(tag_list_generator, "Sábado", "Domingo", class_param="info", inline_param=True))

"""
Outro ponto importante que devemos levar em consideração é, quando usamos parâmetros OPCIONIAS como é o caso do *ARGS
todos os outros parâmetros que vierem a seguir deverão ser NOMEADOS, não poderemos usar parâmtros POSICIONAIS.
Além disso na chamada do PRINT quando passamos TAG_LIST_GENERATOR dentro do BLOCK_TAG_GENERATOR nós não colocamos os
parênteses, isso por quê se passassemos o mesmo então deveríamos informar quais o parâmetros ele deveria processar, 
contudo já estamos informando quais serão os parâmetros através do posicionamento do *ARGS, ou seja, as STRINGS
'Sábado' e 'Domingo' contidas neste exemplo. 
"""
