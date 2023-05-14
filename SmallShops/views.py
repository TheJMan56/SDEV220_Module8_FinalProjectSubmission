"""
Programmer: Final Group 5
    Justin W Daily
    Noah Garritt Killian-Ruckman
    Thomas L Layton
Name of Program: SmallShopsRUs
Description: This program provides a full management system for 
inventory items, users, and orders that users can place.  Data in a 
database file is accessed and manipulated through the class methods 
for object classes that represent Inventory, Users, and Orders.

List of classes and class methods:
Inventory - the object class that represents inventory items
    __init__ - creates the object
    newInventoryItem - sets the attributes for the inventory object
        inventoryID - ID value for database; initialized as None
        inventoryName - name of inventory item
        inventoryPrice - price per unit of inventory item
        inventoryQuantity - total amount of inventory item
        inventoryVaue - total value of inventory calculated by multiplying price with quantity
    outputInventoryItem - outputs attributes of inventory object; only functional in the interactive interpreter
    retrieveInventoryItem - uses SQL to define attributes of inventory object with database row using the row's ID value; assigns the inventory object the ID value of the database row
    addInventoryItem - adds inventory object to database; ID value is automatically assigned based on the ID value of the database row
    addNewInventoryItem - sets the attributes for an inventory object that is immediately added to the database
    alterInventoryItem - resets all attributes for an inventory object, except for the ID value
    alterInventoryQuantity - resets the quantity and value of the inventory object
    commitAlteredInventoryItem - commits alterations of inventory object to database, if inventory object has an ID value, which is only obtained by adding the object to the database or retrieving the object from the database
    deleteInventoryItem - deletes inventory object from database, if inventory object has an ID value
Users - the object class that represents customers
    __init__ - creates the object
    newUser - sets the attributes for the user object
        userID - ID value for the database; initialized as None
        userName - name of the user
        email - email of the user; cannot be changed
        loginPassword - password to log the user in
        creditCard - user's credit card
        address - user's address
        state - user's state
        country - user's country
        phone - user's phone number
    outputUser - outputs attributes of user object; only functional in the interactive interpreter
    addUser - adds user object to database; automatically assigns ID value based on ID value of the database row
    addNewUser - sets the attributes for the user object and immediately adds the user object to the database
    retrieveUser - sets the attributes for the user object using the row of a database that is obtained through the ID value of the row
    updateInfo - resets all attributers for the user object; user ID cannot be reset
    commitUpdatedInfo - commits the alterations of the user object to the database using the user ID for the row's ID
    resetPassword - resets the password for the user object
    commitResetPassword - commits the altered password to the database
    deleteUser - deletes the inventory object from the database using the user ID for the row's ID
    loginUser - retrieves a user object from the database using email and password
        emailFlag - flag for if email is in database
        passwordFlag - flag for if input password matches the stored password
Orders - the object class that represents orders
    __init__ - creates the object
    newOrder - sets the attributes for the order object using a user object
        orderID - ID value for the order object; initialized as None
        userID - ID value for the user object placing the order; obtained from the user object
        creditCard - credit card used for the order; obtained from the user object
        address - address used for the order; obtained from the user object
        city - city used for the order; obtained from the user object
        state - state used for the order; obtained from the user object
        country - country used for the order; obtained from the user object
        items - a set that contains all inventory item ID's for inventory items in the order; initialized as empty
        pricePerItem - a dictionary that contains the price per each inventory item ID; initialized as empty
        quantityPerItem - a dictionary that contains the ordered quantity per each inventory item ID; initialized as empty
        costPerItem - a dictionary that contains the ordered cost per each inventory item ID; initialized as empty; derived by multiplying price and quantity
        originalQuantityPerItem - a dictionary that contains the original quantity per each inventory item ID in storage; initalized as empty
        originalValuePerItem - a dictionary that contains the original value per each inventory item ID in storage; initalized as empty
        alteredQuantityPerItem - a dictionary that contains the altered quantity per each inventory item ID in storage; initialized as empty; derived by substracting the original quantity by the ordered quantity
        alteredValuePerItem - a dictionary that contains the altered value per each inventory item ID in storage; initialized as empty; derived by multiplying the price by the altered quantity
    outputOrder - outputs the attributes for the order object; only functions in the interactive interpreter
    retrieveOrder - sets attributes that are unused for other Order class methods; attributes are defined using a row in a database that is obtained through the row's ID value
    addItemWithID - adds an inventory item to the order through direct database access using the row's ID value
        exceededQuantity - flag for it the ordered quantity exceeds to quantity in storage
    addItem - adds an inventory item to the order through an inventory object with an obtained ID value
        exceededQuantity - flag for it the ordered quantity exceeds to quantity in storage
    removeItemWithID - removes an inventory item from the order using the inventory item's ID value
    removeItem - removes an inventory item from the order using the ID value of an inventory object
    changeItemQuantityWithID - changes the ordered quantity of an inventory item using the ID of the inventory item
        exceededQuantity - flag for it the ordered quantity exceeds to quantity in storage
    changeItemQuantity - changes the ordered quantity of an inventory item using the ID of an inventory object
        exceededQuantity - flag for it the ordered quantity exceeds to quantity in storage
    setAddress - resets the full address for the order object
    setPaymentMethod - resets the credit card for the order object
    finalizeOrder - adds the order to the database; automatically assigns the order ID with the database row's ID value
        date - date of the order finalization
    deductInventory - uses the inventory ID values in items to alter the inventory items quantities and values in the database
        quantities and values are altered using the alteredQuantityPerItem and alteredValuePerItem dictionaries
    
    List of views:
    base - opens the main page
    employeeMenu - opens the page with the full function suite
    customerMenu - opens the page with only the functions that customers need for creating orders
    inventoryMenu - opens the page with the full inventory function suite
    listInventory - outputs a list of all stored inventory items
    newInventoryItem - creates a new inventory object with an ID value of None
    outputInventoryItem - outputs the attributes of the current inventory object
    retrieveInventoryItem - creates an inventory object using the ID value for a database row
    addCurrentInventoryItem - adds the current inventory object to the database; automatically assigns the database row's ID to the inventory object's ID value
    addNewInventoryItem - creates a new inventory object and immediately adds the inventory object to the database
    alterInventoryItem - resets the attributes for the inventory object, except for the inventory ID
    alterInventoryQuantity - resets the quantity and value for the inventory object
    commitAlteredInventoryItem - saves the alterations to an inventory object to the database using the inventory ID for the database row's ID value
    deleteCurrentInventoryItem - deletes inventory object from the database using inventory ID for the database row's ID value
    deleteSelectedInventoryItem - deletes an inventory row from the database using the row's ID value
    userMenu - opens the page with the full user function suite
    listUsers - outputs a list of all stored users
    newUser - creates a new user object with an ID value of None
    outputUser - outputs the attributes of the current user object
    addCurrentUser - adds the the current user object to the database; automatically assigns the database row's ID to the user object's ID value
    addNewUser - creates a new user object and immediately adds teh user object to the database
    retrieveUser - creates a user object using the ID value for a database row
    updateUserInfo - resets the attributes for the user object, except for user ID and email
    commitUpdatedInfo - commits the alterations of the user object to the database using user ID as the database row's ID value
    resetPassword - resets the password for the user object
    commitResetPassword - commits the altered password of the user object to the database using the user ID as the database row's ID value
    deleteCurrentUser - deletes the current user object from the database using the user ID as the database row's ID value
    deleteSelectedUser - deletes a user row from the database using the row's ID value
    loginUser - creates a user object using the email and password of a database row
    orderMenu - opens the page with the full order function suite
    listOrders - outputs a list of all stored orders
    newOrder - creates a new order object using a user object; has an ID value of None
    outputOrder - outputs the attributes of the current order object
    retrieveOrder - outputs the attributes of an order stored in the database
    setAddress - resets the full address for the order object
    setPaymentMethod - resets the credit card for the order object
    addItem - adds an inventory item to the order through an inventory object
    addItemWithID - adds an inventory item to the order using a database row's ID value
    removeItem - removes an inventory item using the ID value of an inventory object
    removeItemWithID - removes an inventory item using a manually entered ID value for an inventory object
    changeItemQuantity - changes the ordered quantity of an inventory item using the ID value of an inventory object
    changeItemQuantityWithID - changes the ordered quantity of an inventory item using a manually entered ID value
    finalizeOrder - adds the order object to the database; automatically assigns an ID value using the database row's ID value; automatically adds a date to the order object
        automatically deducts the ordered quantity of each inventory item from the database
"""

from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from datetime import date

conn = sqlite3.connect('SmallShops.db', check_same_thread=False)
curs = conn.cursor()

# Create your views here.

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def obtainAllInventoryItems():
    sql = 'SELECT * FROM Inventory'
    curs.execute(sql)
    rows = curs.fetchall()
    return rows

def obtainInventoryItem(inventoryID):
    sql = 'SELECT * FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    row = curs.fetchone()
    return row

def deleteInventoryItem(inventoryID):
    sql = 'DELETE FROM Inventory WHERE inventoryID ='
    inventoryID = str(inventoryID)
    curs.execute(sql + " " + inventoryID)
    conn.commit()

def obtainAllUsers():
    sql = 'SELECT * FROM Users'
    curs.execute(sql)
    rows = curs.fetchall()
    return rows

def obtainUser(userID):
    sql = 'SELECT * FROM Users WHERE userID ='
    userID = str(userID)
    curs.execute(sql + " " + userID)
    row = curs.fetchone()
    return row

def deleteUser(userID):
    sql = 'DELETE FROM Users WHERE userID ='
    useID = str(userID)
    curs.execute(sql + " " + userID)
    conn.commit()

def obtainAllOrders():
    sql = 'SELECT * FROM Orders'
    curs.execute(sql)
    rows = curs.fetchall()
    return rows

def obtainOrder(orderID):
    sql = 'SELECT * FROM Orders WHERE orderID ='
    orderID = str(orderID)
    curs.execute(sql + " " + orderID)
    row = curs.fetchone()
    return row

class Inventory():
    def __init__(self):
        pass

    def newInventoryItem(self, inventoryName, department, inventoryPrice, inventoryQuantity):
        self.inventoryID = None
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = float(inventoryPrice) * float(inventoryQuantity)
        self.inventoryValue = inventoryValue

    def outputInventoryItem(self):
        print(f"Inventory Item ID: {self.inventoryID}")
        print(f"Inventory Item Name: {self.inventoryName}")
        print(f"Inventory Item Department: {self.department}")
        print(f"Inventory Item Price: {self.inventoryPrice}")
        print(f"Inventory Item Quantity: {self.inventoryQuantity}")
        print(f"Inventory Item Value: {self.inventoryValue}")

    def retrieveInventoryItem(self, inventoryID):
        getInventory = 'SELECT * FROM Inventory WHERE inventoryID ='
        inventoryID = str(inventoryID)
        curs.execute(getInventory + " " + inventoryID)
        inventoryItem = curs.fetchone()
        self.inventoryID = inventoryItem[0]
        self.inventoryName = inventoryItem[1]
        self.department = inventoryItem[2]
        self.inventoryPrice = inventoryItem[3]
        self.inventoryQuantity = inventoryItem[4]
        self.inventoryValue = inventoryItem[5]

    def addInventoryItem(self):
        insInventory = 'INSERT INTO Inventory (inventoryName, \
        department, inventoryPrice, inventoryQuantity, inventoryValue) \
        VALUES (?, ?, ?, ?, ?)'
        curs.execute(insInventory, (self.inventoryName, \
                                    self.department, self.inventoryPrice, \
                                    self.inventoryQuantity, self.inventoryValue))
        conn.commit()
        inventoryID = curs.lastrowid
        self.inventoryID = inventoryID

    def addNewInventoryItem(self, inventoryName, department, inventoryPrice, inventoryQuantity):
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = float(inventoryPrice) * float(inventoryQuantity)
        self.inventoryValue = inventoryValue

        insInventory = 'INSERT INTO Inventory (inventoryName, \
        department, inventoryPrice, inventoryQuantity, inventoryValue) \
        VALUES (?, ?, ?, ?, ?)'
        curs.execute(insInventory, (self.inventoryName, \
                                    self.department, self.inventoryPrice, \
                                    self.inventoryQuantity, self.inventoryValue))
        conn.commit()
        inventoryID = curs.lastrowid
        self.inventoryID = inventoryID

    def alterInventoryItem(self, inventoryName, department, inventoryPrice, inventoryQuantity):
        self.inventoryName = inventoryName
        self.department = department
        self.inventoryPrice = inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def alterInventoryQuantity(self, inventoryQuantity):
        inventoryPrice = self.inventoryPrice
        self.inventoryQuantity = inventoryQuantity
        inventoryValue = inventoryPrice * inventoryQuantity
        self.inventoryValue = inventoryValue

    def commitAlteredInventoryItem(self):
        updInventory = 'UPDATE Inventory SET inventoryName = ?, \
                        department = ?, inventoryPrice = ?, inventoryQuantity = ?, \
                        inventoryValue = ? \
                        WHERE inventoryID = ?'
        curs.execute(updInventory, (self.inventoryName, self.department, \
                                    self.inventoryPrice, self.inventoryQuantity, \
                                    self.inventoryValue, self.inventoryID))
        conn.commit()

    def deleteInventoryItem(self):
        delInventory = 'DELETE FROM Inventory WHERE inventoryID ='
        inventoryID = str(self.inventoryID)
        curs.execute(delInventory + " " + inventoryID)
        conn.commit()

class User():
    def __init__(self):
        pass

    def newUser(self, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userID = None
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone

    def outputUser(self):
        print(f"User ID: {self.userID}")
        print(f"User Name: {self.userName}")
        print(f"User Email: {self.email}")
        print(f"User Passowrd: {self.loginPassword}")
        print(f"User Credit Card: {self.creditCard}")
        print(f"User Address: {self.address}")
        print(f"User City: {self.city}")
        print(f"User State: {self.state}")
        print(f"User Country: {self.country}")
        print(f"Phone: {self.phone}")

    def addUser(self):
        insUser = 'INSERT INTO Users (userName, email, \
        loginPassword, creditCard, address, city, state, country, phone) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insUser, (self.userName, self.email, \
                               self.loginPassword, self.creditCard, self.address, \
                               self.city, self.state, self.country, self.phone))
        conn.commit()
        userID = curs.lastrowid
        self.userID = userID
    
    def addNewUser(self, userName, email, loginPassword, creditCard, address, city, state, country, phone):
        self.userName = userName
        self.email = email
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        insUser = 'INSERT INTO Users (userName, email, \
        loginPassword, creditCard, address, city, state, country, phone) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insUser, (self.userName, self.email, \
                               self.loginPassword, self.creditCard, self.address, \
                               self.city, self.state, self.country, self.phone))
        conn.commit()
        userID = curs.lastrowid
        self.userID = userID

    def retrieveUser(self, userID):
        getUser = 'SELECT * FROM Users WHERE userID ='
        userID = str(userID)
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()
        self.userID = userData[0]
        self.userName = userData[1]
        self.email = userData[2]
        self.loginPassword = userData[3]
        self.creditCard = userData[4]
        self.city = userData[5]
        self.state = userData[6]
        self.country = userData[7]
        self.address = userData[8]
        self.phone = userData[9]

    def updateInfo(self, userName, loginPassword, creditCard, address, city, state, country, phone):
        self.userName = userName
        self.loginPassword = loginPassword
        self.creditCard = creditCard
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone

    def commitUpdatedInfo(self):
        updUser = 'UPDATE Users SET userName = ?, loginPassword = ?, \
                   creditCard = ?, address = ?, city = ?, state = ?, \
                   country = ?, phone = ? \
                   WHERE userID = ?'
        curs.execute(updUser, (self.userName, self.loginPassword, \
                               self.creditCard, self.address, self.city, \
                               self.state, self.country, self.phone, \
                               self.userID))
        conn.commit()

    def resetPassword(self, loginPassword):
        self.loginPassword = loginPassword

    def commitResetPassword(self):
        updPassword = 'UPDATE Users SET loginPassword = ? WHERE userID = ?'
        curs.execute(updPassword, (self.loginPassword, self.userID))
        conn.commit()

    def deleteUser(self):
        delUser = 'DELETE FROM Users WHERE userID ='
        userID = str(self.userID)
        curs.execute(delUser + " " + userID)
        conn.commit()

    def loginUser(self, email, inputPassword):
        email = str(email)
        email = "\"" + email + "\""
        getUser = 'SELECT * FROM Users WHERE email ='
        
        curs.execute(getUser + " " + email)
        userData = curs.fetchone()

        if userData == None:
            self.emailFlag = False
        else:
            self.emailFlag = True

            correctPassword = userData[3]
        
            if inputPassword == correctPassword:
                self.passwordFlag = True
                self.userID = userData[0]
                self.userName = userData[1]
                self.email = userData[2]
                self.loginPassword = userData[3]
                self.creditCard = userData[4]
                self.city = userData[5]
                self.state = userData[6]
                self.country = userData[7]
                self.address = userData[8]
                self.phone = userData[9]
            else:
                self.passwordFlag = False

class Order():
    def __init__(self):
        pass

    def newOrder(self, user):
        items = set()
        pricePerItem = {}
        quantityPerItem = {}
        costPerItem = {}
        originalQuantityPerItem = {}
        originalValuePerItem = {}
        alteredQuantityPerItem = {}
        alteredValuePerItem = {}
        totalCost = 0
        self.orderID = None
        self.userID = user.userID
        self.creditCard = user.creditCard
        self.address = user.address
        self.city = user.city
        self.state = user.state
        self.country = user.country
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost
        self.date = None

    def outputOrder(self):
        print(f"Order ID: {self.orderID}")
        print(f"User ID: {self.userID}")
        print(f"Credit Card: {self.creditCard}")
        print(f"Address: {self.address}")
        print(f"City: {self.city}")
        print(f"State: {self.state}")
        print(f"Country: {self.country}")
        print(f"Items: {self.items}")
        print(f"Price Per Item: {self.pricePerItem}")
        print(f"Quantity Per Item: {self.quantityPerItem}")
        print(f"Cost Per Item: {self.costPerItem}")
        print(f"Original Quantity Per Item: {self.originalQuantityPerItem}")
        print(f"Original Value Per Item: {self.originalValuePerItem}")
        print(f"Altered Quantity Per Item: {self.alteredQuantityPerItem}")
        print(f"Altered Value Per Item: {self.alteredValuePerItem}")
        print(f"Total Cost: {self.totalCost}")

    def retrieveOrder(self, orderID):
        orderID = str(orderID)
        getOrder = 'SELECT * FROM Orders WHERE orderID ='
        curs.execute(getOrder + " " + orderID)
        orderInfo = curs.fetchone()
        self.retrievedOrderID = orderInfo[0]
        self.retrievedUserID = orderInfo[1]
        self.retrievedCreditCard = orderInfo[2]
        self.retrievedCity = orderInfo[3]
        self.retrievedState = orderInfo[4]
        self.retrievedCountry = orderInfo[5]
        self.retrievedAddress = orderInfo[6]
        self.retrievedItems = orderInfo[7]
        self.retrievedPricePerItem = orderInfo[8]
        self.retrievedQuantityPerItem = orderInfo[9]
        self.retrievedCostPerItem = orderInfo[10]
        self.retrievedOriginalQuantityPerItem = orderInfo[11]
        self.retrievedOriginalValuePerItem = orderInfo[12]
        self.retrievedAlteredQuantityPerItem = orderInfo[13]
        self.retrievedAlteredValuePerItem = orderInfo[14]
        self.retrievedTotalCost = orderInfo[15]
        self.retrievedDate = orderInfo[16]

    def addItemWithID(self, inventoryID, orderQuantity):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = float(self.totalCost)

        inventoryItem = obtainInventoryItem(inventoryID)
        inventoryID = inventoryItem[0]
        inventoryPrice = float(inventoryItem[3])
        inventoryQuantity = float(inventoryItem[4])
        inventoryValue = float(inventoryItem[5])

        if orderQuantity > inventoryQuantity:
            self.exceededQuantity = True
        else:
            self.exceededQuantity = False
            alteredInventoryQuantity = inventoryQuantity - orderQuantity
            alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
            orderPrice = inventoryPrice * orderQuantity
            totalCost += orderPrice
            items.add(inventoryID)
            pricePerItem[inventoryID] = inventoryPrice
            quantityPerItem[inventoryID] = orderQuantity
            costPerItem[inventoryID] = orderPrice
            originalQuantityPerItem[inventoryID] = inventoryQuantity
            alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
            originalValuePerItem[inventoryID] = inventoryValue
            alteredValuePerItem[inventoryID] = alteredInventoryValue
        
            self.items = items
            self.pricePerItem = pricePerItem
            self.quantityPerItem = quantityPerItem
            self.costPerItem = costPerItem
            self.originalQuantityPerItem = originalQuantityPerItem
            self.originalValuePerItem = originalValuePerItem
            self.alteredQuantityPerItem = alteredQuantityPerItem
            self.alteredValuePerItem = alteredValuePerItem
            self.totalCost = totalCost

    def addItem(self, inventoryItem, orderQuantity):
        inventoryID = inventoryItem.inventoryID
        inventoryQuantity = inventoryItem.inventoryQuantity
        inventoryPrice = inventoryItem.inventoryPrice
        inventoryValue = inventoryItem.inventoryValue
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        orderPrice = inventoryPrice * orderQuantity
        
        items.add(inventoryID)
        pricePerItem[inventoryID] = inventoryPrice
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        originalQuantityPerItem[inventoryID] = inventoryItem.inventoryQuantity
        alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
        originalValuePerItem[inventoryID] = inventoryItem.inventoryValue
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def removeItemWithID(self, inventoryID):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = self.totalCost

        inventoryID = int(inventoryID)
        totalCost = totalCost - costPerItem[inventoryID]
        items.remove(inventoryID)
        del pricePerItem[inventoryID]
        del quantityPerItem[inventoryID]
        del costPerItem[inventoryID]
        del originalQuantityPerItem[inventoryID]
        del originalValuePerItem[inventoryID]
        del alteredQuantityPerItem[inventoryID]
        del alteredValuePerItem[inventoryID]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def removeItem(self, iventoryItem):
        inventoryID = inventoryItem.inventoryID
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = self.totalCost
        
        inventoryID = int(inventoryID)
        totalCost = totalCost - costPerItem[inventoryID]
        items.remove(inventoryID)
        del pricePerItem[inventoryID]
        del quantityPerItem[inventoryID]
        del costPerItem[inventoryID]
        del originalQuantityPerItem[inventoryID]
        del originalValuePerItem[inventoryID]
        del alteredQuantityPerItem[inventoryID]
        del alteredValuePerItem[inventoryID]
        
        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def changeItemQuantityWithID(self, inventoryID, orderQuantity):
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        inventoryID = int(inventoryID)
        inventoryPrice = float(pricePerItem[inventoryID])
        inventoryQuantity = originalQuantityPerItem[inventoryID]
        orderQuantity = float(orderQuantity)

        self.exceededQuantity = False
        orderPrice = inventoryPrice * orderQuantity
        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        alteredQuantityPerItem[inventoryID] = alteredInventoryQuantity
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def changeItemQuantity(self, inventoryItem, orderQuantity):
        inventoryID = inventoryItem.inventoryID
        inventoryQuantity = inventoryItem.inventoryQuantity
        inventoryPrice = inventoryItem.inventoryPrice
        inventoryValue = inventoryItem.inventoryValue
        items = set(self.items)
        pricePerItem = dict(self.pricePerItem)
        quantityPerItem = dict(self.quantityPerItem)
        costPerItem = dict(self.costPerItem)
        originalQuantityPerItem = dict(self.originalQuantityPerItem)
        originalValuePerItem = dict(self.originalValuePerItem)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        totalCost = 0

        orderQuantity = float(orderQuantity)
        alteredInventoryQuantity = inventoryQuantity - orderQuantity
        alteredInventoryValue = inventoryPrice * alteredInventoryQuantity
        orderPrice = inventoryPrice * orderQuantity
        
        pricePerItem[inventoryID] = inventoryPrice
        quantityPerItem[inventoryID] = orderQuantity
        costPerItem[inventoryID] = orderPrice
        originalQuantityPerItem[inventoryID] = inventoryItem.inventoryQuantity
        alteredQuantityPerItem[inventoryID]= alteredInventoryQuantity
        originalValuePerItem[inventoryID] = inventoryItem.inventoryValue
        alteredValuePerItem[inventoryID] = alteredInventoryValue

        for key in costPerItem:
            totalCost += costPerItem[key]

        self.items = items
        self.pricePerItem = pricePerItem
        self.quantityPerItem = quantityPerItem
        self.costPerItem = costPerItem
        self.originalQuantityPerItem = originalQuantityPerItem
        self.originalValuePerItem = originalValuePerItem
        self.alteredQuantityPerItem = alteredQuantityPerItem
        self.alteredValuePerItem = alteredValuePerItem
        self.totalCost = totalCost

    def setAddress(self, address, city, state, country):
        self.address = address
        self.city = city
        self.state = state
        self.country = country

    def setPaymentMethod(self, creditCard):
        self.creditCard = creditCard

    def finalizeOrder(self):
        self.date = str(date.today())
        insOrder = 'INSERT INTO Orders (userID, creditCard, \
        address, city, state, country, items, pricePerItem, \
        quantityPerItem, costPerItem, originalQuantityPerItem, \
        originalValuePerItem, alteredQuantityPerItem, alteredValuePerItem, \
        totalCost, orderDate) \
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        curs.execute(insOrder, (self.userID, self.creditCard, \
                                self.address, self.city, self.state, \
                                self.country, str(self.items), str(self.pricePerItem), \
                                str(self.quantityPerItem), str(self.costPerItem), \
                                str(self.originalQuantityPerItem), str(self.originalValuePerItem), \
                                str(self.alteredQuantityPerItem), str(self.alteredValuePerItem), \
                                self.totalCost, self.date))
        conn.commit()
        orderID = curs.lastrowid
        self.orderID = orderID

    def deductInventory(self):
        items = set(self.items)
        alteredQuantityPerItem = dict(self.alteredQuantityPerItem)
        alteredValuePerItem = dict(self.alteredValuePerItem)
        updQuantity = 'UPDATE Inventory SET inventoryQuantity = ?, \
                      inventoryValue = ? WHERE inventoryID = ?'
        for inventoryID in items:
            inventoryQuantity = alteredQuantityPerItem[inventoryID]
            inventoryValue = alteredValuePerItem[inventoryID]
            curs.execute(updQuantity, (inventoryQuantity, inventoryValue, inventoryID))
            conn.commit()

def base(request):
    return render(request, "base.html")

def employeeMenu(request):
    return render(request, "employeeMenu.html")

def customerMenu(request):
    return render(request, "customerMenu.html")

def inventoryMenu(request):
    return render(request, "inventoryMenu.html")

def listInventory(request):
    inventoryList = []
    inventoryList = obtainAllInventoryItems()
    return render(request, "inventoryList.html", {"inventoryList": inventoryList})

def newInventoryItem(request):
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])
    
    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.newInventoryItem(inventoryName, department, inventoryPrice, inventoryQuantity)

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def outputInventoryItem(request):
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def retrieveInventoryItem(request):
    inventoryID = request.GET["inventoryID"]

    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.retrieveInventoryItem(inventoryID)

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def addCurrentInventoryItem(request):
    inventoryItem.addInventoryItem()

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def addNewInventoryItem(request):
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])
    
    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.newInventoryItem(inventoryName, department, inventoryPrice, inventoryQuantity)
    inventoryItem.addInventoryItem()

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def alterInventoryItem(request):
    inventoryName = request.GET["inventoryName"]
    department = request.GET["department"]
    inventoryPrice = float(request.GET["inventoryPrice"])
    inventoryQuantity = float(request.GET["inventoryQuantity"])

    inventoryItem.alterInventoryItem(inventoryName, department, inventoryPrice, inventoryQuantity)
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def alterInventoryQuantity(request):
    inventoryQuantity = float(request.GET["inventoryQuantity"])

    inventoryItem.alterInventoryQuantity(inventoryQuantity)
    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def commitAlteredInventoryItem(request):
    inventoryItem.commitAlteredInventoryItem()

    return render(request, "inventoryItem.html", {"inventoryID": inventoryItem.inventoryID, "inventoryName": inventoryItem.inventoryName, "department": inventoryItem.department, "inventoryPrice": inventoryItem.inventoryPrice, "inventoryQuantity": inventoryItem.inventoryQuantity, "inventoryValue": inventoryItem.inventoryValue})

def deleteCurrentInventoryItem(request):
    inventoryItem.deleteInventoryItem()

    return HttpResponse("<html><body><p>Inventory Item Deleted</p></body></html>")

def deleteSelectedInventoryItem(request):
    inventoryID = str(request.GET["inventoryID"])
    global inventoryItem
    inventoryItem = Inventory()
    inventoryItem.retrieveInventoryItem(inventoryID)
    inventoryItem.deleteInventoryItem()

    return HttpResponse("<html><body><p>Inventory Item Deleted</p></body></html>")

def userMenu(request):
    return render(request, "userMenu.html")

def listUsers(request):
    userList = []
    userList = obtainAllUsers()
    return render(request, "userList.html", {"userList": userList})

def newUser(request):
    userName = request.GET["userName"]
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]
    
    global user
    user = User()
    user.newUser(userName, email, loginPassword, creditCard, address, city, state, country, phone)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def outputUser(request):
    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def addCurrentUser(request):
    user.addUser()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def addNewUser(request):
    userName = request.GET["userName"]
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]
    
    global user
    user = User()
    user.newUser(userName, email, loginPassword, creditCard, address, city, state, country, phone)
    user.addUser()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def retrieveUser(request):
    userID = request.GET["userID"]

    global user
    user = User()
    user.retrieveUser(userID)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def updateUserInfo(request):
    userName = request.GET["userName"]
    loginPassword = request.GET["loginPassword"]
    creditCard = request.GET["creditCard"]
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]
    phone = request.GET["phone"]

    user.updateInfo(userName, loginPassword, creditCard, address, city, state, country, phone)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def commitUpdatedInfo(request):
    user.commitUpdatedInfo()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def resetPassword(request):
    loginPassword = request.GET["loginPassword"]

    user.resetPassword(loginPassword)

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def commitResetPassword(request):
    user.commitResetPassword()

    return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def deleteCurrentUser(request):
    user.deleteUser()

    return HttpResponse("<html><body><p>User Deleted</p></body></html>")

def deleteSelectedUser(request):
    userID = request.GET["userID"]

    global user
    user = User()
    user.retrieveUser(userID)
    user.deleteUser()

    return HttpResponse("<html><body><p>User Deleted</p></body></html>")

def loginUser(request):
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]

    global user
    user = User()
    user.loginUser(email, loginPassword)

    if user.emailFlag == False:
        return HttpResponse("<html><body><p>Incorrect Email</p></body></html>")
    elif user.passwordFlag == False:
        return HttpResponse("<html><body><p>Incorrect Password</p></body></html>")
    else:
        return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})

def orderMenu(request):
    return render(request, "orderMenu.html")

def listOrders(request):
    orderList = []
    orderList = obtainAllOrders()
    return render(request, "orderList.html", {"orderList": orderList})

def newOrder(request):
    global order
    order = Order()
    order.newOrder(user)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": order.date})

def outputOrder(request):
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": order.date})

def retrieveOrder(request):
    orderID = request.GET["orderID"]
    
    global retrievedOrder
    retrievedOrder = Order()
    retrievedOrder.retrieveOrder(orderID)

    return render(request, "order.html", {"orderID": retrievedOrder.retrievedOrderID,"userID": retrievedOrder.retrievedUserID,"creditCard": retrievedOrder.retrievedCreditCard,"city": retrievedOrder.retrievedCity,"state": retrievedOrder.retrievedState,"country": retrievedOrder.retrievedCountry,"address": retrievedOrder.retrievedAddress,"items": retrievedOrder.retrievedItems,"pricePerItem": retrievedOrder.retrievedPricePerItem,"quantityPerItem": retrievedOrder.retrievedQuantityPerItem,"costPerItem": retrievedOrder.retrievedCostPerItem,"originalQuantityPerItem": retrievedOrder.retrievedOriginalQuantityPerItem,"originalValuePerItem": retrievedOrder.retrievedOriginalValuePerItem,"alteredQuantityPerItem": retrievedOrder.retrievedAlteredQuantityPerItem,"alteredValuePerItem": retrievedOrder.retrievedAlteredValuePerItem,"totalCost": retrievedOrder.retrievedTotalCost,"date": retrievedOrder.retrievedDate})

def setAddress(request):
    city = request.GET["city"]
    state = request.GET["state"]
    country = request.GET["country"]
    address = request.GET["address"]

    order.setAddress(address, city, state, country)
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def setPaymentMethod(request):
    creditCard = request.GET["creditCard"]

    order.setPaymentMethod(creditCard)
    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def addItem(request):
    orderQuantity = float(request.GET["orderQuantity"])
    if orderQuantity > inventoryItem.inventoryQuantity:
        return HttpResponse("<html><body><p>Order Quantity must be less than or equal to Inventory Quantity</p></body></html>")
    else:
        order.addItem(inventoryItem, orderQuantity)
        return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def addItemWithID(request):
    inventoryID = int(request.GET["inventoryID"])
    orderQuantity = float(request.GET["orderQuantity"])

    order.addItemWithID(inventoryID, orderQuantity)
    if order.exceededQuantity == True:
        return HttpResponse("<html><body><p>Order Quantity must be less than or equal to Inventory Quantity</p></body></html>")
    else:
        return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def removeItem(request):
    order.removeItem(inventoryItem)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def removeItemWithID(request):
    inventoryID = request.GET["inventoryID"]
    order.removeItemWithID(inventoryID)

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def changeItemQuantity(request):
    orderQuantity = float(request.GET["orderQuantity"])
    if orderQuantity > inventoryItem.inventoryQuantity:
        return HttpResponse("<html><body><p>Order Quantity must be less than or equal to Inventory Quantity</p></body></html>")
    else:
        order.changeItemQuantity(inventoryItem, orderQuantity)

        return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def changeItemQuantityWithID(request):
    inventoryID = int(request.GET["inventoryID"])
    orderQuantity = float(request.GET["orderQuantity"])
    originalQuantityPerItem = dict(order.originalQuantityPerItem)
    inventoryQuantity = originalQuantityPerItem[inventoryID]
    if orderQuantity > inventoryQuantity:
        return HttpResponse("<html><body><p>Order Quantity must be less than or equal to Inventory Quantity</p></body></html>")
    else:
        order.changeItemQuantityWithID(inventoryID, orderQuantity)
        return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": ""})

def finalizeOrder(request):
    order.finalizeOrder()
    order.deductInventory()

    return render(request, "order.html", {"orderID": order.orderID,"userID": order.userID,"creditCard": order.creditCard,"city": order.city,"state": order.state,"country": order.country,"address": order.address,"items": order.items,"pricePerItem": order.pricePerItem,"quantityPerItem": order.quantityPerItem,"costPerItem": order.costPerItem,"originalQuantityPerItem": order.originalQuantityPerItem,"originalValuePerItem": order.originalValuePerItem,"alteredQuantityPerItem": order.alteredQuantityPerItem,"alteredValuePerItem": order.alteredValuePerItem,"totalCost": order.totalCost,"date": order.date})
