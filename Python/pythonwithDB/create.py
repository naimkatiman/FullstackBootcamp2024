import mariadb

try:

    conn = mariadb.connect(
        host="localhost",
        user="naim",
        password="AbcPassword123",
        database="pydb"
    )
    print("Connection successful!")
    
    cursor = conn.cursor()

    # Insert data into table
    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    values = ("This Guy", "this_guy@email.com")
    cursor.execute(sql, values)

    conn.commit()
    print("Customer inserted successfully")

except mariadb.Error as err:
    print("Error inserting data: ", err)

finally:
    # Close connection
    if conn:
        conn.close()
        print("Connection closed")
