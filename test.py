userpassword = "Bruh"     #User database
userusername = "BruhUser"

login_or_create = input("hello there welcome to dubgkhx would you like to A) log in or B) Create account ") #Login or create account options {Logged Out State}

if login_or_create == "A": #Person chose option A
    askusername = input("Welcome back please enter your username ") #Asks for username

    if askusername == userusername: #If the person enters a Username from the database
        askpassword = input("Welcome please enter your password ")

        if askpassword == userpassword: #Ask {User} for password for any account from the database
            print("Welcome", userusername, "You've successfully logged in") #Logged on state

        else: #Error 404 for not entering any proper data from the data base
            print("Error 404: Dead End, Could not find this username or password on the database please try again or to create an account please restart the program")

    else: #Error 404 for not entering any proper data from the data base
            print("Error 404: Dead End, Could not find this username or password on the database please try again or to create an account please restart the program")

elif login_or_create == "B": #If the person wants to create an account
    newuserusername = input("So you would like to create an account nice let's start with an epic username ") #Adds new username to the database
    newuserpassword = input("Please create a passowrd for your account ") #Adds password to the database
    confirmnewuserpassword = input("PLease type your password in again ")
    if confirmnewuserpassword == newuserpassword:
        asknewuserusername = input("Now please log into your account fisrt enter your username ")
        if asknewuserusername == newuserusername:
            asknewuserpassword = input("Now please type your password ")
            if asknewuserpassword == newuserpassword:
                print("You are now finished with your account welcome", newuserusername, "please also keep your password", newuserpassword, "safe") #Welcomes user {Logged in State}

            else:
                print("Error 404: Dead End, Could not find this username or password on the database please try again or to create an account please restart the program")
        else:
             print("Error 404: Dead End, Could not find this username or password on the database please try again or to create an account please restart the program")
    else:
        print("Error 402: Incorrect Password Typed")
else: #Error 403
    print("Error 403: Dead End, No proper options have been selected")
            


