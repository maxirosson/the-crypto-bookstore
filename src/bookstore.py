import requests
import random
from bs4 import BeautifulSoup


class Product:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description


def select_product():
    html_text = requests.get('https://thecryptobookstore.com/product-sitemap.xml').text
    sitemapSoup = BeautifulSoup(html_text, 'lxml')
    products = sitemapSoup.find_all('loc')
    number_of_products = len(products)
    selected_idx = random.randint(0, number_of_products - 1)
    selected_url = products[selected_idx].text

    html_text = requests.get(selected_url).text
    product_soup = BeautifulSoup(html_text, 'html.parser')
    title = product_soup.head.title.text.replace(' - The Crypto Bookstore', '')
    description = product_soup.find('meta', {'name': 'description'})['content']

    return Product(url=selected_url, title=title, description=description)
