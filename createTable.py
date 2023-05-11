import sqlite3

conn = sqlite3.connect('SmallShops.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE Inventory
    (inventoryID INTEGER PRIMARY KEY NOT NULL,
     inventoryName VARCHAR(80) NOT NULL,
     department VARCHAR(80) NOT NULL,
     inventoryPrice FLOAT NOT NULL,
     inventoryQuantity FLOAT NOT NULL,
     inventoryValue FLOAT NOT NULL)''')

curs.execute('''CREATE TABLE Users
    (userID INTEGER PRIMARY KEY NOT NULL,
     userName VARCHAR(80) NOT NULL,
     email VARCHAR(80) NOT NULL UNIQUE,
     loginPassword VARCHAR(40) NOT NULL,
     creditCard CHAR(16) NOT NULL,
     city VARCHAR(80) NOT NULL,
     state VARCHAR(80) NOT NULL,
     country VARCHAR(80) NOT NULL,
     address VARCHAR(80) NOT NULL,
     phone CHAR(10) NOT NULL)''')

curs.execute('''CREATE TABLE Orders
    (orderID INTEGER PRIMARY KEY NOT NULL,
     userID INTEGER NOT NULL,
     creditCard CHAR(16) NOT NULL,
     city VARCHAR(80) NOT NULL,
     state VARCHAR(80) NOT NULL,
     country VARCHAR(80) NOT NULL,
     address VARCHAR(80) NOT NULL,
     items VARCHAR(255) NOT NULL,
     pricePerItem VARCHAR(255) NOT NULL,
     quantityPerItem VARCHAR(255) NOT NULL,
     costPerItem VARCHAR(255) NOT NULL,
     originalQuantityPerItem VARCHAR(255) NOT NULL,
     originalValuePerItem VARCHAR(255) NOT NULL,
     alteredQuantityPerItem VARCHAR(255) NOT NULL,
     alteredValuePerItem VARCHAR(255) NOT NULL,
     totalCost FLOAT NOT NULL,
     orderDate DATE NOT NULL)''')

conn.close()
