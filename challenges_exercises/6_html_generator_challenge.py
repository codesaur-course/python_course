# DESAFIO 6

"""
Neste desafio iremos criar um gerador HTML que deverá retornar ao fim o seguinte texto:
<p class="alert"><span>Curso de Python 3, por</span><strong id="jf">Juracy Filho</strong><span> e </span>
<strong id="ll">Leonardo Leitão</strong><span>.</span></p>
Abaixo teremos uma estrutura inicial:
"""

"""
def tag(tag, *args, **kwargs):
    pass
    
print(
    tag("p",
        tag("span", "Curso de Python 3, por "),
        tag("strong", "Juracy Filho", id="if),
        tag("span", " e "),
        tag("strong", "Leonardo Leitão", id="ll"),
        tag("span", "."),
        html_class="alert"
    )
)
"""

def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    attrs = ''.join(f"{k}='{v}'" for k, v in kwargs.items()) # UNPACKING do DICIONÁRIO
    inner = ''.join(args) # UNPACKING das TUPLAS
    return f"<{tag} {attrs}>{inner}</{tag}>"

print(
    tag("p",
        tag("span", "Curso de Python 3, por "),
        tag("strong", "Juracy Filho", id="if"),
        tag("span", " e "),
        tag("strong", "Leonardo Leitão", id="ll"),
        tag("span", "."),
        html_class="alert"
    )
)
