# for converting string into list
import ast

class Works():
  '''
  A class that holds the different work objects

  Attibutes
  ---------
  genre: string
      The type of genre
    
  name: string
    The title of the work

  author: string
    The author of the work

  price: float
    The price of the work

  synopsis: string
    A short overview of the work

  work: string
    Indication of what type of work this is; book or video games

  Methods
  -------
  addWork() -> string
    Generate a string in a form of a list containing the information of the work
  convertWorks() -> list
    Find and convert the work back into a list
  '''

  def __init__(self, genre, name, author, price, synopsis, work):
    '''
    Constructor to build this object

    Parameters
    ----------
    genre: string
      The type of genre
    
    name: string
      The title of the work

    author: string
      The author of the work

    price: float
      The price of the work

    synopsis: string
      A short overview of the work

    work: string
      Indication of what type of work this is; book or video games
    '''
    self.genre = genre
    self.name = name
    self.author = author
    self.price = price
    self.synopsis = synopsis
    #replaces the ' with \' to prevent crashes later on
    if "'" in self.synopsis:
      self.synopsis.replace("'", "\'")
    
    self.work = work
  
  def addWork(self) -> list:
    '''
    Create the individual genre headings into a genre table

    Returns
    -------
    work: string[]
      A list of all the information of this work in one place
    '''
    genreTypes = ["adventure", "fantasy", "romance", "thriller"]
    work = []
    # checks if the genre is one of the options
    if (self.genre in genreTypes):
      # reads the current state of the textfile
      # with open('library/{}/{}/{}.txt'.format(self.work, self.genre, self.genre), 'r') as textFile:
      #   fileContent = textFile.readlines()
      
      # maybe use the search work function
      # checks if the title of the book already exists or not  
      content = Works.convertWorks(self.genre, self.work)
      if (self.name not in content):
        with open('library/{}/{}/{}.txt'.format(self.work, self.genre, self.genre),'a+') as outfile :
          # append all the information into the work list created earlier
          work.append(self.genre)
          work.append(self.name)
          work.append(self.author)
          work.append(self.price)
          work.append(self.synopsis)
          # converted into string, as textfiles only support string types
          workString = str(work)
          # append the work list into the file
          outfile.write(workString + "\n")

    return work
  
  def convertWorks(genre, work):
    '''
    To convert all the works currently stored in 'database' back into a list/array for easy access

    Parameters
    ----------
    genre: string
      The type of genre

    work: string
      Indication of what type of work this is; book or video games

    Returns
    -------
    workTitles: dictionary{}
      An dictionary of all the titles in one place
    '''
    #to store all the names of the works in one place as keys
    workTitles = {}
    with open('library/{}/{}/{}.txt'.format(work,genre,genre), 'r') as readArray:
      #stores the text within fileContent
      fileContent = readArray.readlines()
      #checking how many works are stored within this file
      fileLength = len(fileContent)
      for total in range(0,fileLength):
        #checking the individual works
        specificLine = fileContent[total]
        #convert the string contained within the file into a list
        specificLine = ast.literal_eval(specificLine)
        title = specificLine[1]
        author = specificLine[2]
        summary = specificLine[4]
        price = specificLine[3]
        # makes it accessible to access the name of the work along with its author, summary, and price
        workTitles[title] = [author, summary, price]

    return workTitles