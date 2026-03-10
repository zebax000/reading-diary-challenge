from datetime import datetime

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False

        note = Note(text, page, date)
        self.notes.append(note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        notas = []

        for note in self.notes:
            if note.page == page:
                notas.append(note)

        return notas

    def page_with_most_notes(self) -> int:
        pass


    def __str__(self):
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nRating: {self.rating}"





