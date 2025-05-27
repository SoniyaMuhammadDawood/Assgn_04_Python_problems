# 11. Class Methods                                                  Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, book_name):
        self.book_name = book_name
        Book.increment_book_count()  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
b1 = Book("Modern Ai Python")
b2 =Book("Typescript")
b3 =Book("Nextjs")
b4 =Book("CSS")
print(b1.total_books)