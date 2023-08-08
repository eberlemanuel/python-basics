import requests
from bs4 import BeautifulSoup

# pip install requests, bs4

# headers wird benötigt um die Website zu laden 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def get_price(url):
    # laden des Seiteninhalts
    product_site = requests.get(url, headers=headers)
    # verarbeiten mit BS
    soup = BeautifulSoup(product_site.content, features='html.parser')
    # finden des Bereiches worin der Preis steht
    price_div = soup.find('div', {'class' : 'pdp_price__price pl_mt100 js_pdp_price__price'})
    # auslesen des Elements worin der Preis steht
    price_arr = price_div.find('span', {'class' : 'js_pdp_price__retail-price__value pl_headline300'})
    # zurückgeben des Preis
    return price_arr.get_text()

def compare_price(product_one, product_two):
    pass
    # bei Implementierung bitte löschen
    # ....

def main():
    url_1 = "https://www.otto.de/p/apple-iphone-14-pro-max-256gb-smartphone-17-cm-6-7-zoll-256-gb-speicherplatz-48-mp-kamera-1676826899/#variationId=1676025303"
    #url_2 = "..."

    product_price_1 = get_price(url_1)
    print(product_price_1)

    #product_price_2 = get_price(url_2)
    #print...

    #compare_price(product_price_1, product_price_2)

main()