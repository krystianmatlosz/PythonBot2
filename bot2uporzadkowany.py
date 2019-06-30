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
# Dodana nowa klasa - BookBot

class Book:
    def __init__(self, title, authors, rating, read):
        self.title = title
        self.authors = authors
        self.set_rating(rating)
        self.read = read

    def set_rating(self, value):
        if value >= 1.0 and value <= 10.0:
            self.rating = value

    def set_read(self, value):
        if value == "Yes":
            self.read = True
        else:
            self.read = False
 
class BookBot:
    def __init__(self):
        self.shelve = []
    
    def add_book(self, title, authors, rating, read):
        b = Book(title, authors, rating, read)
        self.shelve.append(b)
    
    def print_book(self, index):
        book = self.shelve[index]
        print("{:4} | {:30} | {:30} | {:5} | {:5}".format(index, book.title, book.authors, book.rating, book.read))
    
    def add_book_from_input(self):
        print("Adding new book")
        title = input("Title: ")
        authors = input("Authors: ")
        rating = float(input("Rate: "))
        read = input("Is read?: ")
        if read == "Yes":
            read = True
        else:
            read = False

        self.add_book(title, authors, rating, read)
    
    def print_all_books(self):
        for index in range(len(self.shelve)):
            self.print_book(index)

    def set_book_rating(self, book_index, rating):
        book = self.shelve[book_index]
        book.set_rating(rating)
    
    def set_book_read(self, book_index, read):
        book = self.shelve[book_index]
        book.set_read(read)

    
bot = BookBot()


bot.add_book("Pan Tadeusz", "Adam Mickiewicz", 6.5, True)
bot.add_book("Zbrodnia i kara", "F. Dostojewski", 7.5, False)
bot.add_book("Ortodoksja", "G. K. Chesterton", 10, True)
bot.add_book("Władca Świata", "Robert Hugh Benson", 9.5, True)

bot.print_all_books()