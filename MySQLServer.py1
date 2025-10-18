import mysql.connector
from mysql.connector import Error

def execute_sql_script(file_path):
    connection = None  # ✅ Ensure connection is defined before try block

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='jeremiah1234$#2'  # 🔑 Replace with your actual password
        )

        if connection.is_connected():
            print("Connected to MySQL server.")

            # Read and split SQL commands
            with open(file_path, 'r') as sql_file:
                sql_commands = sql_file.read().split(';')

            cursor = connection.cursor()
            for command in sql_commands:
                command = command.strip()
                if command:
                    try:
                        cursor.execute(command)
                    except Error as e:
                        print(f"Error executing command:\n{command}\n{e}")

            connection.commit()
            cursor.close()
            print("SQL script executed successfully.")

    except Error as e:
        print(f"Error connecting to MySQL server: {e}")

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

def main():
    # 📁 Path to your .sql file
    file_path = 'C:\\Users\\User\\Desktop\\Intro_to_DB\\alx_book_store.sql'
    execute_sql_script(file_path)

if __name__ == "__main__":
    main()
