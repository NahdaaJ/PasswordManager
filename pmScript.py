# PASSWORD MANAGER
# Author: Nahdaa Jawed
# Date Started: 01/04/2023 19:13
# Date Finished: 02/04/2023 13:17
# Description:  A password manager function with several features.
#               Initially, the user is prompted to enter a master user and password that the user can set beforehand.
#               The user has 3 attempts to enter the master information correctly, else the program records
#               it as a breach attempt at the exact time and date and stops the program.
#               Once the user enters the information successfully, they are routed to the main menu.
#               In the menu they have access to the various features. They can add, view, delete or generate a password.
#               They can also quit the program from the main menu.

# Importing important modules.
from pathlib import Path
import datetime
import random
import string
import os

# Defining Functions

# Validate master username and password function. ----------------------------------------------------------------------
def validatePW(username, password):
    correctUsername = "YourUsername"
    correctPassword = "YourPassword"

    while (username == correctUsername) and (password == correctPassword):
        return True

    print("Username or password incorrect.")


# Menu function, where you have access to other functions. -------------------------------------------------------------
def menuFunc():
    continueLoop = 1

    # Asking the user what they would like to do.
    print("\nWould you like to:\n• Add a Password (add)\n• View Your Passwords (view)\n• Delete a Password (delete)\n• Generate a Password (generate)\n• Leave (quit)\n")

    # Loops through the menu until the program is told to exit.
    while continueLoop == 1:
        userAnswer = input().lower()

        # Actions based on the user choice. Different choices call different functions, then return to menu once finished.
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
    # Generating a random password of length 16 with letters, digits, and symbols.
    characters = string.ascii_letters + string.digits + string.punctuation
    genAgain = ""

    # While the user wants to generate a new password, the program loops.
    while genAgain != "n":
        generatedPW = ''.join(random.choice(characters) for i in range(16))
        print(f"\nGenerated Password:{generatedPW}")
        genAgain = input("Generate another password? (Y/N) ").lower()

    # If the user doesnt want to generate a new password, the loop breaks and exits to the menu.
    print("Returning you to the main menu.")


# Function to add more passwords to the password file. -----------------------------------------------------------------
def addPassword():
    # create a Path object with the path to the file
    fileExist = Path('./boringStuff.txt').is_file()
    newSite = ""
    newUsername = ""
    newPassword = ""
    isCorrect = "n"

    # Loops until the new password is confirmed to be correct by the user.
    while isCorrect != "y":
        while isCorrect == "n":
            #If the file does not exist, the program creates it.
            if fileExist == False :
                print("Passwords file does not exist. Creating one now.")
                newPW = open("boringStuff.txt", "x")
                fileExist = True
                addPassword()

            else:
                # Asking the user to input new information.
                print("\nWARNING: The following inputs will be CASE SENSITIVE.")
                print("Please enter the following:")
                newSite = input("Site: ")
                newUsername = input("Username/email: ")
                newPassword = input("Password: ")

                # Asking for user confirmation.
                print(f"\nYou have input:\nSite/Software: {newSite}         Username/email: {newUsername}           Password: {newPassword}")
                isCorrect = input("Is this correct? (Y/N), or would you like to cancel (C)?").lower()

        # If the user chooses to quit, the program exits to the menu.
        if isCorrect == "c":
            menuFunc()

    # Formatting the new entries.
    siteStr = "Site: " +newSite
    userStr = "Username: " +newUsername
    passStr = "Password: " +newPassword

    # Adding the new entries to the text file.
    newPW = open("boringStuff.txt", "a")
    newPW.write(siteStr.ljust(40)+userStr.ljust(40)+passStr.ljust(40)+"\n")

    # Returning to the menu.
    print("\nPassword added. Taking you back to the menu.")
    return


# Function to view existing stored passwords. -------------------------------------------------------------------------
def viewPasswords():
    whichSite = ""
    viewAgain = ""
    viewMode = ""
    fileExist = Path('./boringStuff.txt').is_file()

    # If the password file doesn't exist, the program creates it, then loops back to the beginning.
    if fileExist == False:
        print("Passwords file does not exist. Creating one now.")
        newPW = open("boringStuff.txt", "x")
        fileExist = True
        viewPasswords()

    # Allows the user to choose whether to see one password or all of them.
    else:
        viewMode = input("\nWould you like to see one password (single) or all your passwords (all)?\n").lower()
        checkFile = os.stat("boringStuff.txt").st_size # Checking the size of the .txt file.
        addNew = ""

        # If the file size = 0, it means it is empty and has nothing to display.
        if checkFile == 0:
            addNew = input("You currently have no passwords saved. \nWould you like to add a new password? (Y/N)\n").lower()
            if addNew == "y":
                addPassword()

            else:
                print("Taking you back to main menu.\n")
                menuFunc()

        # Displaying the passwords using the different modes.
        else:
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

                    viewAgain = input("Would you like to view another password? (Y/N)").lower()

            elif viewMode == "all":
                f = open("boringStuff.txt","r")
                print("Your Passwords:")
                print(f.read())
                f.close()

            else:
                print("Invalid input. Please try again.\n")
                viewPasswords()

            print("Passwords file closed. Taking you back to the menu.")

# Function to delete stored passwords. ---------------------------------------------------------------------------------
def deletePassword():
    deleteAgain = ""
    passExist = ""

    # If the user DOES want to delete another password, and if the password they entered isn't correct, the function loops.
    while deleteAgain != "n":
        isCorrect = "n"
        while isCorrect != "y":
            while isCorrect == "n":
                # Opening, reading and looking for the specified site in the .txt file.
                whichSite = input("Which sites password would you like to delete?\nYour input is CASE SENSITIVE.\n")
                f = open(r"boringStuff.txt", "r")
                lines = f.readlines()
                for line in lines:
                    lineExist = line.find(whichSite)

                # If the specified site doesn't exist, the program tells the user.
                if lineExist == -1:
                    print("User and password for this site not recorded.\n")



                with open(r"boringStuff.txt", "r") as viewPW:
                    lines = viewPW.readlines()
                    for line in lines:
                        if line.find(whichSite) != -1:
                            # Asking for user confirmation.
                            print(f"You have asked to delete the following:\n{line}")
                            isCorrect = input("Is this correct? (Y/N), or would you like to cancel (C)?").lower()

            # If the user decides to cancel, they are returned to the menu.
            if isCorrect =="c":
                menuFunc()

        # Deleting the requested password.
        with open("boringStuff.txt", "r") as f:
            lines = f.readlines()
            f.close()
        with open("boringStuff.txt", "w") as f:
            for line in lines:
                if whichSite not in line:
                    f.write(line)

        # Confirmation with the user, and asking if they would like to delete another.
        print(f"Your {whichSite} username and password has been deleted.")
        deleteAgain = input("Would you like to delete another password? (Y/N)\n").lower()

    f.close()
    print("Taking you back to the main menu.\n")


# Function to run the main password manager.----------------------------------------------------------------------------
def pwManager():
    loginAttempt = 0
    fileExist = Path('./LoginAttempt.txt').is_file()

    # If the login attempt file exists, the program runs as follows.
    if fileExist == True:
        # While 3 login attempts HAVEN't been exceeded, the user is prompted 3 times.
        while loginAttempt != 3:
            print("Please enter your master username:")
            masterUsername = input()
            print("Please enter you master password:")
            masterPassword = input()

            # If the master information is entered correctly, they are routed to the menu.
            if validatePW(masterUsername, masterPassword):
                print("\nWelcome back, [YourName].")
                menuFunc()

            # If they exceed 3 attempts, the program records the attempted "breach"
            else:
                loginAttempt = loginAttempt + 1
                print(f"Attempt {loginAttempt}.\n")

        # Recording the exact date and time of the attempt, and printing it to a file.
        todayDateTime = datetime.datetime.now()
        with open("LoginAttempt.txt", "r+") as f:
            content = f.read()
            f.seek(0,0) # Most recent attempts are recorded ABOVE older attempts.
            f.write("Login Attempt: "+str(todayDateTime)+"\n"+content)
            print(f"Breach attempt at {todayDateTime} has been recorded.")

    # If the login attempt file DOES NOT exist, the program creates it and the function is looped to the beginning.
    elif fileExist == False:
        print("Login attempt file does not exist. Creating now.")
        login = open("LoginAttempt.txt", "x")
        fileExist = True
        pwManager()

# Running the main Password Manager Function
pwManager()