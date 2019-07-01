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
# 3.9 done

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
    
    # ----------- Add -----------
    def add_book(self, title, authors, rating, read):
        b = Book(title, authors, rating, read)
        self.shelve.append(b)
    
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
    
    # ------------ Print --------------
    def print_all_books(self):
        for index in range(len(self.shelve)):
            self.print_book(index)

    def print_book(self, index):
        book = self.shelve[index]
        print("{:4} | {:30} | {:30} | {:5} | {:5}".format(index, book.title, book.authors, book.rating, book.read))

    def print_all_read_books(self):
        for i in range(len(self.shelve)):
            book = self.shelve[i]
            if book.read:
                self.print_book(i)
    
    def print_all_rating_books(self, min_rating, max_rating):
        for i in range(len(self.shelve)):
            book = self.shelve[i]
            if min_rating <= book.rating <= max_rating:
                self.print_book(i)

    # ------------ Set --------------
    def set_book_rating(self, book_index, rating):
        book = self.shelve[book_index]
        book.set_rating(rating)
    
    def set_book_read(self, book_index, read):
        book = self.shelve[book_index]
        book.set_read(read)


    def save_books(self):
        text_books = []

        for i in range(len(self.shelve)):
            book = self.shelve[i]
            text = "{};{};{};{}".format(book.title, book.authors, book.rating, book.read)
            text_books.append(text)
        
        with open('books.csv','w') as f:
            for line in text_books:
                f.write(line + '\n')

        #pass            # pass oznacza, że nie jest wykonywana żadna operacja
                        # wymagane bo ciało funkcji jest oznaczane przez wcięcie
    
    def load_books(self):
        with open('books.csv', 'r') as f:
            for line in f:
                book_list = line.split(';')
                #print(book_list)

                if book_list[3] == 'True\n':
                    read = True
                else:
                    read = False
                self.add_book(book_list[0], book_list[1], float(book_list[2]), read)
    
    
bot = BookBot()
bot.load_books()

#funkcjonalność przeniesiona do konsoli
"""bot.add_book("Pan Tadeusz", "Adam Mickiewicz", 6.5, True)
bot.add_book("Zbrodnia i kara", "F. Dostojewski", 7.5, False)
bot.add_book("Ortodoksja", "G. K. Chesterton", 10, True)
bot.add_book("Władca Świata", "Robert Hugh Benson", 9.5, True)

#test
#bot.print_all_read_books()
#bot.print_all_rating_books(8.0, 10.0)

bot.save_books()
bot.load_books()
bot.print_all_books()"""

while True:
    command = input("Co mam zrobić? ")

    if command == "dodaj":
        bot.add_book_from_input()
    
    elif command == "wszystkie":
        bot.print_all_books()
    
    elif command == "oceń":
        index = int(input("Index: "))
        rating = float(input("Ocena: "))
        bot.set_book_rating(index, rating)
    
    elif command == "przeczytałem":
        index = int(input("Index: "))
        bot.set_book_read(index, True)

    elif command == "pokaż przeczytane":
        bot.print_all_read_books()
    
    elif command == "pokaż ocenione":
        min_rating = float(input('Min ocena: '))
        max_rating = float(input('Max ocena: '))
        bot.print_all_rating_books(min_rating, max_rating)
    
    elif command == "zapisz":
        bot.save_books()

    elif command == "wyjście":
        exit()

    else:
        print("Nie wiem o co Ci chodzi, spróbuj jeszcze raz")