import random
from library.customer import Customer
# from customer import Customer

class Employee(Customer):
    '''
    A class that holds the employee objects

    Attibutes
    ---------
    email: string
            The email of the customer

    name: string
        The first name of the employee

    lName: string
        The last name of the employee

    password: string
        The stored password of the employee

    staffId: string
        The staff identification

    Methods
    -------
    addEmployee()
        Adds the employee to the database/file
    getName() -> string
        Returns the name of the employee
    checkExistence() -> boolean
        Returns true or false depending on if the employee exists in database/file
    generateStaffId() -> string
        Returns the employeeId as a string
    getStaffId() -> string
        Returns the id of employee
    '''

    def __init__(self, email, name, lName, password, staffId):
        '''
        Constructor to build this object

        Parameters
        ----------     
        email: string
            The email of the employee

        name: string
            The first name of the employee
        
        lName: string
            The last name of the employee

        password: string
            The stored password of the employee
        
        staffId: string
            The staff identification

        ''' 
        super().__init__(email, name, password)
        self.lName = lName
        if staffId == "noSTAFFid":
            self.staffId = Employee.generateStaffId(self)
        else:
            self.staffId = staffId

    def addEmployee(self):
        '''
        Adds the user to the database/file if their email is not already stored
        '''
        EmployeeInfo = [self.email, self.name, self.lName, self.password, self.staffId]
        EmployeeBackup = [self.email, self.name, self.lName]

        #adds the employee to the database/file if the email is not already in database/file
        with open('library/employeeList.txt', 'r+') as readArray:
            content = readArray.readlines()
            # if the email is not already used
            if self.email not in content:
                # adds the customer information into the file/database
                readArray.write(str(EmployeeInfo) + "\n")
                #to check for its existence later
                readArray.write(str(EmployeeBackup) + "\n")
        return
    
    def getName(self) -> str:
        '''
        Returns the first name of the employee
        Returns
        -------
        The first name of the employee
        '''
        return super().getName()
    
    def checkExistence(self) -> str:
        '''
        Checks if the user is logged in or not

        Returns
        -------
        existence: boolean
            Returns true or false
        '''
        existence = False
        with open('library/employeeList.txt', 'r+') as readArray:
            content = readArray.readlines()
            employeeInfo = [self.email, self.name, self.lName]
            for i in range(0, len(content)):
                # check if employee info is in database
                if (str(employeeInfo)) in content[i]:
                    existence = True
                    return existence

        return existence
    
    def generateStaffId(self) -> str:
        '''
        Randomly generates an unique string to new employees


        '''
        jumboNum = random.randrange(1000,9999) #generates a random 4 digit number

        # retrieving the first letter of both first and last name
        FFname = self.name[0]
        LFname = self.lName[0]
        
        #opens the file storing all the employee id
        with open('library/employeeList.txt', 'r+') as readArray:
            listOfId = readArray.readlines()
            staffId = str(jumboNum) + FFname + LFname #combines to create the staff id
            # if the staffId is already stored in the file
            if (str(staffId) in listOfId):
                # run this function again
                Employee.generateStaffId(self)
            else:
                # return staffId
                return staffId

        
    
    def getStaffId(self):
        '''
        Returns the id of the employee
        Returns
        -------
        The id of the employee
        '''
        return self.staffId