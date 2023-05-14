import sqlite3

conn = sqlite3.connect('SmallShops.db', check_same_thread=False)
curs = conn.cursor()

check = 'Delete All Users'
delAll = 'DELETE FROM Users'

print("WARNING: If all users are deleted, they cannot be recovered")
flag = input(f"Enter '{check}' to delete all users: ")

if flag == check:
    curs.execute(delAll)
    conn.commit()
    print("All users deleted")
else:
    print("Users not deleted")

conn.close()

