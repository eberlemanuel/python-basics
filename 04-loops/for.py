# Ein Loop "eine Schleifen", beginnt mit dem Keyword for und iteriert das Objekt

# Ausgeben aller Elemente einer Liste
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# Ausgeben jedes einzelnen Zeichens
for x in "banana":
  print(x)


#Ausgeben aller Elemente einer Liste und abbrechen nach "banana"
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#Ausgeben aller Elemente einer Liste und überspringen des Elements "banana"
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Ausgeben aller Zahlen von 0-5
for x in range(5):
  print(x)

#Ausgeben aller Zahlen von 3-8
for x in range(3, 8):
  print(x)

#Ausgeben aller Zahlen von 2-30 in 3er Schritten
for x in range(2, 30, 3):
  print(x)