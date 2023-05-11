def loginUser(request):
    email = request.GET["email"]
    loginPassword = request.GET["loginPassword"]
    getUser = 'SELECT * FROM Users WHERE email ='
    userID = str(userID)
    try:
        curs.execute(getUser + " " + userID)
        userData = curs.fetchone()

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
        
            global user
            user = User()
            user.newUser(userID, userName, email, loginPassword, creditCard, address, city, state, country, phone)
            return render(request, "user.html", {"userID": user.userID,"userName": user.userName,"email": user.email,"loginPassword": user.loginPassword,"creditCard": user.creditCard,"city": user.city,"state": user.state,"country": user.country,"address": user.address,"phone": user.phone})
        else:
            return HttpResponse("<html><body><p>Incorrect Password</p></body></html>")
    except:
        return HttpRespoonse("<html><body><p>Incorrect Email</p></body></html>")
