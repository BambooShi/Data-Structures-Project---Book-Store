import random
import ast

class Employee():
    '''
    A class that holds the employee objects

    Attibutes
    ---------
    name: string
        The first name of the employee

    lName: string
        The last name of the employee

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

    def __init__(self, name, lName):
        '''
        Constructor to build this object

        Parameters
        ----------    
        name: string
            The first name of the employee
        
        lName: string
            The last name of the employee
        
        staffId: string
            The staff identification

        ''' 
        self.name = name
        self.lName = lName
        self.staffId = Employee.generateStaffId(self)

    def addEmployee(self):
        '''
        Adds the user to the database/file if their email is not already stored
        '''
        EmployeeInfo = [self.name, self.lName, self.staffId]

        #adds the employee to the database/file if the email is not already in database/file
        with open('library/employeeList.txt', 'r+') as readArray:
            content = readArray.readlines()
            if EmployeeInfo not in content:
                # adds the customer information into the file/database
                readArray.write(str(EmployeeInfo) + "\n")
        return
    
    def getName(self) -> str:
        '''
        Returns the first name of the employee
        Returns
        -------
        The first name of the employee
        '''
        return self.name
    
    def checkExistence(self) -> str:
        '''
        Checks if the user exists or not

        Returns
        -------
        existence: boolean
            Returns true or false
        '''
        employeeInfo = [self.name, self.lName]
        file = 'library/employeeList.txt'

        existence = False
        with open(file, 'r+') as readArray:
            content = readArray.readlines()
            for i in range(0, len(content)):
                # check if current info already exists or not
                if (str(employeeInfo)) in content[i]:
                    existence = True
                    return existence

        return existence

    def generateStaffId(self) -> str:
        '''
        Randomly generates an unique string to new employees


        '''
        jumboNum = random.randrange(100000,999999) #generates a random 6 digit number

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
    
    def findEmployee(staffId):
        '''
        To find information such as the first name and last name of the employee based on the staffId provided

        Parameters
        ----------
        staffId: string
            The identification of the employee
            
        Return
        ------
        information: list[]
            A list containing the first name, last name, and staff id
        '''
        # opens the text file and returns the information as an array
        with open('library/employeeList.txt', 'r+') as readArray:
            content = readArray.readlines()
            for i in range(0, len(content)):
                # check if staff id is in the current line being checked
                if (staffId) in content[i]:
                    information = content[i]
                    information = ast.literal_eval(information)

        return information