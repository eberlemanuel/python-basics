import xlsxwriter #pip install xlsxwriter

# Neues Workbook anlegen
workbook = xlsxwriter.Workbook('tutorial.xlsx')
# Neues Datenblatt hinzufügen
worksheet = workbook.add_worksheet('Beispiel')
worksheet2 = workbook.add_worksheet('Beispiel2')
# Schreiben
worksheet.write(0, 0, 'TEST')
worksheet.write(10, 5, "Test2")

worksheet2.write(1,1,"=SUM(1,2)")
# Schließen der Datei
workbook.close()