# Dictionaries sind aufgebaut im Format Key und Value. Sie lassen keine Duplikate zu und sind zur Laufzeit änderbar

fruit_price_dict = {
    "apple" : 1.5,
    "banana" : 2.0,
    "cherry" : 1.0
}

for fruit_price_key, fruit_price_value in fruit_price_dict.items():
    print(fruit_price_key) # Hier steht der Key (linke Seite des Dict) drin
    print(fruit_price_value) # Hier steht das Value (rechte Seite des Dict) drin