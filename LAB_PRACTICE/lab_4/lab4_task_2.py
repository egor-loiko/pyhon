# Вар.1 	Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# б) список книг, выпущенных после заданного года.

class Book:
    book_id = 0
    book_name = 'noname'
    book_author = 'none'
    book_publishing_house = 'none'
    book_year = 1900
    book_pages = 0
    book_price = 0
    book_binding_type = 'soft'
    book_list = []

    # def __int__(self):
    #     pass

    # def __init__(self, book_id, book_name, book_author, book_publishing_house, book_year, book_pages, book_price,
    #              book_binding_type):
    #     self.book_id = book_id
    #     self.book_name = book_name
    #     self.book_author = book_author
    #     self.book_publishing_house = book_publishing_house
    #     self.book_year = book_year
    #     self.book_pages = book_pages
    #     self.book_price = book_price
    #     self.book_binding_type = book_binding_type
    #

    def get_book_id(self):
        return self.book_id

    def set_book_id(self, book_id):
        if not self.is_book_id_exist(book_id):
            self.book_id = book_id
        else:
            print("\33[31m\033[1m {}".format('Same Book ID already exist'))
            print("\33[0m {}".format('Enter another book ID'))
            book_id1 = int(input('Enter Book ID: '))
            self.book_id = self.set_book_id(book_id1)
        return self.get_book_id()

    def is_book_id_exist(self, book_id):
        if Book.get_book_list():
            for i in range(len(Book.book_list)):
                if Book.book_list[i].get_book_id() == book_id:
                    return True
        else:
            return False

    def get_book_name(self):
        return self.book_name

    def set_book_name(self, book_name):
        self.book_name = book_name

    def get_book_author(self):
        return self.book_author

    def set_book_author(self, book_author):
        self.book_author = book_author

    def get_book_publishing_house(self):
        return self.book_publishing_house

    def set_book_publishing_house(self, book_publishing_house):
        self.book_publishing_house = book_publishing_house

    def get_book_year(self):
        return self.book_year

    def set_book_year(self, book_year):
        self.book_year = book_year

    def get_book_pages(self):
        return self.book_pages

    def set_book_pages(self, book_pages):
        self.book_pages = book_pages

    def get_book_price(self):
        return self.book_price

    def set_book_price(self, book_price):
        self.book_price = book_price

    def get_book_binding_type(self):
        return self.book_binding_type

    def set_book_binding_type(self, book_binding_type):
        self.book_binding_type = book_binding_type

    @staticmethod
    def get_book_list():
        return Book.book_list

    @staticmethod
    def add_book_to_list(book):
        Book.book_list.append(book)

    @staticmethod
    def print_book_list():
        for i in range(len(Book.book_list)):
            print(Book.book_list[i])

    @classmethod
    def find_book_by_author(cls, author_name):
        for i in range(len(cls.book_list)):
            if cls.book_list[i].book_author.casefold() == author_name.casefold():
                print(cls.book_list[i])

    @classmethod
    def find_book_by_year_greater(cls, year):
        for i in range(len(cls.book_list)):
            if cls.book_list[i].book_year >= year:
                print(cls.book_list[i])

    def __str__(self):
        return 'Book ID = ' + str(
            self.book_id) + '; Book Name  = ' + self.book_name + '; Book Author = ' + self.book_author + '; Book Publishing House = ' + self.book_publishing_house + '; Book year = ' + str(
            self.book_year) + '; Book Pages = ' + str(self.book_pages) + '; Book Price = ' + str(
            self.book_price) + '; Book Binding = ' + self.book_binding_type


add_new_book = 'yes'
while add_new_book.casefold() == 'yes':
    print('\nDo you want to add new Book (Yes/No): ')
    add_new_book = input()
    if add_new_book.casefold() == 'yes':
        book = Book()
        book_id = int(input('Enter Book Id: '))
        book.set_book_id(book_id)
        book_name = input('Enter Book Name: ')
        book.set_book_name(book_name)
        book_author = input('Enter Book Author: ')
        book.set_book_author(book_author)
        book_publishing_house = input('Enter Book Publishing House: ')
        book.set_book_publishing_house(book_publishing_house)
        book_year = int(input('Enter Book Year: '))
        book.set_book_year(book_year)
        book_pages = int(input('Enter Book pages: '))
        book.set_book_pages(book_pages)
        book_price = int(input('Enter Book price: '))
        book.set_book_price(book_price)
        book_binding_type = input('Enter Book Binding Type: ')
        book.set_book_binding_type(book_binding_type)
        Book.add_book_to_list(book)
        print("\33[32m\033[1m {}".format('Book is successfully added'))
        print("\33[0m {}".format('Added Book: '))
        print(book)
        # Book.add_book_to_list(
        #     Book(book_id, book_name, book_author, book_publishing_house, book_year, book_pages, book_price,
        #          book_binding_type))
    else:
        if Book.book_list:
            option = 1
            while option != 0:
                print('\nList of options')
                print('1 - Find book by Author Name')
                print('2 - Find book released after certain Year')
                print('3 - List of books')
                print('0 - Exit')
                option = int(input('Select an option: '))
                if option == 1:
                    #print('Option 1 is selected')
                    author_name = input('\nEnter author name: ')
                    Book.find_book_by_author(author_name)
                elif option == 2:
                    #print('Option 2 is selected')
                    year = int(input('\nEnter Year: '))
                    Book.find_book_by_year_greater(year)
                elif option == 3:
                    #print('Option 3 is selected')
                    print('\nLIST OF BOOKS: ')
                    Book.print_book_list()
                else:
                    #print('Exit selected')
                    print("\033[36m {}".format('\nGood Bye!'))
                    option = 0
        else:
            print("\033[36m {}".format('\nOk, Good Bye!'))
