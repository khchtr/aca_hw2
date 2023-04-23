from datetime import date, timedelta
from uuid import uuid4

# change student’s borrowing limit
# see all books
# see all available books (at least one available copy)
class Library:
    def __init__(self, name):
        self.name = name
        self.student = set()
        self.books = set()
        return f"{self.name} has been created"

    def __repr__(self):
        return f"Number of books in the library {len(self.books)}. Number of students {len(self.student)}"

    def add_book(self, title, authors: list, year, isbn, genre):
        add_book = Book(title=title, authors=authors, year=year, isbn=isbn, genre=genre)
        self.books.append(add_book)
        return add_book

    def remove_book(self, book):
        self.books.remove(book)  # insert search function here

    def add_student(self, name, email, borrowing_limit=5):
        add_student = Student(name=name, email=email, borrowing_limit=borrowing_limit)
        self.student.append(add_student)
        return add_student

    def remove_student(self, email):
        remove_student = any(x for x in self.student if x.email == email)
        self.student.remove(remove_student)

    def seek_book(self, criteria, value): #chech this
        valid_criteria = ["title", "authors", "year", "isbn", "genre"]
        if any(x == criteria for x in valid_criteria):
            result = all(x for x in self.books if x.criteria == value)
        else:
            print("Such criteria does not exist")
        return result


class Book: #Done
    def __init__(self, title, authors: list, year, isbn, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = isbn
        self.genre = genre  # handle list
        self.copies = []

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
            if copy.availability:
                total += 1
            else:
                pass
        return total

class BookCopy:
    def __init__(self, condition: int, availability=True, borrower=None, borrowed_date=None,
                 book_id=None):
        self.book_id = book_id
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.availability = availability
        self.condition = condition  # Limit this to 10

    def borrow_book(self, borrower):  #check the limit of 5 books and single item before lent, and if there are expired books
        self.borrower = borrower ## add student_id obj
        self.borrowed_date = date.today()
        self.availability = False
        return f"Book is lent to {borrower}"

    def return_book(self):  # remove student_id obj, this should take element from student as well.
        self.borrower = None
        self.borrowed_date = None
        self.availability = True
        return f"Book has been returned"

    def change_condition(self, condition):
        self.condition = condition


class Student:
    def __init__(self, name, surname, email, borrowing_limit=5):
        self.student_id = str(uuid4())
        self.name = name
        self.surname = surname
        self.email = email
        self.books_taken = []
        self.borrowing_limit = borrowing_limit

    def borrow_book(self, ):
        pass  # borrow a book

    def return_book(self, ):
        pass  # return a book

    @property
    def status(self):
        for book in self.books_taken:
            return f"{book.book_id} // Due to {book.borrowed_date+timedelta(days=14)}"


book_1 = Book('Anna Karenina', "Leo Tolstoy", "2013", "1526-4156", "Historical")
book_2 = Book('Yerkir Nairi', "Eghishe Charents", "1920", '1556-4555', 'Novel')

student_1 = Student('John', 'Smith', 'john@example.com')

book_1.add_copy(8)

book_1.available_copies
print(book_1.copies[0])

print(book_1)