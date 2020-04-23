from openpyxl import load_workbook

filename = 'input/various_worksheets.xlsx'
wb = load_workbook(filename, read_only=True)
print(f'{filename} のワークシート情報を読み込みます')

ws0 = wb.worksheets[0]
print(f'{ws0.title} のセルを1行ずつ表示します')
for row in ws0:
    values = [str(column.value) for column in row]
    print(values)
