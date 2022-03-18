import bookstore
from twitter import TwitterHelper

MAX_RETRY = 2
retry_count = 0


def build_text(book):
    ellipsis_character = "..."
    tags = " #btc #eth"

    length_limit = 280
    # Every url posted is transformed into a shorter url that contains 24 characters
    url_length = 24
    length_available = length_limit - len(tags) - url_length

    text = book.title + "\n" + book.description
    if len(text) > length_available:
        text = text[0:length_available - len(ellipsis_character)] + ellipsis_character + tags
    else:
        text = text + tags
    return text + "\n" + book.url


def post_randomly_book(twitter_helper):
    selected_book = bookstore.select_book()
    print("Selected book title: " + selected_book.title)
    print("Selected book description: " + selected_book.description)
    print("Selected book url: " + selected_book.url)

    status_list = twitter_helper.user_timeline()

    is_posted_book = any(status.full_text.lower().startswith(selected_book.title.lower()) for status in status_list)
    if is_posted_book:
        print("This book was already posted")
        global retry_count
        if retry_count < MAX_RETRY:
            retry_count = retry_count + 1
            print("Retrying to post another book")
            post_randomly_book(twitter_helper)
        else:
            print("There are no more attempts available. No book was posted")
    else:
        print("Trying to post a book...")
        text = build_text(selected_book)
        twitter_helper.update_status(text)


# Main
twitter_helper = TwitterHelper()
twitter_helper.connect()
post_randomly_book(twitter_helper)
