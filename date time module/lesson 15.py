from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return f'{self.title} - {self.author} ({self.year}) | {"Available" if self.available else "Given"}'

    def is_classic(self):
        return datetime.now().year - self.year > 50


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if book.available:
                        book.available = False
                        due = datetime.now() + timedelta(days=14)
                        print(f'Book loaned. Return until {due.strftime("%Y-%m-%d")}')
                    else:
                        print('Book is already loaned')
                    return
            raise Exception('Book not found.')
        except Exception as ex:
            print(f'Error: {ex}')

    def return_book(self, title):
        try:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if not book.available:
                        book.available = True
                        print(f'Book returned.')
                    else:
                        print('Book is already available.')
                    return
            raise Exception('Book not found.')
        except Exception as ex:
            print(f'Error: {ex}')

    def filter_books(self, **kwargs):
        result = self.books

        for key, value in kwargs.items():
            result = [book for book in result if value == getattr(book, key)]
        for book in result:
            print(book)
        if not result:
            print('There is no matching books available.')

        # results = self.books
        # if 'title' in kwargs:
        #     results = [book for book in results if book.title == kwargs['title']]
        # if 'author' in kwargs:
        #     results = [book for book in results if book.author == kwargs['author']]
        # if 'year' in kwargs:
        #     results = [book for book in results if book.year == kwargs['year']]
        #
        # if results:
        #     for book in results:
        #         print(book)
        # else:
        #     print('Books not found by chosen criteria.')

library = Library()

while True:
    print('\n--- Menu ---')
    print('1. Add book')
    print('2. Browse books')
    print('3. Borrow  book')
    print('4. Return book')
    print('5. Filter books')
    print('6. Quit')

    choice = input('Choose: ')

    if choice == '1':
        title = input('Title: ')
        author = input('Author: ')
        year = input('Year: ')
        book = Book(title, author, year)
        library.add_book(book)
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input('Book title: ')
        library.borrow_book(title)
    elif choice == '4':
        title = input('Book title: ')
        library.return_book(title)
    elif choice == '5':
        key = input('Filter by (title/author/key): ')
        value = input('Meaning: ')
        if key == 'year':
            value = int(value)
        library.filter_books(**{key: value})
    elif choice == '6':
        break
    else:
        print('Wrong choice.')









