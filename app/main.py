from app.book import Book
from app.display import Display
from app.print import Print
from app.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            getattr(Display(), method_type)(book)
        elif cmd == "print":
            getattr(Print(), method_type)(book)
        elif cmd == "serialize":
            return getattr(Serializer(), method_type)(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
