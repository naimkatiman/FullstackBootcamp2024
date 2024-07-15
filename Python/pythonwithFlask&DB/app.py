from flask import Flask, render_template, request, redirect, url_for
import mariadb
import db_config

app = Flask(__name__)

def get_db_connection():
    conn = mariadb.connect(
        host=db_config.DB_HOST,
        user=db_config.DB_USER,
        password=db_config.DB_PASSWORD,
        database=db_config.DB_DATABASE
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form.get('year', type=int)
        is_available = request.form.get('is_available', type=lambda x: x == 'on')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO books (title, author, genre, published_year, is_available) VALUES (?, ?, ?, ?, ?)', 
                       (title, author, genre, year, is_available))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

# Edit and Delete 
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form.get('year', type=int)
        is_available = request.form.get('is_available', type=lambda x: x == 'on')
        cursor.execute('UPDATE books SET title=?, author=?, genre=?, published_year=?, is_available=? WHERE id=?', 
                       (title, author, genre, year, is_available, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute('SELECT * FROM books WHERE id=?', (id,))
        book = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id=?', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
