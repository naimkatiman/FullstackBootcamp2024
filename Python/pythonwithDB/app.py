from flask import Flask, request, jsonify, render_template
import mariadb
from db_config import HOST, USER, PASSWORD, DATABASE

app = Flask(__name__)

# Connect to DB
def connect_to_database():
    try:
        conn = mariadb.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return conn
    except mariadb.Error as err:
        print(f"Error: {err}")
        return None

# Add a new book to the database
def add_book(title, author, year):
    conn = connect_to_database()
    if not conn:
        return None
    cursor = conn.cursor()
    sql = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
    values = (title, author, year)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return True

# Retrieve all books
def get_books():
    conn = connect_to_database()
    if not conn:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year, is_available FROM books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

# Retrieve a book by ID
def get_book(book_id):
    conn = connect_to_database()
    if not conn:
        return None
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, year, is_available FROM books WHERE id = ?", (book_id,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return book

# Update a book
def update_book(book_id, title, author, year, is_available):
    conn = connect_to_database()
    if not conn:
        return None
    cursor = conn.cursor()
    sql = "UPDATE books SET title = ?, author = ?, year = ?, is_available = ? WHERE id = ?"
    values = (title, author, year, is_available, book_id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return True

# Delete a book
def delete_book(book_id):
    conn = connect_to_database()
    if not conn:
        return None
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

@app.route('/')
def home():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"Connected to database: {db_name[0]}"
    else:
        return "Failed to connect to database"

@app.route('/add_book', methods=['GET', 'POST'])
def add_book_route():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        if not title or not author or not year:
            return jsonify({"error": "Please provide title, author, and year"}), 400

        if add_book(title, author, year):
            return jsonify({"message": "Book added successfully"}), 201
        else:
            return jsonify({"error": "Failed to add book"}), 500
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_books_route():
    books = get_books()
    if books is not None:
        return jsonify(books), 200
    else:
        return jsonify({"error": "Failed to retrieve books"}), 500

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_route(book_id):
    book = get_book(book_id)
    if book is not None:
        return jsonify(book), 200
    else:
        return jsonify({"error": "Failed to retrieve book"}), 500

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book_route(book_id):
    data = request.json
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')
    is_available = data.get('is_available', True)

    if not title or not author or not year:
        return jsonify({"error": "Please provide title, author, and year"}), 400

    if update_book(book_id, title, author, year, is_available):
        return jsonify({"message": "Book updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update book"}), 500

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book_route(book_id):
    if delete_book(book_id):
        return jsonify({"message": "Book deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete book"}), 500

if __name__ == '__main__':
    app.run(debug=True)
