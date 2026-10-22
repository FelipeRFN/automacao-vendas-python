import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

# Importar base de dados
df = pd.read_csv("train.csv")

# Iremos converter os formatos e já salvar no próprio Data Frame
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True) # Dayfirst para informar que o dia vem antes do mês nestas datas
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst= True)

# Processar os dados
# Calcular o tempo de envio
df["Tempo_envio"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Arredondar os valores
df["Sales"] = df["Sales"].round(2)

# Dividir a base de dados em vendas regionais: east, south, central e west
regioes = df["Region"].unique() # Aqui estamos separando as regiões unicas da base de dados

for regiao in regioes:
    # Estamos passando por todas as regiões da base de dados e separando em df_regioes todas as que possuem a mesa regiao pedida acima
    df_regioes = df[df["Region"] == regiao]

    nome_ficheiro = f"vendas_{regiao.lower().replace(' ', '_')}.csv" # Definindo o nome do arquivo com o nome da região
    caminho_completo = os.path.join("C:/Users/Felipe/Desktop/dados_vendas", nome_ficheiro) # Definindo o caminho para onde vai as novas planilhas com o nome desejado

    df_regioes.to_csv(caminho_completo, index=False) #Estamos mandando as linhas da região encontradas para outro arquivo CSV,
                                                    #porém com o nome e caminho desejados

# Listar e carregar todas as bases de dados
dfs_regionais = {}


# Percorrer a pasta dados_vendas e procurar todos os arquivos nomeados como vendas.csv
# O asterisco funciona para procurar qualquer nome depois das vendas_
for arquivo in glob.glob("C:/Users/Felipe/Desktop/dados_vendas/vendas_*.csv"):
    nome_arquivo = os.path.basename(arquivo) # Extrair apenas o nome do arquivo, sem o caminho inteiro
    nome_regiao = nome_arquivo.replace("vendas_", "").replace(".csv", "") #iremos retirar o nome vendas_ e a extensão .csv
    dfs_regionais[nome_regiao] = pd.read_csv(arquivo)
# Assim criamos um loop e sempre que for inserido uma nova região iremos adicionar ela na lista


# Gráficos
#Vendas Totais por Região
vendas_regiao = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
vendas_regiao.plot(kind="bar", color="#2b5c8f", edgecolor="black")
plt.title("Desempenho de Vendas por Região", fontsize=14, fontweight="bold")
plt.xlabel("Região", fontsize=11)
plt.ylabel("Total de Vendas ($)", fontsize=11)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("vendas_por_regiao.png", dpi=300)
plt.show()


# Categorias com maior faturamento
top_categorias = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(8, 4))
top_categorias.plot(kind="barh", color="#2ca02c", edgecolor="black")
plt.title("Faturamento por Categoria de Produto", fontsize=14, fontweight="bold")
plt.xlabel("Total de Vendas ($)", fontsize=11)
plt.ylabel("Categoria", fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("vendas_por_categoria.png", dpi=300)
plt.show()


#Evolução das vendas
# Agrupar vendas por ano/mês (ou data do pedido)
vendas_tempo = df.groupby("Order Date")["Sales"].sum()

plt.figure(figsize=(10, 4))
vendas_tempo.plot(kind="line", color="#d62728", linewidth=1.5)
plt.title("Evolução Temporal das Vendas", fontsize=14, fontweight="bold")
plt.xlabel("Data do Pedido", fontsize=11)
plt.ylabel("Vendas ($)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("evolucao_vendas.png", dpi=300)
plt.show()