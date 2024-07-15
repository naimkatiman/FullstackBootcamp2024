import mariadb

def delete_book():
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
        book_id = int(input("Enter book ID to delete: "))
        
        sql = "DELETE FROM books WHERE id=%s"
        values = (book_id,)
        cursor.execute(sql, values)

        conn.commit()
        print("Book deleted successfully!")

    except mariadb.Error as err:
        print("Error deleting data: ", err)

    finally:
        if conn:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    delete_book()
