import pandas as pd

# carregar dados
df = pd.read_excel("vendas.xlsx")

# mostrar primeiras linhas
print("Primeiras linhas:")
print(df.head())

# calcular total de vendas
total = df["Valor"].sum()
print("Total de vendas:", total)

# vendas por produto
vendas_produto = df.groupby("Produto")["Valor"].sum()

print("\nVendas por produto:")
print(vendas_produto)
