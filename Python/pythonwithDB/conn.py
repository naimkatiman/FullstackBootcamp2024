import mariadb

try:
    # Replace this with your own connection details
    mydb = mariadb.connect(
        host="localhost",
        user="naim",
        password="AbcPassword123",
        database="pydb"
    )
    print("Connection successful!")

except mariadb.Error as err:
    print("Connection error: ", err)

finally:
    # Close connection
    if mydb:
        mydb.close()
        print("Connection closed")
