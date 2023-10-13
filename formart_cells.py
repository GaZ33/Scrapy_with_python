from openpyxl import load_workbook
from openpyxl.styles import Font

# Abrindo o arquivo na variável
wb = load_workbook('pivot_table.xlsx')

# Selecionando a tabela que queremos usar
sheet = wb['Report']

# Titulo
sheet['A1'] = 'SALES REPORT'
# sub título
sheet['A2'] = 'Januray'

# Alterando a fonte
sheet['A1'].font = Font('Arial', bold=True, size=20)
sheet['A2'].font = Font('Arial', bold=True, size=12)

#Salvando
wb.sabe('Report January.xlsx')

