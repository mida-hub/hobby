from openpyxl import load_workbook

filename = 'output/copied_worksheets.xlsx'
wb = load_workbook(filename)
for ws in wb.worksheets:
    print(f'{ws.title}')
    if ws.title.endswith('Copy'):
        print(f'{ws.title} を削除します')
        wb.remove(ws)
wb.save('output/remove_worksheets.xlsx')
    