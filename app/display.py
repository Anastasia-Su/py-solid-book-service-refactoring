from app.book import Book


class Display:
    @staticmethod
    def console(book: Book) -> None:
        print(book.content)

    @staticmethod
    def reverse(book: Book) -> None:
        print(book.content[::-1])
