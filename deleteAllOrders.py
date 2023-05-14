import sqlite3

conn = sqlite3.connect('SmallShops.db', check_same_thread=False)
curs = conn.cursor()

check = 'Delete All Orders'
delAll = 'DELETE FROM Orders'

print("WARNING: If all orders are deleted, they cannot be recovered")
flag = input(f"Enter '{check}' to delete all orders: ")

if flag == check:
    curs.execute(delAll)
    conn.commit()
    print("All orders deleted")
else:
    print("Orders not deleted")

conn.close()
