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

    def __init__(self, book_id, book_name, book_author, book_publishing_house, book_year, book_pages, book_price,
                 book_binding_type):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.book_publishing_house = book_publishing_house
        self.book_year = book_year
        self.book_pages = book_pages
        self.book_price = book_price
        self.book_binding_type = book_binding_type

    def get_book_id(self):
        return self.book_id

    def set_book_id(self, book_id):
        self.book_id = book_id

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

    def __str__(self):
        return 'Book ID = ' + str(
            self.book_id) + '; Book Name  = ' + self.book_name + '; Book Author = ' + self.book_author + '; Book Publishing House = ' + self.book_publishing_house + '; Book year = ' + str(
            self.book_year) + '; Book Pages = ' + str(self.book_pages) + '; Book Price = ' + str(
            self.book_price) + '; Book Binding = ' + self.book_binding_type


book1 = Book(1, 'Gold', 'Abrams', 'Astoria', 1905, 110, 555, 'hard')
book2 = Book(2,'Silver', 'Simons', 'Peresvet', 1891, 205, 1100, 'soft')

Book.add_book_to_list(book1)
Book.add_book_to_list(book2)

Book.print_book_list()
