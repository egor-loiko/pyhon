# Вар.1 	Kласс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a)	список книг заданного автора;
# б) список книг, выпущенных после заданного года.

class Book:
    book_list = []

    # def __init__(self, book_id, book_name, book_author, book_publishing_house, book_year, book_pages, book_price,
    #              book_binding_type):
    #     self.book_id = self.set_book_id(book_id)
    #     self.book_name = book_name
    #     self.book_author = book_author
    #     self.book_publishing_house = book_publishing_house
    #     self.book_year = book_year
    #     self.book_pages = book_pages
    #     self.book_price = book_price
    #     self.book_binding_type = book_binding_type

    def get_book_id(self):
        return self.__book_id

    def set_book_id(self, book_id):
        if not self.is_book_id_exist(book_id):
            self.__book_id = book_id
        else:
            print("\33[31m\033[1m {}".format('Same Book ID already exist. Enter another book Id'))
            book_id = int(input("\33[0m {}".format('Enter Book ID: ')))
            self.__book_id = self.set_book_id(book_id)
        return self.get_book_id()

    def is_book_id_exist(self, book_id):
        if Book.get_book_list():
            for i in range(len(Book.book_list)):
                if Book.book_list[i].get_book_id() == book_id:
                    return True
        else:
            return False

    def get_book_name(self):
        return self.__book_name

    def set_book_name(self, book_name):
        self.__book_name = book_name

    def get_book_author(self):
        return self.__book_author

    def set_book_author(self, book_author):
        self.__book_author = book_author

    def get_book_publishing_house(self):
        return self.__book_publishing_house

    def set_book_publishing_house(self, book_publishing_house):
        self.__book_publishing_house = book_publishing_house

    def get_book_year(self):
        return self.__book_year

    def set_book_year(self, book_year):
        self.__book_year = book_year

    def get_book_pages(self):
        return self.__book_pages

    def set_book_pages(self, book_pages):
        self.__book_pages = book_pages

    def get_book_price(self):
        return self.__book_price

    def set_book_price(self, book_price):
        self.__book_price = book_price

    def get_book_binding_type(self):
        return self.__book_binding_type

    def set_book_binding_type(self, book_binding_type):
        self.__book_binding_type = book_binding_type

    @staticmethod
    def get_book_list():
        return Book.book_list

    @staticmethod
    def add_book_to_list(book):
        Book.book_list.append(book)

    @staticmethod
    def remove_book_from_list(book_id):
        checker = 0
        index_store = 0
        for i in range(len(Book.book_list)):
            if Book.book_list[i].__book_id == book_id:
                index_store = i
                checker = 1
        if checker == 0:
            print("\33[31m\033[1m {}".format('Book with ID = \'' + str(book_id) + '\' doesn\'t exist in the List'))
        else:
            Book.book_list.pop(index_store)
            print('Book with ID = \'' + str(book_id) + '\' has been removed from the List!')

    @staticmethod
    def print_book_list():
        if Book.book_list:
            for i in range(len(Book.book_list)):
                print(Book.book_list[i])
        else:
            print("\33[31m\033[1m {}".format('List of book is empty!'))

    @classmethod
    def find_book_by_author(cls, author_name):
        checker = 0
        for i in range(len(cls.book_list)):
            if cls.book_list[i].__book_author.casefold() == author_name.casefold():
                print(cls.book_list[i])
                checker = 1
        if checker == 0:
            print("\33[31m\033[1m {}".format('Book with Author Name = \'' + author_name + '\' has not been found!'))

    @classmethod
    def find_book_by_year_greater(cls, year):
        checker = 0
        for i in range(len(cls.book_list)):
            if cls.book_list[i].__book_year >= year:
                print(cls.book_list[i])
                checker = 1
        if checker == 0:
            print("\33[31m\033[1m {}".format('No books have been found for provided conditions!'))

    def __str__(self):
        return 'Book ID = ' + str(
            self.__book_id) + '; Book Name  = ' + self.__book_name + '; Book Author = ' + self.__book_author + '; Book Publishing House = ' + self.__book_publishing_house + '; Book year = ' + str(
            self.__book_year) + '; Book Pages = ' + str(self.__book_pages) + '; Book Price = ' + str(
            self.__book_price) + '; Book Binding = ' + self.__book_binding_type


def create_new_book():
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
    # book = Book(book_id, book_name, book_author, book_publishing_house, book_year, book_pages, book_price, book_binding_type)
    Book.add_book_to_list(book)
    print("\33[32m\033[1m {}".format('Book is successfully added'))
    print("\33[0m {}".format('Added Book: '))
    print(book)


option = 1
while option != 0:
    print("\33[0m\033[1m {}".format('\nList of options. Please select one'))
    print('1 - Add a book')
    print('2 - Delete book')
    print('3 - List of books')
    print('4 - Find book by Author Name')
    print('5 - Find book released after certain Year')
    print('0 - Exit')
    option = int(input('\nEnter a number of option: '))
    if option == 1:
        print('Starting book creation')
        create_new_book()
    elif option == 2:
        book_id = int(input('\nEnter book Id to remove: '))
        Book.remove_book_from_list(book_id)
    elif option == 3:
        print('\nLIST OF BOOKS: ')
        Book.print_book_list()
    elif option == 4:
        author_name = input('\nEnter author name: ')
        Book.find_book_by_author(author_name)
    elif option == 5:
        year = int(input('\nEnter Year: '))
        Book.find_book_by_year_greater(year)
    elif option == 0:
        print("\033[36m {}".format('\nGood Bye!'))
        option = 0
    else:
        print("\033[33m {}".format('\nThis option is not present in the list, please try again'))
        print("\33[0m {}".format(''))
        continue
