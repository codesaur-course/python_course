# DESAFIO 2

"""
O desafio consiste em analisar o seguinte cenário:
João terá que realizar dois trabalhos na semana, se os dois trabalhos derem certo ele e sua família irão ao
shopping comprar uma TV de 50` e também irão tomar um sorvete.
Porém, se apenas um trabalho der certo eles ainda irão ao shopping mas a TV será de 32` e também tomarão sorverte.
Contudo se nenhum trabalho der certo eles não irão ao shopping, e por consequência terão mais saúde pelo simples
fato de não tomar sorvete.
"""

# ESTRUTURA BASE
tuesday_job = True
thursday_job = False

"""
Dica: 
- Confirmando 2: TV 50` + sorvete
- Confirmando 1: TV 32` + sorvete
- Nenhum trabalho: Fica em casa
"""

tv_50 = tuesday_job and thursday_job
tv_32 = tuesday_job != thursday_job
icecream = tuesday_job or thursday_job
healthier = not icecream

print("TV 50`={}, TV 32`={}, Sorvete={}, Mais Saudável={}"
      .format(tv_50, tv_32, icecream, healthier))
