# Ein Set ist ähnlich zum Tuple, nicht veränderbar und lässt aber keine Duplikate zu

fruit_set = {"apple", "banana", "cherry"}
for fruit in fruit_set:
    print(fruit)


fruit_set_error = {"apple", "banana", "cherry", "apple"}
print(fruit_set_error) # Da keine Duplikate zugelassen sind, wird "apple" nur einmal ausgegeben