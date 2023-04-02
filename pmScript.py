# PASSWORD MANAGER
# Author: Nahdaa Jawed
# Date Started: 01/04/2023 19:13
# Date Finished: -
# Description: -

# Importing important modules.
from pathlib import Path
import datetime
import random
import string

# Defining Functions

# Validate master username and password function. ----------------------------------------------------------------------
def validatePW(username, password):
    correctUsername = "NJawed1999"
    correctPassword = "Pr0gram2023!"

    while (username == correctUsername) and (password == correctPassword):
        return True

    print("Username or password incorrect.")


# Menu function, where you have access to other functions. -------------------------------------------------------------
def menuFunc():
    continueLoop = 1
    print("Would you like to:\n• Add a Password (add)\n• View Your Passwords (view)\n• Delete a Password (delete)\n• Generate a Password (generate)\n• Leave (quit)\n")

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

        elif userAnswer == "delete":
            deletePassword()
            menuFunc()

        elif userAnswer == "generate":
            genPassword()
            menuFunc()

        else:
            print("Invalid entry, please try again.")
            menuFunc()

        return

# Function to generate strong passwords. -------------------------------------------------------------------------------
def genPassword():
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    genAgain = ""

    while genAgain != "n":
        generatedPW = ''.join(random.choice(characters) for i in range(16))
        print(f"\nGenerated Password:{generatedPW}")
        genAgain = input("Generate another password? (Y/N) ").lower()

    print("Returning you to the main menu.")


# Function to add more passwords to the password file. -----------------------------------------------------------------
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
            fileExist = True
            addPassword()

        else:
            print("\nWARNING: The following inputs will be CASE SENSITIVE.")
            print("Please enter the following:")
            newSite = input("Site: ")
            newUsername = input("Username/email: ")
            newPassword = input("Password: ")
            print(f"\nYou have input:\nSite/Software: {newSite}         Username/email: {newUsername}           Password: {newPassword}")
            isCorrect = input("Is this correct? (Y/N) ").lower()


    siteStr = "Site: " +newSite
    userStr = "Username: " +newUsername
    passStr = "Password: " +newPassword

    newPW = open("boringStuff.txt", "a")
    newPW.write(siteStr.ljust(40)+userStr.ljust(40)+passStr.ljust(40)+"\n")
    print("\nPassword added. Taking you back to the menu.")
    return

# Function to view exisiting stored passwords. -------------------------------------------------------------------------
def viewPasswords():
    whichSite = ""
    viewAgain = ""
    viewMode = ""

    viewMode = input("\nWould you like to see one password (single) or all your passwords (all)?\n").lower()
    if viewMode == "single":
        while viewAgain != "n":
            print("Which site's username and password are you looking for?\nYour entry is CASE SENSITIVE.")
            whichSite = input()
            with open (r"boringStuff.txt","r") as viewPW:

                lines = viewPW.readlines()
                for line in lines:
                    if line.find(whichSite) != -1:
                        print(line)

            viewPW.close()

            viewAgain = input("\nWould you like to view another password? (Y/N)").lower()

    elif viewMode == "all":
        print("\n")
        f = open("boringStuff.txt","r")
        print(f.read())
        f.close()

    else:
        print("Invalid input. Please try again.\n")
        viewPasswords()

    print("Passwords file closed. Taking you back to the menu.\n")

# Function to delete stored passwords. ---------------------------------------------------------------------------------
def deletePassword():
    deleteAgain = ""

    while deleteAgain != "n":
        whichSite = input("Which sites password would you like to delete?\nYour input is CASE SENSITIVE.\n")
        with open("boringStuff.txt", "r") as f:
            lines = f.readlines()
            f.close()
        with open("boringStuff.txt", "w") as f:
            for line in lines:
                if whichSite not in line:
                    f.write(line)

        print(f"Your {whichSite} username and password has been deleted.")
        deleteAgain = input("Would you like to delete another password? (Y/N)\n").lower()

    f.close()
    print("Taking you back to the main menu.\n")


# Function to run the main password manager.----------------------------------------------------------------------------
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
        fileExist = True
        pwManager()

pwManager()
