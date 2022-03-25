import requests
from bs4 import BeautifulSoup
from typing import List


class Product:
    def __init__(self, url, title, description, author, year):
        self.url = url
        self.title = title
        self.description = description
        self.author = author
        self.year = year


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

    author = None
    author_result = product_soup.select('.summary.entry-summary .woocommerce_extensions_brand_item_caption')
    if len(author_result) == 1:
        author = author_result[0].text

    year = None
    year_result = product_soup.select('.summary.entry-summary '
                                      '.woocommerce-product-attributes-item--attribute_pa_year-of'
                                      '-publishing .woocommerce-product-attributes-item__value')
    if len(year_result) == 1:
        year = year_result[0].text

    return Product(url=url, title=title, description=description, author=author, year=year)

