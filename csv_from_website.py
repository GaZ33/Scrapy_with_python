import pandas as pd
# lendo o arquivo csv e atribuindo todos os dados a variável
df_premier23 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")

# Renomeando o nome das colunas FTHG para Home_goals e FTAG para Away_goals. Necessário colocar inplace
df_premier23.rename(columns={"FTHG": "Home_goals", "FTAG": "Away_goals"}, inplace= True)

print(df_premier23)