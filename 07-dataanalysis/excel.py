import xlsxwriter #pip install xlsxwriter

# Neues Workbook anlegen
workbook = xlsxwriter.Workbook('tutorial.xlsx')
# Neues Datenblatt hinzufügen
worksheet = workbook.add_worksheet('Beispiel')
# Schreiben
worksheet.write(0, 0, 'TEST')
# Schließen der Datei
workbook.close()