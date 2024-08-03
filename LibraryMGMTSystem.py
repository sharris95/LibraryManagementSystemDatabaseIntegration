#LibraryMGMTapp

import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='LibraryDB',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.is_borrowed = False

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

class LibraryManagementSystem:
    def __init__(self):
        self.connection = create_connection()
        if self.connection is None:
            print("Failed to connect to the database. Exiting...")
            exit(1)

    def add_book(self, title, author_id, genre_id, isbn, publication_date):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (title, author_id, genre_id, isbn, publication_date))
            self.connection.commit()
            print("Book added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def borrow_book(self, user_id, book_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE books SET availability = 0 WHERE id = %s"
            cursor.execute(query, (book_id,))
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())"
            cursor.execute(query, (user_id, book_id))
            self.connection.commit()
            print("Book borrowed successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def return_book(self, user_id, book_id):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE books SET availability = 1 WHERE id = %s"
            cursor.execute(query, (book_id,))
            query = "UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
            cursor.execute(query, (user_id, book_id))
            self.connection.commit()
            print("Book returned successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def display_books(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            for row in rows:
                id, title, author_id, genre_id, isbn, publication_date, availability = row
                availability_str = 'Available' if availability else 'Borrowed'
                print(f"ID: {id}, Title: {title}, Author ID: {author_id}, Genre ID: {genre_id}, ISBN: {isbn}, Publication Date: {publication_date.strftime('%Y-%m-%d')}, Availability: {availability_str}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def add_user(self, name, library_id):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (name, library_id))
            self.connection.commit()
            print("User added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def display_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def add_author(self, name, biography):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (name, biography))
            self.connection.commit()
            print("Author added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def display_authors(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM authors")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def add_genre(self, name, description, category):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, description, category))
            self.connection.commit()
            print("Genre added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def display_genres(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM genres")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System with Database Integration!")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Select an option: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                self.genre_operations()
            elif choice == '5':
                break
            else:
                print("Invalid option, please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Display all books")
            print("5. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                title = input("Enter book title: ")
                author_id = input("Enter author ID: ")
                genre_id = input("Enter genre ID: ")
                isbn = input("Enter book ISBN: ")
                publication_date = input("Enter publication date (YYYY-MM-DD): ")
                self.add_book(title, author_id, genre_id, isbn, publication_date)
            elif choice == '2':
                user_id = input("Enter your user ID: ")
                book_id = input("Enter book ID to borrow: ")
                self.borrow_book(user_id, book_id)
            elif choice == '3':
                user_id = input("Enter your user ID: ")
                book_id = input("Enter book ID to return: ")
                self.return_book(user_id, book_id)
            elif choice == '4':
                self.display_books()
            elif choice == '5':
                break
            else:
                print("Invalid option, please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. Display all users")
            print("3. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                name = input("Enter user name: ")
                library_id = input("Enter library ID: ")
                self.add_user(name, library_id)
            elif choice == '2':
                self.display_users()
            elif choice == '3':
                break
            else:
                print("Invalid option, please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. Display all authors")
            print("3. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                self.add_author(name, biography)
            elif choice == '2':
                self.display_authors()
            elif choice == '3':
                break
            else:
                print("Invalid option, please try again.")

    def genre_operations(self):
        while True:
            print("\nGenre Operations:")
            print("1. Add a new genre")
            print("2. Display all genres")
            print("3. Back to main menu")
            choice = input("Select an option: ")
            if choice == '1':
                name = input("Enter genre name: ")
                description = input("Enter genre description: ")
                category = input("Enter genre category: ")
                self.add_genre(name, description, category)
            elif choice == '2':
                self.display_genres()
            elif choice == '3':
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()
