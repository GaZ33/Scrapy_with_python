import camelot
# Lendo as tabelas do arquivo foos.pdf na página 1 e armazenando na variável
tables = camelot.read_pdf("foos.pdf", pages='1')

# Exportando as tabelas para o arquivo foos.csv e criando um zip
tables.export("foos.csv", f="csv", compress=True)
# Exportando a tabela 1 para o arquivo foos.csv, ele cria o arquivo sozinho
tables[0].to_csv("foos.csv")
