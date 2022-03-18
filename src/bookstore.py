import requests
import random
from bs4 import BeautifulSoup


class Book:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description


def select_book():
    html_text = requests.get('https://thecryptobookstore.com/product-sitemap.xml').text
    sitemapSoup = BeautifulSoup(html_text, 'lxml')
    books = sitemapSoup.find_all('loc')
    number_of_books = len(books)
    selected_idx = random.randint(0, number_of_books - 1)
    selected_url = books[selected_idx].text

    html_text = requests.get(selected_url).text
    bookSoup = BeautifulSoup(html_text, 'html.parser')
    title = bookSoup.head.title.text.replace(' - The Crypto Bookstore', '')
    description = bookSoup.find('meta', {'name': 'description'})['content']

    return Book(url=selected_url, title=title, description=description)
