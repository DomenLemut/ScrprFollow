from bs4 import BeautifulSoup
import requests

def scrapePrice(url):
    result = requests.get(url)

    soup = BeautifulSoup(
        result.text,
        "html.parser"
    )

    prices = soup.find_all(
        "div",
        class_="price"
    )

    valueStr = prices[0].get_text().strip() #to somehow dela, ker .string ni :-)

    return valueStr

def getName(url):
    str = url[:-4]

    l = len(str) - 1
    while(not str[l] == '/'):
        l -= 1

    
    str = str[l + 1:]
            

    return str.upper()