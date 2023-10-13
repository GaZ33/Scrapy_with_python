from selenium import webdriver
# para fazer headless mode
from selenium.webdriver.chrome.options import Options
#Temos que fazer esse import por ser a versão 4 do selenium
from selenium.webdriver.chrome.service import Service
# Para DF usamos pandas
import pandas as pd
# Importando biblioteca para mexer com datas
from datetime import datetime
# Importando biblioteca para mexerc om os
import os
# Importando biblioteca para o systema. CMD
import sys


# Basicamente essa linha é para conseguir o path do executable que iremos criar e armazenar em uma variável
application_path = os.path.dirname(sys.executable)

# criando uma variável para armazenar o dia de hoje para personalizar o nome do nosso arquivo
now = datetime.now()
# Colocando esse time que conseguimos em um formato de string
dia_mes_ano = now.strftime("%d%m%y") #DDMMYYYY


# Website que queremos pegar os dados
website = "https://www.thesun.co.uk/sport/football/"
# o caminho do executável do chromedriver
path = "C:\chromedriver-win64\chromedriver.exe"


# Headless-mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")


# A próxima linha é por cuasa do selenium 4, caso o seu seja o 3, skip ela
service = Service(executable_path=path)

# Se for a versão 3, não coloque nenhum argumento
driver = webdriver.Chrome(service=service, options=options)
# ir até a página da web
driver.get(website)

# Atribuindo todos os path que econtramos pelo caminho na variável. Lembrando que estamos pegando todos os elementos
# Correspondentes a esse path
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# Criando listas vazias para depois exportar os dados
titles = []
subtitles = []
links = []


# Criando um for loop para iterar os itens da lista e pegarmos os títulos, links e os subtítulos
for container in containers:
    # Como só queremos 1 elemento, usamos find_element, sem o S.
    title = container.find_element(by="xpath", value='./a/span').text
    subtitle = container.find_element(by="xpath", value='./a/h3').text
    # Como o link é um atributo "herf", precisamos pegar o valor do atributo.
    link = container.find_element(by="xpath", value='./a').get_attribute(name='href')
    # Adicionando o título a lista
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitles': subtitles, 'links': links}
# a gente até pode criar o dicionário dentro da função, mas para facilitar fizemos isso.
df_headlines = pd.DataFrame(my_dict)

# Criando o nome do nosso arquivo:
file_name = f"headlines-{dia_mes_ano}.csv"

# arrumando para que o path seja universal para todos os sistemas, concatenando as variável
# Esse path vai ser onde estará o executável
path_file =  os.path.join(application_path, file_name)
# Agora exportando para um arquivo csv:

df_headlines.to_csv(path_file)
# Para finalizar precisamos fazer:
driver.quit()