# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, isbn_num):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn_num': isbn_num
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def get_book(self, isbn):
        return self.books.get(isbn, "Book not found.")

    def search_books(self, keyword, by="title"):
        results = [book for book in self.books.values() if keyword.lower() in book[by].lower()]
        return results

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        if isbn in self.books:
            self.books[isbn].update(kwargs)
            print(f"Book with ISBN {isbn} updated successfully.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def is_available(self, isbn):
        return isbn in self.books

# Demonstration
if __name__ == "__main__":
    library = LibraryManager()

    # Adding sample books
    library.add_book("978-3-16-148410-0", "Operating Systems Concepts", "Abraham Silberschatz", "Wiley", "10th", 2021, "978-3-16-148410-0")
    library.add_book("978-0-13-409341-3", "Data Structures and Algorithms in Python", "Michael T. Goodrich", "Wiley", "1st", 2020, "978-0-13-409341-3")
    library.add_book("978-0-262-03384-8", "Machine Learning", "Tom M. Mitchell", "McGraw Hill", "1st", 2021, "978-0-262-03384-8")

    # Removing a book
    library.remove_book("978-0-13-409341-3")

    # Retrieving book details
    print(library.get_book("978-3-16-148410-0"))

    # Searching for books by title
    print(library.search_books("Machine Learning"))

    # Listing all books
    print(library.list_books())

    # Updating book details
    library.update_book("978-3-16-148410-0", title="Operating Systems Concepts Updated Edition")

    # Checking if a book is available
    print(library.is_available("978-0-262-0384-8"))
    print(library.is_available("978-0-13-409341-3"))
