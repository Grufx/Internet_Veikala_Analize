import requests
from bs4 import BeautifulSoup

class Prodcut:
    name = str
    price = str
    category = str
    countColors = str
    link = str

    def __init__(self, name, price,category, countColors, link):
        self.name = name
        self.price = price
        self.category = category
        self.countColors= countColors
        self.link = link

    def __repr__(self):
        return str(self.__dict__)

headers = {
    'authority': 'www.yeezysupply.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}

session = requests.session()

response = session.get('https://www.adidas.com/us/men-athletic_sneakers', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

for element in soup.find_all('div', class_='plp-container-with-masking'):
    name = element.find('p', class_="gl-paragraph gl-paragraph--s gl-product-card__title").text.strip()
    price = element.find('div', class_="badge-container___DVUWN").text.strip()
    category = element.find('p', class_="gl-paragraph gl-paragraph--s gl-product-card__category").text.strip()
    countColors = element.find('span', class_="dark-grey___2ufTt").text.strip()
    link = "https://www.adidas.com/" + element.find('a').get('href')

    prodcut = Prodcut(name, price, category, countColors, link)

    print(prodcut.__repr__())