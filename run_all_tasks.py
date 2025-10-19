import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",                 # Change if different
    password="jeremiah1234$#2",    # Replace with your actual MySQL password
    database="alx_book_store"
)

cursor = connection.cursor()

# List of SQL files to execute
sql_files = ["task_4.sql", "task_5.sql", "task_6.sql"]

for sql_file in sql_files:
    with open(sql_file, "r") as file:
        sql_script = file.read()

    print(f"\n🔹 Executing {sql_file} ...")
    for statement in sql_script.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ";")
            if "INSERT" in stmt.upper():
                connection.commit()
                print("✅ Data inserted successfully.")
            elif "SHOW" in stmt.upper():
                result = cursor.fetchall()
                for row in result:
                    print(row)

cursor.close()
connection.close()
print("\n🎉 All scripts executed successfully.")