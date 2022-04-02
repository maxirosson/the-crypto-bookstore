from typing import List
import random
import bookstore
import twitter


def build_text(product):
    ellipsis_character = "..."
    #tags = " #btc #eth"
    tags = ""
    coinkit_legend = "\n\n@coinkit_ mon 10 1 #BTC"

    length_limit = 280
    # Every url posted is transformed into a shorter url that contains 24 characters
    url_length = 24
    
    coinkit_length =  len(coinkit_legend)
    
    length_available = length_limit - len(tags) - url_length - coinkit_length

    if product.author is not None and product.year is not None:
        text = product.title + "\n" +  \
               "Published in " + product.year + " by " + product.author + "\n" + \
               product.description
    else:
        text = product.title + "\n" + product.description
    if len(text) > length_available:
        text = text[0:length_available - len(ellipsis_character)] + ellipsis_character + tags
    else:
        text = text + tags
    return text + coinkit_legend + "\n" + product.url


def exclude_posted_urls(product_urls, tweets) -> List[str]:
    result = []
    for product in product_urls:
        excluded = False
        product_title = product.split('/')[-2].replace('-', ' ')
        for tweet in tweets:
            tweet_title = tweet.text.split('\n')[0].lower()
            if product_title == tweet_title:
                excluded = True
        if not excluded:
            result.append(product)
    return result


def post_randomly_product():
    days_ago = 30
    tweets = twitter.user_timeline(days_ago)
    product_urls = bookstore.product_urls()
    product_urls = exclude_posted_urls(product_urls, tweets)

    if len(product_urls) != 0:
        print("Trying to post a product...")

        number_of_products = len(product_urls)
        selected_idx = random.randint(0, number_of_products - 1)
        selected_url = product_urls[selected_idx]

        selected_product = bookstore.get_product(selected_url)
        print("Selected product title: " + selected_product.title)
        if selected_product.author is not None:
            print("Selected product author: " + selected_product.author)
        if selected_product.year is not None:
            print("Selected product year: " + selected_product.year)
        print("Selected product description: " + selected_product.description)
        print("Selected product url: " + selected_product.url)

        text = build_text(selected_product)
        twitter.update_status(text)
    else:
        print("All product have been posted during the last " + str(days_ago) + " days")


# Main
post_randomly_product()
