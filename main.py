#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name:        Data Structures (main.py)
# Purpose:     A book store allowing users to sign up, log in, browse items, purchase items, sell items, even working under Tundra! Allowing employees to work (do math), collect pay, and even able to move up in ranks! Everything is remembered, even after rerunning the program!
#
# Author:      Snow S.
# Created:     21-Apr-2023
# Updated:     03-May-2023
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import the classes created + logging
from library.works import Works
from library.customer import Customer
from library.employee import Employee
from library.jobs import Jobs
import logging
#to initiate for logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#to disable logging messages
logging.disable(logging.ERROR)

#to create all the lists that will be used later
choicesForPurpose = ["books", "video games", "back", "1", "2", "3"]
genreAccept = ["adventure", "fantasy", "romance", "thriller"]
numbersAccept = ["1","2","3","4"]
shoppingCart = {}

#to initialize the variables to enter the loops
userChoice = ""
# totalPay = Jobs.grabAccountM()

loginStatus = False
isEmployee = False
uniqueStaffId = False

#Welcome message
print("Welcome to the newly opened book store, Tundra!")

# keeps the user in the library until they choose to leave
while (userChoice != "leave") and (userChoice != "3"):
    logging.info("The user is currently logged in: " + str(loginStatus))
    # to reset this variable to re-enter the while loop
    userPurpose = ""
    # to check whether or not the user is logged in/signed up as a customer
    if (loginStatus == True and isEmployee == False):
        option = "(1) Browse Catalogue"
        option1 = "\n(2) View Cart"
        option2 = "\n(3) Sell Work"
        optional = "\n(4) Log Out"
        welcomeMessage = "\nWelcome " + Customer.getName(existCustomer) + "! "
    # if the user is not logged in
    elif (loginStatus == False):
        option = "(1) Browse Catalogue"
        option1 = "\n(2) Log In"
        option2 = "\n(3) Leave"
        optional = "\n(4) Apply For Job"
        welcomeMessage = ""
    # if the user is logged in as an employee
    elif (loginStatus == True and isEmployee == True):
        option = "(1) Work"
        option1 = "\n(2) Collect Pay"
        option2 = "\n(3) Promotion"
        optional = "\n(4) Log Out"
        welcomeMessage = "\nWelcome " + Employee.getName(existEmployee) + "! "

    print(welcomeMessage + "What would you like to do today?\n" + option + option1 + option2 + optional) # + "\n(5) Account Recovery"
    #records the user's choice
    userChoice = input().strip().lower()
    # to see what the user typed in, may be the cause of potential errors
    logging.info("The user typed in " + userChoice + " when asked what they would like to do.")

    #if the user chooses to browse or chose <back> in the next option
    if (userChoice == "browse" or userChoice == "browse catalogue" or userChoice == "1") and (isEmployee == False):
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
                            print("\nSign up to purchase books/games from Tundra.\n")

                else:
                    print("\nPlease choose from the options provided.\n")

            #if the user chose none of the options provided
            elif userPurpose not in choicesForPurpose:
                #repeat until they choose one of the options
                print("\nPlease enter a valid option.\n")
    
    #if the user chooses to login
    elif (loginStatus == False and (userChoice == "log in" or userChoice == "2")):
        logIn = input("Are you: \n(1) Employee\n(2) Customer\n").lower()

        #if user chose the employee option
        if logIn == "employee" or logIn == "1":
            #collecting the information
            fName = input("First name: ")
            lName = input("Last name: ")
            email = input("Email: ")
            pwd = input("Password: ")
            empId = input("EmployeeID: ")

            existEmployee = Employee(email, fName, lName, pwd, empId)
            
            #checking if employeeId is in database
            employeeExistence = existEmployee.checkExistence()
            #if employeeId is in database
            if employeeExistence == True:
                loginStatus = True
                isEmployee = True

                # finding the job and experience they have
                job = Jobs.findJob(empId)
                jobTitle = job[1]
                exp = job[2]
                amount = job[3]
                # creating the currentJob object under the Jobs class
                currentJob = Jobs(jobTitle, empId, exp, amount)
            else:
                print("Sorry, the staff ID provided is not found.")
        elif logIn == "customer" or logIn == "2":
            needSignUp = input("Do you already have an account (y/n)? ")
            #if user types in one of the provided options
            if needSignUp == "n" or needSignUp == "y":
                # registering the user
                newUserEmail = input("Email: ")
                newUsername = input("Username: ")
                newUserPassword = input("Password: ")

                if newUserEmail != "" or newUsername != "" or newUserPassword != "" or "@" not in newUserEmail:
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
                            print("\nAccount does not exist.\n")
                
                # if the user inputs invalid information
                else:
                    print("\nInvalid information.\n")

    # if the user chooses to view their cart
    elif (loginStatus == True and (userChoice == "view" or userChoice == "view cart" or userChoice == "2") and (isEmployee == False)):
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
    elif (loginStatus == True and (userChoice == "sell" or userChoice == "sell work" or userChoice == "3") and (isEmployee == False)):
        # prompts the user to type in the genre of the work
        genreOfWork = input("What genre is the work you are selling? We are only accepting the following genres: \n(1) Adventure\n(2) Fantasy\n(3) Romance\n(4) Thriller\n").strip().lower()
        typeOfWork = input("What type of work is this? \n(1) Books\n(2) Video Games\n").strip().lower()
        # checking if the user's responses are reasonable
        if ((genreOfWork in genreAccept or genreOfWork in numbersAccept) and (typeOfWork == "books" or typeOfWork == "video games" or typeOfWork == "1" or typeOfWork == "2")):
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

            if genreOfWork in numbersAccept:
                genreOfWork = genreAccept[int(genreOfWork)-1]
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

    # if the user is prepared to leave the store
    elif (loginStatus == False and (userChoice == "leave" or userChoice == "3")):
        # to exit the loop
        userChoice = "leave"

    #if the user wants to log out
    elif (loginStatus == True and (userChoice == "log out" or userChoice == "4")):
        loginStatus = False

    # if the user wants to apply to become a part of Tundra's staff
    elif (loginStatus == False and (userChoice == "apply" or userChoice == "apply for job" or userChoice == "4")):
        # pop up screen for applying to be an employee
        # records information on the applicant
        fName = input("First name: ")
        lName = input("Last name: ")
        email = input("Email: ")
        pwd = input("Password: ")

        if fName == "" or lName == "" or email == "" or pwd == "" or "@" not in email:
            print("\nInvalid information.\n")

        else:
            #place all the information gathered into the Employee class to generate an object
            existEmployee = Employee(email, fName, lName, pwd, "noSTAFFid")

            #checking for no duplicate applicants
            alreadyApplied = existEmployee.checkExistence()

            # if have not applied before
            if alreadyApplied == False:
                employeeId = existEmployee.getStaffId() # stores the generated employee id

                #changing user status
                isEmployee = True
                loginStatus = True 

                # add employee to database
                Employee.addEmployee(existEmployee)
                # assign them their job - cashier
                currentJob = Jobs("cashier", employeeId, 0, 0.00)
                currentJob.addJob()

                print("\nWelcome " + fName + "!\nRemember your employee ID!\n\nYour employee ID is: \033[1m" + employeeId + "\033[0m")
            
            else:
                print("\nYou have already applied.\n")

    elif (isEmployee == True and (userChoice == "work" or userChoice == "1")):
        # should pop up an option to work

        workInput = input("Your shift is 8 hours long. \nBegin working by pressing 'Enter'")
        pay = currentJob.beginWorking() # run the working minigame (math) and return total pay for the work session

    elif (isEmployee == True and (userChoice == "collect pay" or userChoice == "collect" or userChoice =="2")):
        # should pop up a screen showing the amount in account, and whether or not to collect it
        moneyChoice = input("You currently have $" + str(currentJob.findMoney()) + " in your account.\nWould you like to take it out now (y/n)? ")
        if moneyChoice == "y":
            # after collecting their pay; resets back to $0
            currentJob.clearZero()

    elif (isEmployee == True and (userChoice == "promotion" or userChoice == "3")):
        # calling the promote function; checks if the employee can promote or not
        jobNow = currentJob.promote()

        print("\nYour current job is: " + str(jobNow[0]) + "\nYour current pay is: $" + str(jobNow[1]) + "/hr")
        userChoice = "stay" #keeps the user in while loop

    #if the user did not choose a valid option
    else:
        print("\nPlease input a valid option.\n")

print("\nPlease come again!")