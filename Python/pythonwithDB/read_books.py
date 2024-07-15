import mariadb

def read_books():
    conn = None
    try:
        conn = mariadb.connect(
            host="localhost",
            user="naim",
            password="AbcPassword123",
            database="pydb"
        )
        print("Connection successful!")

        cursor = conn.cursor()
        print("1. List all books")
        print("2. Search books by title")
        print("3. Search books by author")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            cursor.execute("SELECT * FROM books")
        elif choice == 2:
            title = input("Enter book title: ")
            cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
        elif choice == 3:
            author = input("Enter book author: ")
            cursor.execute("SELECT * FROM books WHERE author LIKE %s", ('%' + author + '%',))
        else:
            print("Invalid choice")
            return
        
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except mariadb.Error as err:
        print("Error reading data: ", err)

    finally:
        if conn:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    read_books()
