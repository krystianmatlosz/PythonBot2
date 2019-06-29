# Book organising bot - Bob v2.0
#
# Co robi bot? 
# 1. Dodaje książkę.
# 2. Dodaje ocenę (od 1 do 10).
# 3. Oznacza jako przeczytaną.
# 4. Wypisuje posiadane książki.
# 5. Filtruje.
# 6. Zapamiętuje wprowadzone dane.
#

class Book:
    def __init__(self, title, authors, rating, read):
        self.title = title
        self.authors = authors
        self.rating = rating
        self.read = read

""" 
Constructor test

b = Book("Pan Tadeusz", "Adam Mickiewicz", 6.5, True)
print(b.title)
print(b.authors)
print(b.rating)
print(b.read)

"""

shelve = []


def add_book(title, authors, rating, read):
    b = Book(title, authors, rating, read)
    shelve.append(b)

def print_book(index, book):
    print("{:4} | {:30} | {:30} | {:5} | {:5}".format(index, book.title, book.authors, book.rating, book.read))
    # {:30} oznacza, że przeznaczam na ten napis max 30 znaków

    """ ugly printing
    print(book.title, " : ", book.authors, " : ", book.rating, " : ", book.read)
    """
    """ # extended form:                             
    print("Title: ", book.title)
    print("Author: ", book.authors)
    print("Rate: ", book.rating)
    print("Read?: ", book.read)
    """

def add_book_from_input():
    print("Adding new book")
    title = input("Title: ")
    authors = input("Authors: ")
    rating = float(input("Rate: "))
    read = input("Is read?: ")
    if read == "Yes":
        read = True
    else:
        read = False

    add_book(title, authors, rating, read)

# add_book_from_input()

add_book("Pan Tadeusz", "Adam Mickiewicz", 6.5, True)
add_book("Zbrodnia i kara", "F. Dostojewski", 7.5, False)
add_book("Ortodoksja", "G. K. Chesterton", 10, True)
add_book("Władca Świata", "Robert Hugh Benson", 9.5, True)


for index in range(len(shelve)):
    print_book(index, shelve[index])

index = int(input("Indeks: "))

book = shelve[index]
book.rating = float(input("Chaning rate on: "))

for index in range(len(shelve)):
    print_book(index, shelve[index])