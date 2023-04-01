# PASSWORD MANAGER
# Author: Nahdaa Jawed
# Date Started: 01/04/2023 19:13
# Date Finished: -
# Description: -

# Importing important modules.
from pathlib import Path
import datetime

# Defining Functions
def validatePW(username, password):
    correctUsername = "NJawed1999"
    correctPassword = "Pr0gram2023!"

    while (username == correctUsername) and (password == correctPassword):
        return True

    print("Username or password incorrect.")

def menuFunc():
    continueLoop = 1
    print("Would you like to add a password (add), view your passwords (view), or leave (quit)?")

    while continueLoop == 1:
        userAnswer = input().lower()

        if userAnswer == "add":
            addPassword()
            userAnswer = 0
            menuFunc()


        elif userAnswer == "view":
            viewPasswords()
            menuFunc()


        elif userAnswer =="quit":
            print("Thank you for using the Password Manager. Goodbye.")
            exit()

        else:
            print("Invalid entry, please try again.")
            menuFunc()

        return



def addPassword():
    # create a Path object with the path to the file
    fileExist = Path('./boringStuff.txt').is_file()
    newSite = ""
    newUsername = ""
    newPassword = ""
    isCorrect = ""

    while isCorrect != "y":
        if fileExist == False :
            print("Passwords file does not exist. Creating one now.")
            newPW = open("boringStuff.txt", "x")
            addPassword()

        else:
            print("\nWARNING: The following inputs will be CASE SENSITIVE.")
            print("Please enter the following:")
            newSite = input("Site: ")
            newUsername = input("Username/email: ")
            newPassword = input("Password: ")


        print(f"\nYou have input:\nSite/Software: {newSite}         Username/email: {newUsername}           Password: {newPassword}")
        isCorrect = input("Is this correct? (Y/N) ").lower()


    newPW = open("boringStuff.txt", "a")
    newPW.write(f"Site: {newSite}   Username: {newUsername}     Password: {newPassword}\n")
    print("\nPassword added. Taking you back to the menu.")





def viewPasswords():
    whichSite = ""
    viewAgain = ""

    while viewAgain != "n":
        print("Which site's username and password are you looking for?\nYour entry is CASE SENSITIVE.")
        whichSite = input()
        with open (r"boringStuff.txt","r") as viewPW:

            lines = viewPW.readlines()
            for line in lines:
                if line.find(whichSite) != -1:
                    print(line)



        viewPW.close()

        viewAgain = input("Would you like to view another password? (Y/N)").lower()

    print("Passwords file closed. Taking you back to the menu.\n")



def pwManager():
    loginAttempt = 0
    fileExist = Path('./LoginAttempt.txt').is_file()

    if fileExist == True:
        while loginAttempt != 3:
            print("Please enter your username:")
            masterUsername = input()
            print("Please enter you password:")
            masterPassword = input()

            if validatePW(masterUsername, masterPassword):
                print("\nWelcome back, Nahdaa.")
                menuFunc()

            else:
                loginAttempt = loginAttempt + 1
                print(f"Attempt {loginAttempt}.\n")

        todayDateTime = datetime.datetime.now()
        with open("LoginAttempt.txt", "r+") as f:
            content = f.read()
            f.seek(0,0)
            f.write("Login Attempt: "+str(todayDateTime)+"\n"+content)
            print(f"Breach attempt at {todayDateTime} has been recorded.")

    elif fileExist == False:
        print("Login attempt file does not exist. Creating now.")
        login = open("LoginAttempt.txt", "x")
        pwManager()


pwManager()