import matplotlib.pyplot as plt
from models import relatorios

def grafico_pizza_cat(ini=None, fim=None):
    dados = relatorios.total_categoria(ini, fim)
    if not dados:
        print("Sem dados para o periodo. ")
        return
    categorias = [cat for cat, _ in dados]
    valores = [total for _, total in dados]

    plt.figure(figsize=(6,6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de despesas por categoria")
    plt.axis('equal')
    plt.show()

def grafico_barra_mes(ini=None, fim=None):
    dados = relatorios.total_mes(ini, fim)
    if not dados:
        print("Sem dados para o periodo. ")
        return
    mes = [cat for cat, _ in dados]
    valores = [total for _, total in dados]

    plt.figure(figsize=(8,5))
    plt.bar(mes, valores)
    plt.xlabel("Mes")
    plt.ylabel("Total (R$)")
    plt.title("Despesas total por mes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()