# 2019-2020 Programação 1 (LTI)
# Grupo 13
# 53927 Julliana Sousa
# 54935 Tomás Neves

def nameFiles(attributionList, nameList):
    """
    Get a list and check if it's a drone list or a timetable list.

    Requires: a list a his name
    Ensures: a string
    """
    if nameList == "drone":
        name = "drones"
    else:
        name = "timetable"
        
    hour = str(attributionList[0][1])

    yearTemp = str(attributionList[0][0]) + " "
    year = yearTemp[-5:-1]

    monthTemp = str(attributionList[0][0])
    month = monthTemp[-7:-5]

    dayTemp = str(attributionList[0][0])
    day = dayTemp[-10:-8]

    fileName = name + hour + "_" + year + "y" + month + "m" + day + ".txt"

    return fileName


def writeDroneFile(dronesList, nameList):
    """
    get a list and write it to a .txt file

    Requires: a list a his name
    Ensures: a .txt file with the content of the list
    """
    fileName = nameFiles(dronesList, nameList)

    inFile = open(fileName, "w")

    parcels = " "

    inFile.write("Time: \n")
    inFile.write(dronesList[0][1])
    inFile.write("\n")
    inFile.write("Day: \n")
    inFile.write(dronesList[0][0])
    inFile.write("\n")
    inFile.write("Company: \n")
    inFile.write(dronesList[0][2])
    inFile.write("\n")
    inFile.write("Drones:")
    inFile.write("\n")
    for drones in dronesList:
        if dronesList.index(drones) >= 1:
            parcels = ""
            for elements in drones:
                elements = str(elements)
                parcels += elements
                parcels += ", "
            parcels = parcels[0:(len(parcels)-2)]
            inFile.write(parcels)
            inFile.write("\n")

    inFile.close( )

def writeTimetableFile(timetableList, nameList):
    """
    get a list and write it to a .txt file

    Requires: a list a his name
    Ensures: a .txt file with the content of the list
    """
    fileName = nameFiles(timetableList, nameList)

    inFile = open(fileName, "w")

    parcels = " "

    inFile.write("Time: \n")
    inFile.write(timetableList[0][1])
    inFile.write("\n")
    inFile.write("Day: \n")
    inFile.write(timetableList[0][0])
    inFile.write("\n")
    inFile.write("Company: \n")
    inFile.write(timetableList[0][2])
    inFile.write("\n")
    inFile.write("Timeline:")
    inFile.write("\n")
    for drones in timetableList:
        if timetableList.index(drones) >= 1:
            parcels = ""
            for elements in drones:
                elements = str(elements)
                parcels += elements
                parcels += ", "
            parcels = parcels[0:(len(parcels)-2)]
            inFile.write(parcels)
            inFile.write("\n")

    inFile.close( )


