import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jeremiah1234$#2",
    database="alx_book_store"
)

cursor = connection.cursor()

with open("task_5.sql", "r") as file:
    sql_script = file.read()

for statement in sql_script.split(";"):
    stmt = statement.strip()
    if stmt:
        cursor.execute(stmt + ";")

connection.commit()
print("✅ One customer record inserted successfully.")

cursor.close()
connection.close()