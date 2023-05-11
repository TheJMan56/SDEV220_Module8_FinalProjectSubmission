import sqlite3

conn = sqlite3.connect('Inventory_and_Users_and_Orders_Updated.db', check_same_thread=False)
curs = conn.cursor()

def loginUser():
    email = input("Enter email: ")
    loginPassword = input("Enter password: ")
    getUser = 'SELECT * FROM Users WHERE email ='
    email = str(email)
    email = "\"" + email + "\""
    curs.execute(getUser + " " + email)
    userData = curs.fetchone()
    if userData == None:
        return "Incorrect email"
    else:
        correctPassword = userData[3]
        
        if loginPassword == correctPassword:
            userID = userData[0]
            userName = userData[1]
            email = userData[2]
            loginPassword = userData[3]
            creditCard = userData[4]
            city = userData[5]
            state = userData[6]
            country = userData[7]
            address = userData[8]
            phone = userData[9]
            
            return userData
        else:
            return "Incorrect password"

print(loginUser())
