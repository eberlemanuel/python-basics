# While ist ebensfalls eine Schleife wie for, nur dass die Schleife so lange läuft bis die Bedingung eintrifft

i = 1
while i < 5:  # Läuft so lange bis die Bedingung zutrifft. Hier gelten die gleichen Operatoren wie beim IF Keyword
  print("i: " + str(i))
  i += 1 # Achtung: Hier wird der Index hochgezählt mit jedem Durchlauf, ansonsten landen wir in einer Endlosschleife, weil die Bedingung sonst nie zutrifft


j = 1
while j < 5:
  if j == 3: # Wir können die Schleife auch verlassen wenn j == 3
    break 
  print("j: " + str(j))
  j += 1


k = 1
while k < 5:
  k += 1
  if k == 3: # Wir können auch wieder die Iteration 3 überspringen
    continue 
  print("k: " + str(k))