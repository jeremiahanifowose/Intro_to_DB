import mysql.connector
from mysql.connector import Error

def create_tables():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='jeremiah1234$#2',  # 🔑 Replace with your actual MySQL password
            database='alx_book_store'
        )

        if connection.is_connected():
            print("Connected to MySQL server.")

            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS AUTHORS (
                    author_id INT PRIMARY KEY,
                    author_name VARCHAR(215)
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS BOOKS (
                    book_id INT PRIMARY KEY,
                    title VARCHAR(130),
                    author_id INT,
                    price DOUBLE,
                    publication_date DATE,
                    FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id)
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS CUSTOMERS (
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR(215),
                    email VARCHAR(215),
                    address TEXT
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ORDERS (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id)
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ORDER_DETAILS (
                    orderdetailid INT PRIMARY KEY,
                    order_id INT,
                    book_id INT,
                    quantity DOUBLE,
                    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
                    FOREIGN KEY (book_id) REFERENCES BOOKS(book_id)
                );
            """)

            connection.commit()
            cursor.close()
            print("All tables created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_tables()
