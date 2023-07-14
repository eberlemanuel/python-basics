# Funktionen nutzen wir um Code mehrfach zu nutzen ohne den Code X-mal neu zu schreiben


# OHNE FUNKTION
a = 1
b = 2
c = a + b
print("c ist: " + str(c))

c = a - b
print("c ist: " + str(c))


# MIT FUNKTION
def print_result(c): # c ist ein Argument. Eine Funktion kann kein oder mehrere Argumente enthalten. Die Argumente werden mit Kommas getrennt z.B. print_result(arg1, arg2, arg3, ...)
    print("c ist: " + str(c)) # print Anweisung muss nur einmal definiert werden und kann X-mal verwendet werden

a = 1
b = 2
print_result(a + b) # Vorteil: Falls sich etwas ändert weniger Pflegeaufwand
print_result(a - b) # Lohnt sich immer dann, wenn du die gleiche Sache min. 2 mal verwendest