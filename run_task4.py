import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",                 # Change if different
    password="jeremiah1234$#2",    # Replace with your MySQL password
    database="alx_book_store"
)

cursor = connection.cursor()

with open("task_4.sql", "r") as file:
    sql_script = file.read()

cursor.execute(sql_script)

# Fetch and print the result
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
connection.close()
print("✅ Table structure displayed successfully.")