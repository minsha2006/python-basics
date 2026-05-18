class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued")
        else:
            print("Book not found")

    def return_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(self.books)


l = Library()

l.add_book("Python")
l.add_book("Java")

l.display_books()

l.issue_book("Python")

l.display_books()

l.return_book("Python")

l.display_books()

