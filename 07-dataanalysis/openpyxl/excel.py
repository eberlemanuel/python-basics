import openpyxl # pip install openpyxl -> doc: https://openpyxl.readthedocs.io/en/stable/
from openpyxl.chart import BarChart, Reference, Series

wb = openpyxl.load_workbook("umsatz.xlsx", data_only = True)
 
# Workbook aktiv schalten
worksheet = wb.active

for i in range(1,5):
    # Lesen einer Zelle
    # Achtung hier starten wir bei 1 nicht bei 0. Siehe Dokumentation von openpyxl
    cell_description = worksheet.cell(row = i, column = 1)
    cell_cost = worksheet.cell(row = i, column = 2)

    # Ausgeben der Zelle
    print("Description: {} mit Wert {}".format(cell_description.value, cell_cost.value))

# Wir können auch direkt das Value anhand des Zellennamens ausgeben
print("GuV: {}".format(worksheet['B5'].value))

# Alles iterieren
for row in worksheet.iter_rows():
    for cell in row:
        print(cell.value)

# Schreiben mit openpyxl
worksheet['E2'] = 'Test'
# Ändern einer bestehenden Zelle
worksheet['A3'] = 'Auto'

# Chart einfügen
chart = BarChart()
chart.type = "col"
chart.style = 10
chart.title = "Ausgaben"
chart.y_axis.title = 'Betrag (€)'
chart.x_axis.title = 'Bezeichnung'

labels = Reference(worksheet, min_col = 1, min_row = 2, max_row = 4)
data = Reference(worksheet, min_col = 2, min_row = 1, max_row = 4)

chart.add_data(data, titles_from_data=True)
chart.shape = 4
chart.legend = None
chart.set_categories(labels)
worksheet.add_chart(chart, "A10")

# Speichern
wb.save('umsatz_test.xlsx')