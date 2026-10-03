class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def take(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "✅" if self.available else "❌"
        return f"{status} {self.title} ({self.author})"

class Reader:
    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book):
        if book.take():
            self.books.append(book)
            print(f"{self.name} взял(a) книгу: {book.title}")
        else:
            print("Книга уже занята!")

    def return_book(self, book):
        book.return_book()
        if book in self.books:
            self.books.remove(book)
        print(f"{self.name} вернул(a) книгу: {book.title}")

    def __str__(self):
        return f"Читатель: {self.name}, книг: {len(self.books)}"

class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Добавлена книга: {book.title}")

    def add_reader(self, reader):
        self.readers.append(reader)
        print(f"Добавлен читатель: {reader.name}")

    def give_book(self, reader, book):
        if book not in self.books:
            print("Книги нет в библиотеке")
            return
        reader.take_book(book)

    def return_book(self, reader, book):
        reader.return_book(book)

    def show_books(self):
        print("\n Книги в библиотеке:")
        for book in self.books:
            print(f"   {book}")

    def show_readers(self):
        print("\n Читатели:")
        for reader in self.readers:
            print(f"   {reader}")

class LibraryCLI:
    def __init__(self):
        self.library = Library()

    def show_menu(self):
        print("\n1. Добавить книгу")
        print("2. Добавить читателя")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Показать книги")
        print("6. Показать читателей")
        print("0. Выход")

    def add_book(self):
        title = input("Название: ")
        author = input("Автор: ")
        book = Book(title, author)
        self.library.add_book(book)

    def add_reader(self):
        name = input("Имя: ")
        reader = Reader(name)
        self.library.add_reader(reader)

    def give_book(self):
        reader_name = input("Имя читателя: ")
        book_title = input("Название книги: ")

        reader = None
        for r in self.library.readers:
            if r.name == reader_name:
                reader = r
                break

        book = None
        for b in self.library.books:
            if b.title == book_title:
                book = b
                break
        if reader and book:
            self.library.give_book(reader, book)
        else:
            print("Читатель или книга не найдены!")

    def return_book(self):
        reader_name = input("Имя читателя: ")
        book_title = input("Название книги: ")

        reader = None
        for r in self.library.readers:
            if r.name == reader_name:
                reader = r
                break

        book = None
        for b in self.library.books:
            if b.title == book_title:
                book = b
                break

        if reader and book:
            self.library.return_book(reader, book)
        else:
            print("Читатель или книга не найдены!")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Выберите действие: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.add_reader()
            elif choice == "3":
                self.give_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                self.library.show_books()
            elif choice == "6":
                self.library.show_readers()
            elif choice == "0":
                print("До свидания!")
                break
            else:
                print("Неверный выбор")



cli = LibraryCLI()
cli.run()