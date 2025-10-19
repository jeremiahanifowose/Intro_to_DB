import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",                # Change if your MySQL username is different
    password="jeremiah1234$#2",   # Replace with your actual MySQL password
    database="alx_book_store"   # Database name
)

cursor = connection.cursor()

# Execute the SQL command
cursor.execute("SHOW TABLES;")

# Print all table names
print("Tables in alx_book_store database:")
for (table_name,) in cursor:
    print(f"- {table_name}")

# Close connections
cursor.close()
connection.close()