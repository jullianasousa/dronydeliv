# 2019-2020 Programação 1 (LTI)
# Grupo 13
# 53927 Julliana Sousa
# 54935 Tomás Neves


def readDronesFile(fileName):
    """
    Converts a given file listing drones into a collection.
    
    Requires: fileName is str, the name of a .txt file listing drones,
    following the format specified in the project sheet.
    Ensures: list whose first element is a tuple with the header of 
    file fileName and the rest of the elements are a list with the 
    information of each drone available at the moment.
    """


    outputList = []
    
    
    fileIn = open(fileName, 'r')

    outputList.append(readHeader(fileIn))

    for line in fileIn:
        line = line.strip().replace("\n", "").split(", ")
        outputList.append(line)

    fileIn.close()

    return outputList


def readParcelsFile(fileName):
    """
    Converts a given file listing parcels into a collection.
    
    Requires: fileName is str, the name of a .txt file listing parcels,
    following the format specified in the project sheet.
    Ensures: list whose first element is a tuple with the header of 
    file fileName and the rest of the elements are a list with the 
    information of each parcel available at the moment.
    """

    outputList = []
    
    
    fileIn = open(fileName, 'r')

    outputList.append(readHeader(fileIn))

    for line in fileIn:
        line = line.strip().replace("\n", "").split(", ")
        outputList.append(line)

    fileIn.close()

    return outputList



def readHeader(fileName):
    """
    Converts the header of a given file into a tuple.

    Requires: fileName is str, the name of a .txt file
    listing drones, following the format specified in the
    project sheet.
    Ensures: tuple which first element is the day, the second
    is the time, the third is the company's name and the fourth
    is the scope.

    """
    
    fileName.readline()
    time = fileName.readline().strip().replace("\n", "")
    fileName.readline()
    day = fileName.readline().strip().replace("\n", "")
    fileName.readline()
    company = fileName.readline().strip().replace("\n", "")
    scope = fileName.readline().strip().replace("\n", "").replace(":", "").replace("P", "p").replace("D", "d")
    
    return (day, time, company, scope)

