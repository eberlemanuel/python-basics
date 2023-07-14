# Tuple ist das gleiche wie eine Liste nur, dass die Elemente nicht mehr geändert werden können

fruit_tuple = ("apple", "banana", "cherry")
for fruit in fruit_tuple:
    print(fruit)

# thistuple[1] = "kiwi" # Hier kommt ein Fehler, wenn wir das Element 1 ändern möchten

# Mehrere Tuple zusammenführen
fruit_tuple_2 = ("kiwi", "apple") # Duplikate sind erlaubt
fruit_tuple_3 = fruit_tuple + fruit_tuple_2
print(fruit_tuple_3)