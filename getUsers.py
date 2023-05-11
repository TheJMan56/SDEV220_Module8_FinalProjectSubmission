import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db', check_same_thread=False)
curs = conn.cursor()

getUsers = 'SELECT * FROM Users'

curs.execute(getUsers)
rows = curs.fetchall()

print(rows)

getEmail = 'SELECT * FROM Users WHERE email='
email = input("Enter email: ")
email = str(email)
email = "\"" + email + "\""
print(email)

curs.execute(getEmail + " " + email)
row = curs.fetchone()

print(row)
