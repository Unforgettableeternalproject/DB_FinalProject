import mariadb

user_setting = {
    "user": "411177034",
    "password": "411177034",
    "host": "0.tcp.jp.ngrok.io",
    "port": 11051,
    "database": "411177034"
}

connection = mariadb.connect(**user_setting)
cursor = connection.cursor()

# Disable Auto-Commit
connection.autocommit = False

# retrieving information
some_name = "Georgi"
cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,))

for first_name, last_name in cursor:
    print(f"First name: {first_name}, Last name: {last_name}")

# insert information
try:
    cursor.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria", "DB"))
except mariadb.Error as e:
    print(f"Error: {e}")

connection.commit()
print(f"Last Inserted ID: {cursor.lastrowid}")

cursor.close()
connection.close()