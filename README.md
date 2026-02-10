# Library-Management-System

📚 Library Management System (Python)

A console-based Library Management System developed using Python, designed to simulate real-world library operations such as user authentication, book borrowing, returning, renewing, fine calculation, and receipt generation.

This project is beginner-friendly and ideal for college mini projects, lab exams, and Python practice.

🚀 Features

🔐 Secure Login System

Username, User ID, and Password authentication

Dictionary-based user database

Input validation with exception handling

📖 Book Management

View available books

Borrow books (with availability check)

Return books

Renew borrowed books

🧾 Receipt Generation

Borrow receipt with:

User name

Book details

Date & Time (IST)

Free borrowing period (10 days)

Fine receipt with:

Late days

Fine amount

Current date & time

⏳ Fine Calculation

10 days free borrowing period

₹10 per extra day (manual input)

Date & time handled using Python datetime module

🗂 Data Handling

Dictionaries for login data

Lists for books and borrowed records

🧠 Beginner-Friendly Design

Simple logic

Menu-driven interface

Easy to understand code structure

🛠 Technologies Used

Language: Python

Concepts:

Object-Oriented Programming (OOP)

Conditional statements

Loops

Lists & Dictionaries

Exception handling

Date & Time (datetime, timezone, timedelta)

Platform: Console / Terminal

📋 System Modules

Login Module

Book Viewing Module

Borrow Book Module

Return Book Module

Renew Book Module

Fine Payment Module

Feedback Module

⏱ Date & Time Handling

Uses Indian Standard Time (IST)

Borrow date & time is recorded automatically

Free period is calculated as:

Borrow Date & Time + 10 days

▶️ How to Run the Project

Clone the repository:

git clone https://github.com/nithin-ponnuru/Library-Management-System.git


Navigate to the project folder:

cd Library-Management-System


Run the program:

python main.py

🔑 Sample Login Credentials
Username : Nithin
User ID  : 12303486
Password : Nithin@2005

📌 Sample Receipt Output
------ BORROW RECEIPT ------
User Name   : Nithin
Book Title  : Harry Potter
Author      : J.K. Rowling
Book ID     : 1
Date & Time : 10-Feb-2026 10:30 AM
Free Time   : 20-Feb-2026 10:30 AM
-----------------------------

📈 Future Enhancements

Multiple user support

Database integration (MySQL / SQLite)

Automatic fine calculation using borrow time

GUI interface (Tkinter / Web)

Export receipts as PDF

🎓 Learning Outcomes

Gained hands-on experience with Python OOP

Learned how real-world systems are modeled in code

Improved logical thinking and problem-solving skills

🤝 Contribution

This project is open for learning and improvement.
Feel free to fork the repository and submit pull requests.

📬 Contact

Developer: Nithin Ponnuru
📂 GitHub: https://github.com/nithin-ponnuru
