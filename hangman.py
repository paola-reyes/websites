accounts = {}

def madeAccount(username, password):
	print("Welcome " + username + "!")

def urIn(username, password):
	print("Welcome back, " + username + "; you're in!")
	
#This is the start menu that prints out the options to make an account or log in
def startMenu():
 
    options = ("[1] Make An Account", "[2] Log In")
    
    for i in options:
        print(i)

    choice = input("Choose a number option ")
    choice = choice.strip()

    if choice == "1":
        username = input("Choose a username ")
        password = input("Choose a password ")
        makeAccount(username, password)
        current_player = username.strip()
        madeAccount(username, password)
    elif choice == "2":
        username = input("Choose a username ")
        password = input("Choose a password ")
        logIn(username, password)

#This is a helper function for startMenu()
#This function makes a new account by taking in a new username and password
def makeAccount(username, password):
    accounts[username] = password
    
    accounts_file = open("accounts.txt", "a")
    accounts_file.write(username + "," + password + "," + "\n")
    accounts_file.close()

#This is a also a helper function for startMenu()  
#This function asks for a username and password and checks if they are in the dictionary
def logIn(uname, pword):
    accounts_file = open("accounts.txt", "r")
    accounts = list(accounts_file)
    accounts_file.close()

    is_found = False
    
    for i in accounts:
        info = i.split(",")
        username = info[0].strip()
        password = info[1].strip()
        score = info[2].strip()
        if uname == username and pword == password:
            urIn(uname, pword)
        else:
            print("\nIncorrect username/password. Try again!\n")
            startMenu()

startMenu()
