from typing import List
import random
import bookstore
from twitter import TwitterHelper


def build_text(product):
    ellipsis_character = "..."
    tags = " #btc #eth"

    length_limit = 280
    # Every url posted is transformed into a shorter url that contains 24 characters
    url_length = 24
    length_available = length_limit - len(tags) - url_length

    text = product.title + "\n" + product.description
    if len(text) > length_available:
        text = text[0:length_available - len(ellipsis_character)] + ellipsis_character + tags
    else:
        text = text + tags
    return text + "\n" + product.url


def exclude_posted_urls(product_urls, status_list) -> List[str]:
    result = []
    for product in product_urls:
        excluded = False
        product_title = product.split('/')[-2].replace('-', ' ')
        for status in status_list:
            tweet_title = status.full_text.split('\n')[0].lower()
            if product_title == tweet_title:
                excluded = True
        if not excluded:
            result.append(product)
    return result


def post_randomly_product(twitter_helper):
    days_ago = 30
    status_list = twitter_helper.user_timeline(days_ago)
    product_urls = bookstore.product_urls()
    product_urls = exclude_posted_urls(product_urls, status_list)

    if len(product_urls) != 0:
        print("Trying to post a product...")

        number_of_products = len(product_urls)
        selected_idx = random.randint(0, number_of_products - 1)
        selected_url = product_urls[selected_idx]

        selected_product = bookstore.get_product(selected_url)
        print("Selected product title: " + selected_product.title)
        print("Selected product description: " + selected_product.description)
        print("Selected product url: " + selected_product.url)

        text = build_text(selected_product)
        twitter_helper.update_status(text)
    else:
        print("All product have been posted during the last " + str(days_ago) + " days")


# Main
twitter_helper = TwitterHelper()
twitter_helper.connect()
post_randomly_product(twitter_helper)
