import xlsxwriter

workbook = xlsxwriter.Workbook('umsatz.xlsx')
worksheet = workbook.add_worksheet('GuV')

table = (
    ['Einnahmen', 5000],
    ['Miete', -500],
    ['Strom', -100],
    ['Aushilfe', -450]
)

col = 0
row = 0

for description, cost in table:
    print("Write '{}' and '{}' to file".format(description, cost))
    worksheet.write(row, col, description) # A1
    worksheet.write(row, col+1, cost) # B1
    row += 1

worksheet.write(row, 0, "Total")
worksheet.write(row, 1, "=SUM(B1:B{})".format(len(table)))

workbook.close()


































#table = (
#    ['Einnahmen', 5000],
#    ['Miete', -500],
#    ['Strom', -100],
#    ['Aushilfe', -1000]
#)
#
#row = 0
#col = 0
#
#for description, cost in table:
#    print("Write '{}' with '{}' to file".format(description, cost))
#    worksheet.write(row, col, description)
#    worksheet.write(row, col+1, cost)
#    row += 1
#
#worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B{})'.format(len(table)))
#
#workbook.close()
