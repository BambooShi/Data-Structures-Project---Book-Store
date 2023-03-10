class Customer():
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
        self.email = email
        self.name = name
        self.password = password
    
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
        return self.name
    
    def checkExistence(self) -> str:
        '''
        Checks if the user is logged in or not

        Returns
        -------
        existence: boolean
            Returns true or false
        '''
        existence = False
        with open('library/customerList.txt', 'r+') as readArray:
            content = readArray.readlines()
            customerInfo = [self.email, self.name, self.password]
            for i in range(0, len(content)):
                # check if customer info matches the current line exactly
                if (str(customerInfo)+ "\n") == content[i]:
                    existence = True
                    return existence

        return existence

