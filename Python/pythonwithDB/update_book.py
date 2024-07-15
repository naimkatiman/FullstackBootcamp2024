import mariadb

def update_book():
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
        book_id = int(input("Enter book ID to update: "))
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        genre = input("Enter new genre: ")
        year = int(input("Enter new publication year: "))
        
        sql = "UPDATE books SET title=%s, author=%s, genre=%s, year=%s WHERE id=%s"
        values = (title, author, genre, year, book_id)
        cursor.execute(sql, values)

        conn.commit()
        print("Book updated successfully!")

    except mariadb.Error as err:
        print("Error updating data: ", err)

    finally:
        if conn:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    update_book()
