#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name:        Algorithms
# Purpose:     To help the user find an employee using insertion sort, linear search, and binary search. 
#              Will tell the user the position the employee is ordered at after being organized and sorted.
#
# Author:      Snow S.
# Created:     11-May-2023
# Updated:     18-June-2023
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import the class created + logging, ast, time, names
import ast
from employee import Employee
import logging
import names
import time

#to initiate for logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#to disable logging messages
logging.disable(logging.ERROR)

def findNumAndInitials(emp):
    '''
    To only pull out the number portion from the staff id for easier sorting

    Parameters
    ----------
    emp: string
        employeeId waiting to be deciphered

    Return
    ------
    num: int
        The number portion of the employeeId
    initials: string
        The initial portion of the employeeId
    '''
    num = ''
    initials = ""
    numbers = '0123456789'
    for i in emp:
        if i in numbers:
            num += i
        else:
            initials += i
    num = int(num) #converting types
    return num, initials

def insertionSort(arr, secArr):
   '''
    Sorts the first array and orders the second array based on the first array.

    Parameters
    ----------
    arr: list[]
        A list of items; the one to be sorted
    secArr: list[]
        A list of items; the one ordered based on 'arr'
    
   '''
   for i in range(1, len(arr)):
      key = arr[i]
      key2 = secArr[i]
      # Move elements of arr[0..i-1], that are greater than key,
      # to one position ahead of their current position
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         secArr[j+1] = secArr[j]
         j -= 1
      arr[j+1] = key
      secArr[j+1] = key2

def linearSearch(arr, item):
    '''
    To search for an item in a large list, one-by-one

    Parameters
    ----------
    arr: list[]
        A large sorted array of items
    item: any
        The item to search for

    Return
    ------
    i: int
        indicator of where the item is in the list
    '''
    for i in range(0, len(arr)):
        if item == arr[i]:
            return i
    
    return -10 #not in list

def binarySearch(arr, item):
    '''
    To search for an item in a large sorted list, using the binary method

    Parameters
    ----------
    arr: list[]
        A large sorted list containing several items
    item: any
        The item to search for
    
    Return
    ------
    i: int
        indicator of where the item is in the list
    '''
    min = 0
    max = len(arr)

    while max >= 1: #or min <= len(arr)
        mid = (min + max)//2
        if arr[mid] < item:
            min = mid + 1
        elif arr[mid] > item:
            max = mid - 1
        else: # if arr[mid] == item
            return mid
    
    return -10 # not in list

def findEmployee(fName, lName):
        '''
        To find staffId based on name provided

        Parameters
        ----------
        fName: string
            first name of employee
        lname: string
            last name of employee

        Return
        ------
        information: list[] or int
            A list containing the first name, last name, and staff id
        '''
        information = 0
        # opens the text file and returns the information as an array
        with open('library/employeeList.txt', 'r+') as readArray:
            content = readArray.readlines()
            for i in range(0, len(content)):
                # check if staff id is in the current line being checked
                if (fName in content[i]) and (lName in content[i]):
                    information = content[i]
                    information = ast.literal_eval(information)

        return information

def addEmployee(info, file):
    '''
    Adds the user to the database/file if not already stored
    '''
    #adds the employee to the database/file if the email is not already in database/file
    with open(file, 'r+') as readArray:
        content = readArray.readlines()
        if info not in content:
            # adds the customer information into the file/database
            readArray.write(str(info) + "\n")

    return

def clear():
    '''
    Clear the textfiles
    '''
    with open('library/employeeList.txt', 'w') as remove:
        remove.writelines('')
        remove.close()

    with open ('library/sortedEmpList.txt', 'w') as remove2:
        remove2.writelines('')
        remove2.close()

def addData(txt, data):
    '''
    Add data to file

    Parameters
    ----------
    txt: string
        name of the textfile
    data: information to add
    '''
    with open(txt,'a') as datas:
        datas.write(str(data) + "\n")

listOfEmpId = []
listOfId = []
listOfInitials = []

userFirst = ""
userLast = ""

for i in range(75000):
    name = names.get_full_name().split(" ") #generate name
    fName = name[0] # first name
    lName = name[1] # last name

    employee = Employee(fName, lName) #create object
    employee.addEmployee() #add employee into textfile if not already exist

    listOfEmpId.append(employee.staffId)

for a in listOfEmpId:
    entireId = findNumAndInitials(a)

    id = entireId[0] #the basis of sorting
    listOfId.append(id)
    ini = entireId[1]
    listOfInitials.append(ini)

copyOfId = listOfId.copy()

# INSERTION SORT
startIns = time.perf_counter()
insertionSort(listOfId, listOfInitials) #sort both lists in terms of the number portion of the empID
endIns = time.perf_counter()

logging.info("Insertion sort took: " + str(round((endIns-startIns)*10**3, 15)) + "ms")
logging.info(listOfEmpId)
addData('library/insertionData.txt', round((endIns-startIns)*10**3, 15))

# BULIT-IN SORT
startBI = time.perf_counter()
listOfEmpId.sort()
endBI = time.perf_counter()
logging.info(listOfEmpId)
logging.info("Built-in sort took: " + str(round((endBI-startBI)*10**3, 15)) + "ms")
addData('library/builtData.txt', round((endBI-startBI)*10**3, 15))

# Put the staffId together once more
for name in range(0, len(listOfId)):
    staffId = str(listOfId[name]) + str(listOfInitials[name])
    employeeInfo = Employee.findEmployee(staffId)
    addEmployee(employeeInfo, 'library/sortedEmpList.txt')

for i in range(0,10):
    print("\nWho would you like to search for? ")
    userFirst = input("First Name: ")
    userLast = input("Last Name: ")

    #Determining whether or not the user exists
    startF = time.perf_counter()
    empInfo = findEmployee(userFirst, userLast)
    endF = time.perf_counter()

    addData('library/DNE.txt', round((endF - startF)*10**3, 15))
    if empInfo != 0: # as long as the employee id does not equal 0 = DNE
        empFullId = findNumAndInitials(empInfo[-1])
        empId = empFullId[0]

        # LINEAR SEARCH - BEFORE SORTING
        startC = time.perf_counter()
        positionC = linearSearch(copyOfId, empId)
        endC = time.perf_counter()

        # LINEAR SEARCH
        startL = time.perf_counter()
        positionL = linearSearch(listOfId, empId)
        endL = time.perf_counter()

        # BINARY SEARCH
        startB = time.perf_counter()
        positionB = binarySearch(listOfId, empId)
        endB = time.perf_counter()

        if positionL != -10:
            lineStatusL = "at line " + str(positionL + 1)
        else:
            lineStatusL = "not"
        if positionB != -10:
            lineStatusB = "at line " + str(positionB + 1)
        else:
            lineStatusB = "not"
        if positionC != -10:
            lineStatusC = "at line " + str(positionC + 1)
        else:
            lineStatusC = "not"

        print(str(userFirst) + " " + str(userLast) + " is " + str(lineStatusL) + " in the ordered list of employees.")
        print(str(userFirst) + " " + str(userLast) + " is " + str(lineStatusB) + " in the ordered list of employees.")
        print(str(userFirst) + " " + str(userLast) + " is " + str(lineStatusC) + " in the list of employees.")
        
        addData('library/linear2Data.txt', round((endL-startL)*10**3, 15))
        addData('library/binaryData.txt', round((endB-startB)*10**3, 15))
        addData('library/linear1Data.txt', round((endC - startC)*10**3, 15))
    else: #if could not find the employee being demanded for
        print("This employee does not work at Tundra.")

# CLEAR DATA
clear()