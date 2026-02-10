from datetime import datetime, timezone, timedelta

# IST Timezone (UTC + 05:30)
IST = timezone(timedelta(hours=5, minutes=30))

# Login Details
login_db = {
    "Nithin": {
        "user_id": 12303486,
        "password": "Nithin@2005"
    }
}

# Book Details
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def show_book(self):
        print("ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Available:", self.quantity)
        print("----------------------")


# LMS
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed = []
        self.borrow_time = {}

    def borrow_book(self, book):
        if book in self.borrowed:
            print("You have already borrowed this book")
        elif book.quantity > 0:
            self.borrowed.append(book)
            book.quantity -= 1

            now = datetime.now(IST)
            free_time = now + timedelta(days=10)
            self.borrow_time[book] = now

            print(self.name, "borrowed", book.title)

            print("\n------ BORROW RECEIPT ------")
            print("User Name   :", self.name)
            print("Book Title  :", book.title)
            print("Author      :", book.author)
            print("Book ID     :", book.book_id)
            print("Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            print("Free Time   :", free_time.strftime("%d-%b-%Y %I:%M %p"))
            print("-----------------------------")

        else:
            print("Book out of stock")

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            book.quantity += 1
            print(self.name, "returned", book.title)
            now = datetime.now(IST)
            print("\n------ RETURN RECEIPT ------")
            print("User Name   :", self.name)
            print("Book Title  :", book.title)
            print("Author      :", book.author)
            print("Book ID     :", book.book_id)
            print("Returned Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            print("-----------------------------")
        else:
            print("You did not borrow this book")

    def show_borrowed_books(self):
        if len(self.borrowed) == 0:
            print("No borrowed books")
        else:
            print("Borrowed Books:")
            for book in self.borrowed:
                print("-", book.title)

    def renew_book(self, book):
        if book in self.borrowed:
            print("Book renewed successfully:", book.title)
            now = datetime.now(IST)
            print("\n------ RENEW RECEIPT ------")
            print("User Name   :", self.name)
            print("Book Title  :", book.title)
            print("Author      :", book.author)
            print("Book ID     :", book.book_id)
            print("Renew Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            print("-----------------------------")
        else:
            print("You did not borrow this book")

    def pay_fine(self):
        days = int(input("Enter number of days book was borrowed: "))
        now = datetime.now(IST)

        if days > 10:
            extra_days = days - 10
            fine = extra_days * 10

            print("\n------ FINE RECEIPT ------")
            print("User Name   :", self.name)
            print("Book Title  :", book.title)
            print("Author      :", book.author)
            print("Book ID     :", book.book_id)
            print("Late Days   :", extra_days)
            print("Fine Amount : Rs.", fine)
            print("Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            print("---------------------------")
        else:
            print("No fine. Book returned within 10 days.")


# Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            book.show_book()

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


# Login Function
def login():
    print("---- Login ----")
    username = input("Enter username: ")
    user_id = int(input("Enter user ID: "))
    password = input("Enter password: ")

    if username in login_db:
        if login_db[username]["user_id"] == user_id and login_db[username]["password"] == password:
            print("Login successful!\n")
            return True
        else:
            print("Wrong credentials")
            return False
    else:
        print("User not found")
        return False

# Main Program
if login():
    library = Library()

    library.add_book(Book(1, "Harry Potter", "J.K. Rowling", 5))
    library.add_book(Book(2, "The Hobbit", "Tolkien", 3))
    library.add_book(Book(3, "1984", "George Orwell", 2))
    library.add_book(Book(4, "C++", "Stroustrup", 5))
    library.add_book(Book(5, "Python", "Christos Manolas", 4))
    library.add_book(Book(6, "Java", "Shai Almog", 1))
    library.add_book(Book(7, "C Programming", "Kernighan Brian W.", 8))
    library.add_book(Book(8, "DSA", "Narasimha Karumanchi", 2))
    library.add_book(Book(9, "ASP.NET Core", "Andrew Lock", 0))
    library.add_book(Book(10, "Linux Shell Scripting", "Andrew Mallett", 2))

    user = User(12303486, "Nithin")

    while True:
        print("\nWelcome to Library")
        print("\n--- Library Menu ---")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Borrowed Books")
        print("5. Renew Book")
        print("6. Pay Fine")
        print("7. Feedback")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            bid = int(input("Enter book id: "))
            book = library.find_book(bid)
            if book:
                user.borrow_book(book)
            else:
                print("Book not found")

        elif choice == "3":
            bid = int(input("Enter book id: "))
            book = library.find_book(bid)
            if book:
                user.return_book(book)
            else:
                print("Book not found")

        elif choice == "4":
            user.show_borrowed_books()

        elif choice == "5":
            bid = int(input("Enter book id to renew: "))
            book = library.find_book(bid)
            if book:
                user.renew_book(book)
            else:
                print("Book not found")

        elif choice == "6":
            user.pay_fine()

        elif choice == "7":
            feedback = input("Enter your feedback: ")
            print("Thank you for your feedback!")

        elif choice == "8":
            print("Thank you! Exiting...")
            break

        else:
            print("Invalid choice")
else:
    print("Access denied!")
