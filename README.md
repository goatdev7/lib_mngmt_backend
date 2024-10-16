# Library Management System API (v1-test)

A RESTful API for managing a library system built with Django and Django REST Framework.

## Features
1. User Registration and Authentication
User registration, login, and logout using Django Allauth and DRF.
Token-based authentication for secure access to API endpoints.
2. Book Management
CRUD (Create, Read, Update, Delete) operations for books.
Each book includes details such as title, author, description, ISBN, and publication date.
User-specific book management (only the user who added the book can update or delete it).
3. Search and Filtering
Search books by title, author, or description.
Filtering and ordering based on various fields, such as publication date and title.

# Installation
Clone the Repository

`git clone https://github.com/yourusername/lib_mngmt.git
cd lib_mngmt`

Create a Virtual Environment

`python3 -m venv env
source env/bin/activate` 

Install Dependencies

`pip install -r requirements.txt`

Run Migrations

`python manage.py makemigrations
python manage.py migrate`

Run the Development Server

`python manage.py runserver`

# Usage
The API can be accessed at `http://127.0.0.1:8000/api/`.
You can use tools like Postman or the Django browsable API to interact with the API.

# API Endpoints
Authentication
`POST /api/auth/registration/` - Register a new user
`POST /api/auth/login/` - Log in and get an authentication token
`POST /api/auth/logout/` - Log out

Books

`GET /api/books/` - List all books
`POST /api/books/` - Create a new book
`GET /api/books/<id>/` - Retrieve a specific book
`PUT /api/books/<id>/` - Update a specific book
`DELETE /api/books/<id>/` - Delete a specific book

User-Specific Books

`GET /api/my-books/` - List all books added by the current user


# Configuration
Environment Variables: Configure environment variables for database settings, secret keys, and other sensitive configurations.
Settings: Customize settings in `settings.py` for your specific environment.


P.S: Just a Practice project building for learning, not an expert. I used ChatGPT where I got stuck :P Its the first version. 
