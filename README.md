LibraryManagementSystemDatabaseIntegration Mini-Project


Overview
The LibraryMGMTapp is a Python-based command-line application designed for managing a library system. It integrates with a MySQL database to manage books, users, authors, and genres. This project builds upon foundational knowledge from Python Object-Oriented Programming (OOP) concepts, extending it with database integration.

Setup Instructions
1. Clone the Repository
First, clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your_username/LibraryMGMTapp.git
cd LibraryMGMTapp
2. Set Up the MySQL Database
Before running the application, ensure you have MySQL installed and set up on your system.

Create the Database and Tables:

Open MySQL Workbench or any MySQL client.
Create a new database named LibraryDB.
Run the SQL scripts provided in the sql_scripts folder to create the necessary tables (books, users, authors, genres, and borrowed_books).
Update Database Configuration:

Replace the placeholder your_username and your_password in the create_connection() function with your MySQL credentials.
3. Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies:

bash
Copy code
python3 -m venv flask_stage_venv
source flask_stage_venv/bin/activate  # On Windows, use `flask_stage_venv\Scripts\activate`
4. Install Required Packages
Install the required Python packages using pip:

bash
Copy code
pip install mysql-connector-python
Running the Application
To start the Library Management System, run the following command:

bash
Copy code
python main.py
Follow the on-screen instructions to navigate through the menu and manage books, users, authors, and genres.

Main Features
Book Operations
Add a New Book: Allows you to add a book to the database.
Borrow a Book: Mark a book as borrowed by a user.
Return a Book: Return a previously borrowed book.
Display All Books: List all books in the library along with their availability status.
User Operations
Add a New User: Register a new user in the system.
Display All Users: List all registered users.
Author Operations
Add a New Author: Add new authors to the system.
Display All Authors: List all authors.
Genre Operations
Add a New Genre: Add new genres to the system.
Display All Genres: List all genres.
Important Notes
Database Integration: The application uses MySQL for storing data. Make sure the database server is running and accessible.
Error Handling: The application includes basic error handling for database operations and user inputs.
