# Library Management System

## Overview
The Library Management System is a Python Django-based web application designed to automate the management of library books, borrowing processes, and user activities. The system provides a robust https://github.com/PriyankaTaug/LibraryManagement/tree/mainAPI for handling books, users, and loan transactions. With features like tracking borrowed books, overdue management, and detailed reports, this system makes library operations efficient and scalable.

## Features
- **Book Management**: Add, update, delete, and view books.
- **Borrowing System**: Users can borrow and return books, with overdue tracking.
- **User Management**: Manage users who borrow books from the library.
- **Overdue Tracking**: Track overdue books and apply fines if necessary.
- **RESTful API**: Exposes all functionalities through Django REST Framework for integration with external services.

## Tech Stack
- **Backend**: Python, Django, Django REST Framework
- **Database**: Mysql (configured as default)
- **Authentication**: JWT Token Authentication for secure access
- **Testing**: Django Test Framework

## Installation

### Prerequisites
- Python 3.x
- Mysql (optional, default is SQLite)

### Steps to Set Up Locally
1. **Clone the repository**:
   ```bash
   git clone https://github.com/PriyankaTaug/LibraryManagement.git
   cd LibraryManagement




Create a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install dependencies:

pip install -r requirements.txt



Set up the database: Modify the DATABASES settings in settings.py if using Mysql. Then, run the following command:

python manage.py migrate


Run the development server:

python manage.py runserver

