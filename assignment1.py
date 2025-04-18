# Base class: Book
class Book:
    def __init__(self, title, author, pages):
        # Public attributes
        self.title = title
        self.author = author
        self.pages = pages

        # Protected attribute (encapsulation)
        self._is_available = True

    # Method to display book information
    def display_info(self):
        print(f" '{self.title}' by {self.author}  | Pages: {self.pages}")
        print(f"   Status: {'Available ' if self._is_available else 'Borrowed '}")

    # Method to borrow the book.
    def borrow_book(self):
        if self._is_available:
            self._is_available = False
            print(f" You've borrowed '{self.title}'.")
        else:
            print(f" '{self.title}' is currently not available.")

    # Method to return the boook.
    def return_book(self):
        if not self._is_available:
            self._is_available = True
            print(f"You've returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

# Child class: DigitalBook (inherits from Book)
class DigitalBook(Book):
    def __init__(self, title, author, pages, genre):
        # Call the parent constructor
        super().__init__(title, author, pages)

        # Additional attribute for digital book
        self.genre = genre

    # Override display_info to include genre (polymorphism)
    def display_info(self):
        print(f" [E-Book] '{self.title}' by {self.author}")
        print(f"  Pages: {self.pages} | Genre: {self.genre}")
        print(f"   Status: {'Available ' if self._is_available else 'Borrowed '}")

        # Create book objects
print("===  Book Library ===\n")
book1 = Book("Echoes of war", "Cleophas Malala",  55)
ebook1 = DigitalBook("Siku Njema", "Ken Walibora",70, "Kiswahili")

# Use methods on Book and DigitalBook
book1.display_info()
book1.borrow_book()
book1.display_info()
book1.return_book()

print("\n---\n")

ebook1.display_info()
ebook1.borrow_book()
ebook1.display_info()

