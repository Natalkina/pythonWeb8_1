from models import Author, Quote
from mongoengine import disconnect


def search_quotes(query):
    if query.startswith("name:"):
        author_name = query.split("name:")[1]
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
        else:
            quotes = []
    elif query.startswith("tag:"):
        tag_name = query.split("tag:")[1]
        quotes = Quote.objects(tags=tag_name)
    elif query.startswith("tags:"):
        tag_names = query.split("tags:")[1].split(",")
        quotes = Quote.objects(tags__in=tag_names)
    else:
        quotes = []
    return quotes


if __name__ == '__main__':

    while True:
        query = input("Введіть запит (name: <ім'я>, tag: <тег>, tags: <тег1>,<тег2>, ..., або exit): ")
        if query == "exit":
            break
        quotes = search_quotes(query)
        for quote in quotes:
            author_name = quote.author.fullname
            quote_text = quote.quote
            tags = ", ".join(quote.tags)
            print(f"{author_name}: {quote_text}\nTags: {tags}\n")

    disconnect()

