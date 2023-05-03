from library.person import User

class Customer(User):
    '''
    A class that holds the customer objects

    Attibutes
    ---------
    email: string
        The email of the customer
        
    name: string
        The username of the customer

    password: string
        The stored password of the customer

    Methods
    -------
    addCustomer()
        Adds the customer to the database/file
    getName() -> string
        Returns the username of the customer
    checkExistence() -> boolean
        Returns true or false depending on if the customer exists in database/file
    '''

    def __init__(self, email, name, password):
        '''
        Constructor to build this object

        Parameters
        ----------
        email: string
            The email of the customer
        
        name: string
            The username of the customer

        password: string
            The stored password of the customer
        ''' 
        super().__init__(email, name, password)
    
    def addCustomer(self):
        '''
        Adds the user to the database/file if their email is not already stored
        '''
        customerInfo = [self.email, self.name, self.password]

        #adds the customer to the database/file if the email is not already in database/file
        with open('library/customerList.txt', 'r+') as readArray:
            content = readArray.readlines()
            # if the email is not already used
            if self.email not in content:
                # adds the customer information into the file/database
                readArray.write(str(customerInfo) + "\n")
        return
    
    def getName(self) -> str:
        '''
        Returns the username of the customer
        Returns
        -------
        The username of the customer
        '''
        return super().getName()
    
    def checkExistence(self) -> str:
        '''
        Checks if the user exists or not

        Returns
        -------
        existence: boolean
            Returns true or false
        '''
        customerInfo = self.email #unique to each customer
        file = 'library/customerList.txt'

        return super().checkExistence(customerInfo, file)