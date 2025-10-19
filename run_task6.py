import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jeremiah1234$#2",  # Replace with your actual MySQL password
    database="alx_book_store"
)

cursor = connection.cursor()

# Execute task_6.sql
with open("task_6.sql", "r") as file:
    sql_script = file.read()

for statement in sql_script.strip().split(";"):
    stmt = statement.strip()
    if stmt:
        cursor.execute(stmt + ";")
        connection.commit()
        print(f"✅ Executed: {stmt[:50]}...")

cursor.close()
connection.close()
print("\n🎉 Task 6 executed successfully. Multiple rows inserted into 'customer'.")