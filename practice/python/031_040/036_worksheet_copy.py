from openpyxl import load_workbook

filename = 'input/various_worksheets.xlsx'
wb = load_workbook(filename)
for ws in wb.worksheets:
    print(f'{ws.title} をコピーします')
    wb.copy_worksheet(ws)
wb.save('output/copied_worksheets.xlsx')
    