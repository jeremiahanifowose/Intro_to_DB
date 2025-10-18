import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='jeremiah1234$#2'  # 🔑 Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()

    except Error as e:
        print(f"Error connecting to MySQL server: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
