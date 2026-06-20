# Library Management System

A command-line Library Management System built with Python using Object-Oriented Programming (OOP) principles and JSON data persistence.

This application allows users to manage a library inventory by adding, viewing, borrowing, returning, and removing books. Data is stored in JSON files, allowing library data to persist between program sessions.

---

## Features

### Book Management
- Add new books
- View all books
- Remove books from the library

### Borrowing System
- Borrow available books
- Automatically reduce available copies
- Prevent borrowing when no copies are available
- Automatically mark books as "Out of Stock"

### Return System
- Return borrowed books
- Increase available copies
- Restore availability status

### Data Validation
- Prevent empty book titles
- Prevent empty author names
- Prevent negative copy counts
- Validate menu selections
- Handle invalid user input gracefully

### Data Persistence
- Save library data to JSON
- Load existing library data when the application starts
- Preserve UUIDs across sessions

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- UUID
- File Handling
- Property Decorators
- Input Validation

---

## Project Structure

```text
Library/
│
├── data/
│   ├── books.json
│   └── users.json
│
├── helpers/
│   ├── __init__.py
│   └── menu.py
│
├── models/
│   ├── __init__.py
│   ├── admin_functions.py
│   ├── book.py
│   ├── library.py
│   └── user.py
│
├── services/
│   ├── add_book.py
│   ├── borrow_book.py
│   ├── remove_book.py
│   ├── return_book.py
│   └── view_books.py
│
├── utils/
│   └── storage.py
│
├── .gitignore
├── main.py
└── README.md
```

---
## Architecture

### Models

The `models` package contains the core objects used by the system:

- `Book` - Represents books in the library
- `User` - Represents library users
- `Library` - Library-related data management
- `Admin Functions` - Administrative functionality

### Services

The `services` package contains business logic:

- Add books
- Borrow books
- Return books
- Remove books
- View books

### Utilities

The `utils` package contains helper functionality:

- JSON save/load operations
- Data persistence

### Helpers

The `helpers` package contains user interface helpers:

- Menu display and navigation

---
## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Library
```

### Run the Application

```bash
python main.py
```

---

## Example Usage

### Main Menu

```text
Library Management System

1. Add Book
2. View Books
3. Borrow Book
4. Remove Book
5. Return Book
6. Exit
```

### Add a Book

```text
Enter book title: Atomic Habits
Enter book author: James Clear
Enter number of available copies: 5

Atomic Habits by James Clear successfully added to library!
```

### Borrow a Book

```text
1. Atomic Habits
2. Deep Work

Enter the book you want to borrow: 1

Book borrowed successfully!
```

---

## Object-Oriented Design

### Book Class

Each book contains:

- UUID identifier
- Title
- Author
- Status
- Available copies

Validation is implemented using property decorators to ensure data integrity.

### User Class

The project includes a user model to support future user-related features and library expansion.

### Library Class

Provides a foundation for managing collections of books and future library-wide operations.

---

## Data Storage

Library data is stored in:

```text
data/books.json
```

User data is stored in:

```text
data/users.json
```

Data is automatically loaded when the application starts and saved when the application exits.

---

## Future Improvements

Planned enhancements include:

- Search books by title
- Search books by author
- User authentication
- Borrow history tracking
- Due dates and overdue books
- Admin dashboard
- SQLite database integration
- Flask web interface
- REST API support

---

## Learning Outcomes

This project was built to practice:

- Classes and Objects
- Encapsulation
- Property Decorators
- CRUD Operations
- UUID Generation
- JSON Serialization
- File Handling
- Input Validation
- Modular Application Design
- Command-Line Application Development

---

## Author

Michelle Wanjugu

Built as part of a Python software development learning journey.
