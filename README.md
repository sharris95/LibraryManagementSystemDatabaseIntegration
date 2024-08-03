Library Management System with Database Integration

Overview

This project is a Library Management System that integrates with a MySQL database. It allows users to manage books, authors, genres, and users, as well as borrow and return books. The system is built using Python and follows object-oriented programming principles.

Features

Book Management: Add, view, borrow, and return books.
User Management: Add and view users.
Author Management: Add and view authors.
Genre Management: Add and view genres.
Database Integration: Uses MySQL to store and manage data.
Setup
Prerequisites
Python 3.x
MySQL
Installation
Clone the repository:


git clone https://github.com/sharris95/LibraryMGMTapp.git
cd LibraryMGMTapp
Create and activate a virtual environment:


python3 -m venv flask_stage_venv
source flask_stage_venv/bin/activate  # On Windows use `flask_stage_venv\Scripts\activate`
Install the required packages:
pip install -r requirements.txt

Set up the MySQL database:

Ensure MySQL is installed and running on your machine.
Refer to your specified folder containing the SQL scripts you created to set up the database schema, such as creating tables for books, users, authors, genres, and borrowed_books.
Execute these scripts using a MySQL client or the MySQL command line.

Running the Application:

Run the application:
python app.py

Using the application:

Follow the on-screen instructions to navigate through the menus and manage books, users, authors, and genres.
Code Structure
app.py: Main application file containing the LibraryManagementSystem class and main menu.
models.py: Contains class definitions for Book, User, Author, and Genre.
database.py: Handles database connection and operations.
Important Notes
Database Credentials: Ensure to replace the placeholder database credentials (your_username and your_password) with your actual MySQL credentials in the create_connection function.
Data Persistence: The system stores data in a MySQL database, ensuring persistence across sessions.

Future Enhancements
User Authentication: Implement a user login system for enhanced security.
Due Dates and Fines: Add functionality to manage due dates for borrowed books and calculate fines for overdue books.
Contributing
Feel free to fork this repository, create a branch, and submit a pull request for any improvements or additional features you would like to see.

License
This project is open-source and available under the MIT License.

Acknowledgements
This project is part of a coding bootcamp curriculum and serves as a practical exercise in integrating Python with databases.

