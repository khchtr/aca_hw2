from datetime import date
from uuid import uuid4


class Library:
    def __init__(self, name):
        self.name = name
        self.student = set()
        self.books = set()
        return f"Library has been created"

    def __repr__(self):
        return f"Number of books in the library {len(self.books)}. Number of students {len(self.student)}"
    
    def add_book(self, title, authors: list, year, isbn, genres):
        add_book = Book(title=title, authors=authors, year=year, isbn=isbn, genres=genres)
        self.books.append(add_book)
        return add_book
    
    def remove_book(self, book):
        self.book.remove(book) # insert search function here

    def add_student(self, name, email, borrowing_limit = 5):
        add_student = Student(name=name, email=email, borrowing_limit=borrowing_limit)
        self.student.append(add_student)
        return add_student
    
    def remove_student(self, email):
        remove_student = any(x for x in self.student if x.email == email) 
        self.student.remove(remove_student)

    
# change student’s borrowing limit
# see all books
# see all available books (at least one available copy)
# search for a book by different criteria

class Book:
    def __init__(self, title, authors: list, year, isbn, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = isbn
        self.genre = genre  # handle list
        self.copies = set()

    def __repr__(self):
        return f"{self.authors} - {self.title}"  # TO-DO Neaty print all author names

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.isbn == other.isbn
        
    def add_copy(self, condition: int) -> object:
        add_copy = BookCopy(condition=condition, book_id=self)
        self.copies.append(add_copy)
        return add_copy

    @property
    def available_copies(self):
        total = 0
        for copy in self.copies:
            if copy.availability == 'available':
                total += 1
            else:
                pass
        return total

 


class BookCopy:
    def __init__(self, condition: int, availability='available', borrower=None, borrowed_date=None,
                 book_id=None):  # refer to book
        self.book_id = book_id
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.availability = availability # somehow limit this to binary option
        self.condition = condition  # Limit this to 10

    def borrow_book(self, borrower):  # add student_id obj, check the limnit of 5 books and single item before lent, and if there are expired books
        self.borrower = borrower
        self.borrowed_date = date.today()
        self.availability = "on loan"
        return f"Book is lent to {borrower}"

    def return_book(self):  # remove student_id obj, this should take element from student as well.
        self.borrower = None
        self.borrowed_date = None
        self.availability = "available"
        return f"Book has been returned"

    def change_condition(self, condition):
        self.condition = condition


class Student:
    def __init__(self, name, email, borrowing_limit = 5):
        self.student_id = str(uuid4())
        self.name = name
        self.email = email
        self.books_taken = []
        self.borrowing_limit = borrowing_limit

    def borrow_book(self, ):
        pass # borrow a book

    def return_book(self, ):
        pass # return a book

    @property
    def status(self):
        for book in self.books_taken:
            return f"{book.book_id} // Due to 14-{book.borrowed_date}" #check this


book_1 = Book('Anna Karenina', ["Tolstoy", 'Lev'], "2013", "1526-4156", "Historical")

print(book_1)
book_1.add_copy(4)

print(book_1.copies)
print(book_1.available_copies)
