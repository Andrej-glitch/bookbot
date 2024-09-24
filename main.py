def main():
    book_path = "github.com/Andrej-glitch/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()