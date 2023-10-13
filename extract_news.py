from selenium import webdriver
#Temos que fazer esse import por ser a versão 4 do selenium
from selenium.webdriver.chrome.service import Service
# Para DF usamos pandas
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"

path = "C:\chromedriver-win64\chromedriver.exe"
# A próxima linha é por cuasa do selenium 4, caso o seu seja o 3, skip ela
service = Service(executable_path=path)

# Se for a versão 3, não coloque nenhum argumento
driver = webdriver.Chrome(service=service)
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
# Agora exportando para um arquivo csv:
df_headlines.to_csv("headlines.csv")
# Para finalizar precisamos fazer:
driver.quit()