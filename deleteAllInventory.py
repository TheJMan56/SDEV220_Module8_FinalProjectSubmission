import sqlite3

conn = sqlite3.connect('SmallShops.db', check_same_thread=False)
curs = conn.cursor()

check = 'Delete All Inventory'
delAll = 'DELETE FROM Inventory'

print("WARNING: If all inventory items are deleted, they cannot be recovered")
flag = input(f"Enter '{check}' to delete all inventory items: ")

if flag == check:
    curs.execute(delAll)
    conn.commit()
    print("All inventory deleted")
else:
    print("Inventory not deleted")

conn.close()
