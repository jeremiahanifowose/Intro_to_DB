import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",                # Change if your username is different
    password="jeremiah1234$#2",   # Replace with your actual MySQL password
    database="alx_book_store"   # Database name
)

cursor = connection.cursor()

# Read SQL file
with open("task_2.sql", "r") as file:
    sql_script = file.read()

# Execute multiple SQL statements
for statement in sql_script.split(";"):
    stmt = statement.strip()
    if stmt:
        cursor.execute(stmt + ";")

connection.commit()
print("✅ All tables created successfully in alx_book_store database.")

cursor.close()
connection.close()

    