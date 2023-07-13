# Das IF Keyword ermöglicht es Bedingungen zwischen Zahlen, Strings, Listen etc. zu prüfen und dementsprechend zu reagieren mit einem anderen Code
a = 10
b = 10
c = 44

# Verschiedene Operatoren, die Bedingungen stellen
if a == b:
    print("a ist gleich b")

if a != c:
    print("a ist ungleich c")

if a < c:
    print("a ist kleiner c")

if a <= b:
    print("a ist kleiner gleich b")

if c > b:
    print("c ist größer b")

if c >= b:
    print("c ist größer gleich b")
elif c >= a:
    print("c ist größer gleich a")
else: # falls Möglichkeit 1 und 2 nicht eintreffen
    print("c ist nicht größer gleich b oder a")
print("Nicht im IF Block") # Nach dem IF muss eine Einrückung passieren, ansonsten wird der Command nicht innerhalb des IF ausgeführt

# logische UND Verknüpfung, dass 2 Bedingungen eintreffen müssen
if a < c and b < c:
    print("a und b sind kleiner c")

# logische ODER Verknüpfung, dass entweder Bedingung 1 oder Bedingung 2 eintreffen
if a < c or c < b:
    print("Entweder ist a kleiner c oder c kleiner b")

# logische NICHT Verknüpfung, invertiert die Bedingung
if not c < a:
    print("c ist nicht kleiner a")