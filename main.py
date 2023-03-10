#-----------------------------------------------------------------------------
# Name:        Data Structures (main.py)
# Purpose:     To make a functioning book store that just opened.
#
# Author:      Snow S.
# Created:     02-Mar-2023
# Updated:     10-Mar-2023
#-----------------------------------------------------------------------------
# Import the class(es) created + logging
from library.works import Works
from library.customer import Customer
import logging
#to initiate for logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#to disable logging messages
# logging.disable(logging.ERROR)

#to create all the lists that will be used later
choicesForPurpose = ["books", "video games", "back", "1", "2", "3"]
genreAccept = ["adventure", "fantasy", "romance", "thriller"]
numbersAccept = ["1","2","3","4"]
shoppingCart = {}

#to initialize the variables to enter the loops
userChoice = ""

loginStatus = False

#Welcome message
print("Welcome to the newly opened book store, Tundra!")

# keeps the user in the library until they choose to leave
while (userChoice != "leave") and (userChoice != "3"):
    logging.info("The user is currently logged in: " + str(loginStatus))
    # to reset this variable to re-enter the while loop
    userPurpose = ""
    # to check whether or not the user is logged in/signed up
    if (loginStatus == True):
        option = " View Cart"
        option2 = "\n(3) Sell Work"
        optional = "\n(4) Log Out"
        welcomeMessage = "\nWelcome " + Customer.getName(existCustomer) + "! "
    else:
        option = " Log In"
        option2 = "\n(3) Leave"
        optional = ""
        welcomeMessage = ""

    print(welcomeMessage + "What would you like to do today?\n(1) Browse Catalogue\n(2)" + option + option2 + optional)
    #records the user's choice
    userChoice = input().strip().lower()
    # to see what the user typed in, may be the cause of potential errors
    logging.info("The user typed in " + userChoice + " when asked what they would like to do.")

    #if the user chooses to browse or chose <back> in the next option
    if (userChoice == "browse" or userChoice == "browse catalogue" or userChoice == "1"):
        # ensures that the user must enter appropriate responses to progress
        while (userPurpose not in choicesForPurpose):
            print("What would you like to browse for?\n(1) Books\n(2) Video Games \n(3) Back")
            # records the user's answer
            userPurpose = input().strip().lower()
            # to see what the user typed in, may be the cause of potential errors
            logging.info("The user typed in " + userPurpose + " when choosing what they wanted to browse for.")
            #if the user types in a valid option
            if (userPurpose == "books" or userPurpose == "1" or userPurpose == "video games" or userPurpose == "2"):
                if userPurpose == "2" or userPurpose == "video games":
                    userPurpose = "videoGames"
                    pub = "\nPublisher: "
                else:
                    userPurpose = "books"
                    pub = "\nAuthor: "
                #asks for the type of genre they would like to explore
                print("What genre would you like to explore? \n(1) Adventure\n(2) Fantasy\n(3) Romance\n(4) Thriller")
                userCategory = input().strip().lower()
                # if the user typed in a number
                if userCategory in numbersAccept:
                    #converts the type from string to integer
                    userCategory = int(userCategory)
                    #converts the number into the corresponding option - string
                    userCategory = genreAccept[userCategory-1]
                if (userCategory in genreAccept):
                    #display the titles of the works and the price of the works
                    listOfWorks = Works.convertWorks(userCategory, userPurpose)
                    print("\nThe titles under this genre are:\n")
                    for individualWork in listOfWorks:
                        # printing the individual names of the titles
                        print(individualWork)
                    print("<back>\n")
                    userOption = input().strip()
                    # checks if the user input is valid or not
                    logging.info(listOfWorks)
                    if userOption in listOfWorks:
                        # prints the additional information about this book
                        print("Title: " + str(userOption) + str(pub) + str(listOfWorks[userOption][0]) + "\nSynopsis: " + str(listOfWorks[userOption][1]) + "\nPrice: $" + str(listOfWorks[userOption][2]))
                        userInput = input("(Press 'Enter' to continue)")
                        #prompts the user to buy it or go back only if they are logged in
                        if  loginStatus == True and userInput == "":
                            purchase = input("Would you like to purchase it (y/n)? ")
                            if purchase == "y":
                                #Adds the title of the work along with its price into the user's shopping cart
                                shoppingCart[userOption] = listOfWorks[userOption][2]
                                print("Added to your shopping cart successfully.")
                            else:
                                print(str(userOption) + " was not added to cart.")
                    
                        else:
                            print("\nSign up to purchase the books/games.\n")

                else:
                    print("\nPlease choose from the options provided.\n")

            #if the user chose none of the options provided
            elif userPurpose not in choicesForPurpose:
                #repeat until they choose one of the options
                print("Please enter a valid option.")
    
    #if the user chooses to login
    elif (loginStatus == False and (userChoice == "log in" or userChoice == "2")):
        needSignUp = input("Do you already have an account (y/n)? ")
        if needSignUp == "n" or needSignUp == "y":
            # registering the user
            newUserEmail = input("Email: ")
            newUsername = input("Username: ")
            newUserPassword = input("Password: ")
            # generates the customer data
            existCustomer = Customer(newUserEmail, newUsername, newUserPassword)
            if needSignUp == "n":
                # stores the customer data
                Customer.addCustomer(existCustomer)
                loginStatus = True
            else:
                existence = Customer.checkExistence(existCustomer)
                if existence == True:
                    # change their login status to true
                    loginStatus = True
                else:
                    print("Account does not exist.")

    # if the user chooses to view their cart
    elif (loginStatus == True and (userChoice == "view" or userChoice == "view cart" or userChoice == "2")):
        # prints the 'receipt' including the name of the books/video games and the price, also the total cost of everything combined
        print("\nYour Shopping Cart:\n")
        # to reset the total price each time
        totalPrice = 0.00
        # to loop through the shopping cart
        for item in shoppingCart:
            #prints the name of the work and its corresponding price
            print(str(item) + " - $" + str(shoppingCart[item]))
            # adds up the total from the shopping cart
            totalPrice = round(totalPrice + float(shoppingCart[item]), 2)
        print("-----------------------------------\nTax: " + str(round(totalPrice*0.13, 2)) + "\nTotal: "+ str(totalPrice) +"\nYour total after tax is: $" + str(round(totalPrice*1.13,2)) + " after tax")
        confirmation = input("Are you ready to check out (y/n)?" )
        if confirmation == "y":
            # can now exit the loop
            print("Thank you for your purchase.")
            loginStatus = False
            userChoice = "leave"

    # if the user chooses to sell their work
    elif (loginStatus == True and (userChoice == "sell" or userChoice == "sell work" or userChoice == "3")):
        # prompts the user to type in the genre of the work
        genreOfWork = input("What genre is the work you are selling? We are only accepting the following genres: \n- Adventure\n- Fantasy\n- Romance\n- Thriller\n").strip().lower()
        typeOfWork = input("What type of work is this? \n(1) Books\n(2) Video Games\n").strip().lower()
        # checking if the user's responses are reasonable
        if (genreOfWork in genreAccept and (typeOfWork == "books" or typeOfWork == "video games" or typeOfWork == "1" or typeOfWork == "2")):
            titleOfWork = input("Title: ")
            authorOfWork = input("Author: ")
            synopsisOfWork = input("Quick Summary: ")
            # initial value to enter the while loop
            priceOfWork = 200.00
            # checking what the user typed in
            if (typeOfWork == "video games" or typeOfWork == "2"):
                workType = "videoGames"
            else:
                workType = "books"
            # "traps" the user until they enter an appropriate price
            while (priceOfWork > 100.00 or priceOfWork < 0.00):
                try:
                    priceOfWork = float(input("Ideal price for selling (within $100.00): "))
                except:
                    print("Invalid input, please input a number")
                    priceOfWork = 200.00
                else:
                    # to convert from string to float
                    priceOfWork = float(priceOfWork)
                    #Ensures the user inputs an appropriate price before adding to database/file
                    if (priceOfWork < 100.00 and priceOfWork > 0.00):
                        # the new price, as Tundra is a book store; this is the fee for selling their works
                        priceOfWork += 2.50
                        # generating an object through the use of the class
                        work1 = Works(genreOfWork, titleOfWork, authorOfWork, priceOfWork, synopsisOfWork, workType)
                        work1.addWork()
                        #returns to original price - in case the adjusted price goes beyond 100.00
                        priceOfWork -= 2.50
                        # to ensure the user stays in the bigger loop, does not exit the first loop
                        userChoice = ""
                    else:
                        print("Please enter an appropriate price, within $100.00.")
                        # to run the while loop again
                        priceOfWork = 200.00

        # if the user did not follow the instructions - kick them out
        else:
            print("Sorry, unfortunately, Tundra is unable to accept your product.")

    elif  (loginStatus == True and (userChoice == "log out" or userChoice == "4")) or (loginStatus == False and (userChoice == "leave" or userChoice == "3")):
        # to exit the loop
        loginStatus = False
        userChoice = "leave"

    #if the user did not choose a valid option
    else:
        print("Please input a valid option.")

print("\nPlease come again!")