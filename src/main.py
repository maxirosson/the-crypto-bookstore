import bookstore
from twitter import TwitterHelper

MAX_RETRY = 5
retry_count = 0


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


def post_randomly_product(twitter_helper):
    selected_product = bookstore.select_product()
    print("Selected product title: " + selected_product.title)
    print("Selected product description: " + selected_product.description)
    print("Selected product url: " + selected_product.url)

    status_list = twitter_helper.user_timeline()

    is_posted_product = any(status.full_text.lower().startswith(selected_product.title.lower()) for status in status_list)
    if is_posted_product:
        print("This product was already posted")
        global retry_count
        if retry_count < MAX_RETRY:
            retry_count = retry_count + 1
            print("Retrying to post another product")
            post_randomly_product(twitter_helper)
        else:
            print("There are no more attempts available. No product was posted")
    else:
        print("Trying to post a product...")
        text = build_text(selected_product)
        twitter_helper.update_status(text)


# Main
twitter_helper = TwitterHelper()
twitter_helper.connect()
post_randomly_product(twitter_helper)
