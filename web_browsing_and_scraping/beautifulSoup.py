import bs4
import requests
import re


def getAlePlanszowkiPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    # create soup object, parse text in search of information
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # create list of all matching ocurrencies of CSS selector
    elems = soup.select('#our_price_display')
    return elems[0].text.strip()  # pick first element from list


def getIkeaPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()

    # create soup object, parse text in search of information
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
# You can retrieve a web page element from a BeautifulSoup object by calling the select() method and passing a string of a CSS selector for the element you are looking for. Selectors are like regular expressions: they specify a pattern to look for—in this case, in HTML pages instead of general text strings.
    # create list of all matching ocurrencies of CSS selector in HTML tags
    priceElems = soup.select('#content > div > div.pip-page-container__inner > div > div.pip-product__subgrid.product-pip.js-product-pip > div.pip-product__buy-module-container > div > div.js-price-package.pip-pip-price-package > div > div.pip-pip-price-package__price-wrapper > div > span > span.pip-price__integer')
    productList = productURL.split('/')
    for item in productList:
        if '-' in item:
            regexProduct = re.compile(r'(\w+)-')
            mo = regexProduct.search(item)
            productName = mo[1].upper()
            return 'Cena produktu ' + productName + ' wynosi ' + priceElems[0].text.strip()


# main
listIKEA = ['https://www.ikea.com/pl/pl/p/markus-krzeslo-biurowe-vissle-ciemnoszary-70261150/', 'https://www.ikea.com/pl/pl/p/jaervfjaellet-krzeslo-biurowe-z-podlokietnikami-80510639/',
            'https://www.ikea.com/pl/pl/p/dagotto-podnozek-czarny-40240989/', 'https://www.ikea.com/pl/pl/p/baggmuck-mata-na-buty-do-wewnatrz-na-zewnatrz-szary-60329711/']

for productURL in listIKEA:
    price = getIkeaPrice(productURL)
    print(price)

productURL = 'https://aleplanszowki.pl/dodatki-do-gier/3665-star-wars-rebelia-imperium-u-wladzy.html'
price = getAlePlanszowkiPrice(productURL)
print(price)
