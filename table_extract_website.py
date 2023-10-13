import pandas as pd

simpson = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes') # Função que retorna uma lista de tableas

print(simpson[0])


