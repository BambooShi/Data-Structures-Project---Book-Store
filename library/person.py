class User():
    '''
    A class that holds the user objects

    Attibutes
    ---------
    email: string
            The email of the user

    name: string
        The first name of the user

    password: string
        The stored password of the user

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

    def __init__(self, email, name, password):
        '''
        Constructor to build this object

        Parameters
        ----------
        email: string
            The email of the user
        
        name: string
            The username of the user

        password: string
            The stored password of the user
        ''' 
        self.email = email
        self.name = name
        self.password = password
    
    def checkExistence(self, info, file):
        '''
        Checks if the user is logged in or not

        Parameters
        ----------
        info: any
            The info required to check for existence
        file: string
            The path to the text file desired

        Returns
        -------
        existence: boolean
            Returns true or false
        '''
        existence = False
        with open(file, 'r+') as readArray:
            content = readArray.readlines()
            for i in range(0, len(content)):
                # check if current info already exists or not
                if (str(info)) in content[i]:
                    existence = True
                    return existence

        return existence
    
    def getName(self) -> str:
        '''
        Returns the username of the user

        Returns
        -------
        The username of the user
        '''
        return self.name