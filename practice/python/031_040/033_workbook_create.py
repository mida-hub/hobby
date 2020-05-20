from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = '新しいワークシート'
wb.save('output/new_workbook.xlsx')