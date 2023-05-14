import sqlite3

conn = sqlite3.connect('SmallShops.db', check_same_thread=False)
curs = conn.cursor()

delAll = 'DELETE FROM Inventory'

curs.execute(delAll)
conn.commit()

