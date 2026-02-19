import streamlit as st
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
        st.write("ID:", self.book_id)
        st.write("Title:", self.title)
        st.write("Author:", self.author)
        st.write("Available:", self.quantity)
        st.write("----------------------")


# LMS
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed = []
        self.borrow_time = {}

    def borrow_book(self, book):
        if book in self.borrowed:
            st.write("You have already borrowed this book")
        elif book.quantity > 0:
            self.borrowed.append(book)
            book.quantity -= 1

            now = datetime.now(IST)
            free_time = now + timedelta(days=10)
            self.borrow_time[book] = now

            st.write(self.name, "borrowed", book.title)

            st.write("------ BORROW RECEIPT ------")
            st.write("User Name   :", self.name)
            st.write("Book Title  :", book.title)
            st.write("Author      :", book.author)
            st.write("Book ID     :", book.book_id)
            st.write("Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            st.write("Free Time   :", free_time.strftime("%d-%b-%Y %I:%M %p"))
            st.write("-----------------------------")
        else:
            st.write("Book out of stock")

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            book.quantity += 1
            st.write(self.name, "returned", book.title)
            now = datetime.now(IST)
            st.write("------ RETURN RECEIPT ------")
            st.write("User Name   :", self.name)
            st.write("Book Title  :", book.title)
            st.write("Author      :", book.author)
            st.write("Book ID     :", book.book_id)
            st.write("Returned Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            st.write("-----------------------------")
        else:
            st.write("You did not borrow this book")

    def show_borrowed_books(self):
        if len(self.borrowed) == 0:
            st.write("No borrowed books")
        else:
            st.write("Borrowed Books:")
            for book in self.borrowed:
                st.write("-", book.title)

    def renew_book(self, book):
        if book in self.borrowed:
            st.write("Book renewed successfully:", book.title)
            now = datetime.now(IST)
            st.write("------ RENEW RECEIPT ------")
            st.write("User Name   :", self.name)
            st.write("Book Title  :", book.title)
            st.write("Author      :", book.author)
            st.write("Book ID     :", book.book_id)
            st.write("Renew Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            st.write("-----------------------------")
        else:
            st.write("You did not borrow this book")

    def pay_fine(self):
        days = st.number_input("Enter number of days book was borrowed: ", min_value=0, step=1)
        now = datetime.now(IST)

        if days > 10:
            extra_days = days - 10
            fine = extra_days * 10

            st.write("------ FINE RECEIPT ------")
            st.write("User Name   :", self.name)
            st.write("Late Days   :", extra_days)
            st.write("Fine Amount : Rs.", fine)
            st.write("Date & Time :", now.strftime("%d-%b-%Y %I:%M %p"))
            st.write("---------------------------")
        else:
            st.write("No fine. Book returned within 10 days.")


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
    st.write("---- Login ----")
    username = st.text_input("Enter username: ")
    user_id = st.number_input("Enter user ID: ", step=1)
    password = st.text_input("Enter password: ", type="password")

    if st.button("Login"):
        if username in login_db:
            if login_db[username]["user_id"] == user_id and login_db[username]["password"] == password:
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Wrong credentials")
        else:
            st.error("User not found")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    if "library" not in st.session_state:
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
        st.session_state.library = library

    if "user" not in st.session_state:
        st.session_state.user = User(12303486, "Nithin")

    library = st.session_state.library
    user = st.session_state.user

    st.write("Welcome to Library")

    option = st.selectbox(
        "--- Library Menu ---",
        [
            "View Books",
            "Borrow Book",
            "Return Book",
            "View Borrowed Books",
            "Renew Book",
            "Pay Fine",
            "Feedback",
            "Exit",
        ],
    )

    if option == "View Books":
        library.show_books()

    elif option == "Borrow Book":
        bid = st.number_input("Enter book id: ", step=1)
        if st.button("Borrow"):
            book = library.find_book(bid)
            if book:
                user.borrow_book(book)
            else:
                st.write("Book not found")

    elif option == "Return Book":
        bid = st.number_input("Enter book id: ", step=1)
        if st.button("Return"):
            book = library.find_book(bid)
            if book:
                user.return_book(book)
            else:
                st.write("Book not found")

    elif option == "View Borrowed Books":
        user.show_borrowed_books()

    elif option == "Renew Book":
        bid = st.number_input("Enter book id to renew: ", step=1)
        if st.button("Renew"):
            book = library.find_book(bid)
            if book:
                user.renew_book(book)
            else:
                st.write("Book not found")

    elif option == "Pay Fine":
        user.pay_fine()

    elif option == "Feedback":
        feedback = st.text_input("Enter your feedback: ")
        if st.button("Submit Feedback"):
            st.write("Thank you for your feedback!")

    elif option == "Exit":
        st.session_state.logged_in = False
        st.rerun()
