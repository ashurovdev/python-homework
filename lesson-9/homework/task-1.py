class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExcededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author
        self.is_borrowed = False
    
    def __str__(self):
        status = 'Borrowed' if self.is_borrowed else 'Available'
        return f'{self.title} by {self.author} is {status}'
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExcededException('Limit 3')
        if book.is_borrowed == False:
            book.is_borrowed = True
            self.borrowed_books.append(book)
        else:
            raise BookAlreadyBorrowedException('Book isn\'t available')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
        self.borrowed_books.remove(book)
    
        
    
    def __str__(self):
        books = ', '.join[(book.title for book in self.borrowed_books)] or 'No books'

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_member(self, member):
        self.members.append(member)
    
    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException('Book not found')
    
    def borrow_book(self, member_name, book_title):
        member = self.get_member(member_name)
        book = self.find_book(book_title)
        member.borrow_book(book)
    
    def get_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        
        raise Exception('Member not found')
    
    def return_book(self, member_name, book_title):
        member = self.get_member(member_name)
        book = self.find_book(book_title)
        member.return_book(book)
    
    def show_borrowed_books(self, name):
        member = self.get_member(name)
        books = [book.title for book in member.borrowed_books]
        return books