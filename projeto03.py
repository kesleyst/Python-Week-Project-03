import pandas as pd

dados = pd.read_excel("vendas.xlsx")
import plotly.express as px
grafico = px.histogram(dados, x = "loja",
                    y = "preco", 
                    text_auto = True,
                    title = "Faturamento",
                    color= "forma_pagamento")
grafico.show()
grafico.write_html("Faturamento.html")
lista_colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]

for coluna in lista_colunas:
    grafico = px.histogram(dados, x = coluna,
                           y="preco",
                            text_auto = True,
                            title="Faturamento",
                             color="forma_pagamento" )
    grafico.show()
    grafico.write_html(f"Faturamento Detalhado-{coluna}.html")