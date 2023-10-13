import pandas as pd
#Lendo o dataframe do excel
df = pd.read_excel('supermarket_sales.xlsx')
#Selecionando apenas essas 3 colunas 
df = df[['Gender', 'Product line', 'Total']]
# Criando a tabela dinâmica com a função soma
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum')
# Exportando essa tabela para um arquivo de excel
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4, startcol=3)

