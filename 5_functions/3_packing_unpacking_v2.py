# PACKING | UNPACKING

"""
Neste exercicio iremos abordar um pouco mais sobre o uso do PACKING | UNPACKING
"""

def block_tag(text_model, class_model="success", inline_model=False):
    tag = 'span' if inline_model else 'div'
    return f"<{tag} class='{class_model}'>{text_model}</{tag}>"


def tag_list(*items): # packing para uma TUPLA
    list_model = ''.join(f'<li>{item}</li>' for item in items) # O .JOIN() concaterá novos valores na LISTA
    print(type(list_model)) # O tipo é STRING por quê o list_model começa com uma STR vazia e concatena os valores
    return f"<ul>{list_model}</ul>"

print(block_tag(tag_list('Item 1', 'Item 2'), class_model='info')) # gera o conteúdo através do TAG_LIST()
