# 2019-2020 Programação 1 (LTI)
# Grupo 13
# 53927 Julliana Sousa
# 54935 Tomás Neves

import sys
import readFiles
import constants
import times
import organize
import writeFiles
import copy

def validation(nameFile, fileContent):
        """
        Checks for consistency between a file name and its header content.    

        Requires: nameFile str and fileContent list
        Ensures: true if the file name is consistent with its header content
        false if the file name is not consistent with the file header
        """


        dayNameFile = nameFile[-5:-4]
        monthNameFile = nameFile[-8:-6]
        yearNameFile = nameFile[-13:-9]
        hourNameFile = nameFile[-19:-14]
        hourNameFile = hourNameFile.replace("h", "")
        

        if nameFile[0:6] == "drones":
                scopeNameFile = nameFile[0:6]
        elif nameFile[0:7] == "parcels":
                scopeNameFile = nameFile[0:7]

        headerFileContent = fileContent[constants.header]
        dateFile = headerFileContent[constants.headerTime]
        dayFile = dateFile[0:1]
        monthFile = dateFile[2:4]
        yearFile = dateFile[5:9]
        hourFile = headerFileContent[1]
        hourFile = hourFile.replace("h", "")
        scopeFile = headerFileContent[constants.scope]


        return hourNameFile == hourFile and dayNameFile == dayFile and monthNameFile == monthFile and yearNameFile == yearFile and scopeNameFile == scopeFile


def validation2(fileContent1, fileContent2):
        """
        Checks for inconsistency between both headers content in both files.

        Requires: fileContent1 and fileContent2 lists.
        Ensures: true if both files header are consistent with eachother
        false if both files name are not consistent with eachother.
        """
        
        return fileContent1[constants.header][constants.headerTime] == fileContent2[constants.header][constants.headerTime] and fileContent1[constants.header][constants.headerDay] == fileContent2[constants.header][constants.headerDay] and fileContent1[constants.header][constants.company] == fileContent2[constants.header][constants.company] 



def allocate(fileNameDrones, fileNameParcels):
        """
        Assign given drones to given parcels.
        
        Requires: fileNameDrones, fileNameParcels are str, with the names
        of the files representing the list of drones and parcels, respectively,
        following the format indicated in the project sheet.
        Ensures: Two output files, respectively, with the listing of scheduled
        transportation of parcels and the updated listing of drones, following the format
        and naming convention indicated in the project sheet.
        """


        calendar = []
        dronesList = []


        # Create timetable list
        for i in range(len(parcelsFile)):
                if i > 0:
                        organize.attribution(i, calendar, dronesFile, parcelsFile)
                else:
                        calendar.append(parcelsFile[i])

        #Organize timetable's list  
        calendar = organize.organizeLists(calendar)

        dronesFile[constants.header] = times.attHeader(dronesFile[constants.header])
        droneHeader = dronesFile.pop(0)
        dronesList.append(droneHeader)
        sizeDrones = len(dronesFile)

        # Organize drone's list
        for i in range(sizeDrones):
                drony = copy.deepcopy(dronesFile)
                organize.organizeDroneList(dronesList, drony, dronesFile)

        # Create drone's and calendar's output files
        writeFiles.writeTimetableFile(calendar, "timetable")
        writeFiles.writeDroneFile(dronesList, "drone")




inputFileName1, inputFileName2 = sys.argv[1:]

dronesFile = readFiles.readDronesFile(inputFileName1)
parcelsFile = readFiles.readParcelsFile(inputFileName2)

try:
        assert validation(inputFileName1, dronesFile)
except:
        raise IOError("Input error: name and header inconsistent in file " + inputFileName1 + ".")
        
try:
        assert validation(inputFileName2, parcelsFile)
except:
        raise IOError("Input error: name and header inconsistent in file " + inputFileName2 + ".")
        
try:
        assert validation2(dronesFile, parcelsFile)
except:
        raise IOError("Input error: inconsistent files" + inputFileName1 + " and " + inputFileName2 + ".")

allocate(inputFileName1, inputFileName2)



