import json
import xml.etree.ElementTree as ET
from book import Book


class Serializer:
    @staticmethod
    def json(book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})

    @staticmethod
    def xml(book: Book) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = book.title
        content = ET.SubElement(root, "content")
        content.text = book.content
        return ET.tostring(root, encoding="unicode")
