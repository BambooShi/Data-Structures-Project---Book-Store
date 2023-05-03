from library.employee import Employee
# from employee import Employee
import ast
import random

class Jobs(Employee):
    '''
    A class that holds the different job objects

    Attibutes
    ---------
    workTitle: string
        The job title

    staffId: string
        The staff identification

    experience: int
        Number of times they have worked as their job title
    
    money: float
        Amount of money in account

    Methods
    -------
    promote() -> list
        Returns the new job as a list
    beginWorking()
        A working minigame, will increase and update the experience and pay employee receives each session appropriately
    findJob() -> list
        Returns the current job title as well as the employeeId, job experience, and pay waiting to be collected
    findPay() -> list
        Returns the current job title and the hourly pay of the job
    addJob()
        Adds the employee job information into database
    modifyExpAndMoney()
        Modifies and updates the new information into database
    clearZero()
        Resets the amount awaiting to be collected in employee account
    findMoney() -> float
        Returns the amount of money in account
    '''

    def __init__(self, workTitle, staffId, experience, money):
        '''
        Constructor to build this object

        Parameters
        ----------     
        workTitle: string
            The job title

        staffId: string
            The staff identification

        experience: int
            Number of times they have worked as their job title

        money: float
            Amount of money in account
            
        ''' 
        self.workTitle = workTitle
        self.staffId = staffId
        self.experience = experience
        self.money = money
    
    def promote(self) -> list:
        '''
        To change the job title for a different pay and working hours

        Return
        ------
        newJob: list[]
            contains the name of the job and the pay of the job
        '''
        #default - cashier
        jobNum = 0
        
        # stores the different types of jobs offered; "title of position": pay
        jobTypes = {"cashier": 14.50, "sales associate": 15.50, "customer service representative": 18.50, "assistant manager": 20.50, "manager": 30.25}
        # converts the dictionary into a list for easier organization
        newJobTitle = list(jobTypes.keys())
        # if the employee is already a manager (best job so far)
        if self.workTitle == "manager":
            print("This is already the best job in Tundra.")
            jobNum = 4

        # if the employee has enough experience
        elif self.experience > 10:
            for i in range(0,len(newJobTitle)):
                if self.workTitle == newJobTitle[i]:
                    jobNum = i + 1
                    self.experience = 0 #resets experience to 0, since will begin working on new job

        else:
            print("Sorry, you don't have enough experience. Please gain more experience then try asking for a promotion.")
            for i in range(0,len(newJobTitle)):
                if self.workTitle == newJobTitle[i]:
                    jobNum = i
        
        job = list(jobTypes.items())
        newJob = job[jobNum]

        self.workTitle = newJob[0] #updating the worktitle of employee if promoted, or else stays the same

        Jobs.modifyExpAndMoney(self) #updating the current status of employee

        return newJob
    
    def beginWorking(self) -> int:
        '''
        To keep track of the number of times worked and if a bonus should be given

        '''
        correctness = 0
        bonus = 0
        info = Jobs.findJob(self.staffId)
        job = info[1]
        exp = info[2]
    
        for time in range(0, 5):
            # if they are still relatively new to this job
            if exp < 8:
                num1 = random.randrange(1,10)
                num2 = random.randrange(10,99)
            # if they are experienced
            else:
                num1 = random.randrange(1,100)
                num2 = random.randrange(100,999)

            # if the employee's job is cashier
            if job == "cashier":
                answer = num1 * num2
                userAnswer = input("The customer wants to purchase " + str(num1) + " items that cost $" + str(num2) + " each. How much should you charge them for? ")

            elif job == "sales associate":
                userAnswer = input("The customer took books for a total of $" + str(num1) + " and took a total of $" + str(num2) + " worth of video games. How much did the customer spend in total? ")
                answer = num1 + num2

            elif job == "customer service representative":
                userAnswer = input("The customer wants to remove items from his shopping cart. They originally has $" + str(num2) + " worth of items in their cart, they now wants to remove $" + str(num1) + " from their cart. \nWhat is the value of the items still remaining in the cart? ")
                answer = num2 - num1

            elif job == "assistant manager":
                userAnswer = input("There are " + str(num1) + " employees working in Tundra, and our current budget is $" + str(num2) + ". \nIf each person is paid $14.00, how many people can be paid? ")
                totalPay = num1*14 # the total amount that Tundra owes to their employees
                if num2 >= totalPay: # if Tundra has enough budget to cover the salary expense
                    answer = num1
                else: # if Tundra does not have enough budget to cover the salary expense
                    answer = int(num2/14)
            
            else: #if job is manager
                userAnswer = input("There are now 45 employees working here at Tundra. However, Tundra is still incapable of keeping up with the salary expense with a weekly budget of $" + str(num1*num2) + " and Tundra must pay everyone at least $14.00 per hour for a total of 48 hours a week. " + "\nHow many people should you fire to ensure everyone still working here will get their minimum pay? ")
                personSalary = 14*48 # minimum salary for a week per person
                answer = int(45 - (num2*num1)/personSalary)
            
            if userAnswer == str(answer):
                correctness += 1

            print("\n" + str(correctness) + " out of " + str(time + 1) +"\n")

                    
            if correctness > 2:
                bonus += 10.00
        
        if bonus != 0:
            print("You have gotten a bonus of $" + str(bonus))

        onePay = self.findPay()
        pay = onePay[1]*8 + bonus
        
        self.money += pay #add the amount earned into account
        self.experience += 1 #add one to experience

        Jobs.modifyExpAndMoney(self)

        return

    def findJob(staffId):
        '''
        To find information such as the title of their job, number of experience, and amount of money in account, based on the staffId provided

        Return
        ------
        information: list[]
            A list containing the staffId, job title, number of experience, and pay remaining to be collected
        '''
        # opens the text file and returns the information as an array
        with open('library/workExperience.txt', 'r+') as readArray:
            content = readArray.readlines()
            for i in range(0, len(content)):
                # check if customer info matches the current line exactly
                if (staffId) in content[i]:
                    information = content[i]
                    information = ast.literal_eval(information)

        return information
    
    def findPay(self):
        '''
        To find the job pay along with the job title

        Return
        ------
        newJob: list[]
            A list containing the job title and the pay per hour
        '''
        #default - cashier
        jobNum = 0
        
        # stores the different types of jobs offered; "title of position": pay
        jobTypes = {"cashier": 14.50, "sales associate": 15.50, "customer service representative": 18.50, "assistant manager": 20.50, "manager": 30.25}
        # converts the dictionary into a list for easier organization
        newJobTitle = list(jobTypes.keys())

        # trying to find the index number
        for i in range(0,len(newJobTitle)):
            if self.workTitle == newJobTitle[i]:
                jobNum = i
        
        job = list(jobTypes.items())
        newJob = job[jobNum]

        return newJob
    
    def addJob(self):
        '''
        To add the employee job information into database (text file)
        '''
        with open('library/workExperience.txt', 'a') as addOn:
            addOn.write("['{}', '{}', {}, {}]\n".format(self.staffId, self.workTitle, self.experience, self.money)) #adds this information into the text file

        return

    def modifyExpAndMoney(self):
        '''
        To modify and update the data stored in text file
        '''
        # modify the data stored in text file
        with open('library/workExperience.txt', 'r') as readArray:
            content = readArray.readlines() # stores the current data into variable

        with open('library/workExperience.txt','w') as readArray:
            for i in content: #store each line in content as variable i
                if str(self.staffId) in i: # finding the line containing the staffId
                    readArray.write("['{}', '{}', {}, {}]\n".format(self.staffId, self.workTitle, self.experience, self.money)) # updates the experience information in text file
                else:
                    readArray.write(i) # rewrite the same thing

    def clearZero(self):
        '''
        To reset the amount in account to 0.00
        '''
        self.money = 0.00
        Jobs.modifyExpAndMoney(self)
        return
    
    def findMoney(self):
        '''
        To grab amount of money left in account

        Return
        ------
        The amount of money left in account
        '''
        return self.money
