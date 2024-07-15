import mariadb

def create_book():
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

        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        year = int(input("Enter publication year: "))
        
        sql = "INSERT INTO books (title, author, genre, year) VALUES (%s, %s, %s, %s)"
        values = (title, author, genre, year)
        cursor.execute(sql, values)

        conn.commit()
        print("Book added successfully!")

    except mariadb.Error as err:
        print("Error inserting data: ", err)

    finally:
        if conn:
            conn.close()
            print("Connection closed")

if __name__ == "__main__":
    create_book()
