import requests
from bs4 import BeautifulSoup
from typing import List


class Product:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description


def product_urls() -> List[str]:
    result = []
    html_text = requests.get('https://thecryptobookstore.com/product-sitemap.xml').text
    sitemapSoup = BeautifulSoup(html_text, 'lxml')
    products = sitemapSoup.find_all('loc')
    # ignores the first item because it is not a product
    products = products[1:len(products) - 1]
    for product in products:
        result.append(product.get_text())
    return result


def get_product(url) -> Product:
    html_text = requests.get(url).text
    product_soup = BeautifulSoup(html_text, 'html.parser')
    title = product_soup.head.title.text.replace(' - The Crypto Bookstore', '')
    description = product_soup.find('meta', {'name': 'description'})['content']
    return Product(url=url, title=title, description=description)

