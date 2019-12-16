# 2019-2020 Programação 1 (LTI)
# Grupo 13
# 53927 Julliana Sousa
# 54935 Tomás Neves

import times
import constants
import copy


def attribution(client, calendar, drones, parcels):
    """
    Assigns the most satisfying drone to a parcel.

    Requires: client int, calendar, drones and parcels list
    Ensures: Assigns the most satisfying drone to a parcel.
    """

    possibilities = []
    copydrones = copy.deepcopy(drones)
    copyParcels = copy.deepcopy(parcels)

    for x in range(1, len(copydrones)):
        if copyParcels[client][constants.clientZone] == copydrones[x][constants.operationZone]:
            if (int(copyParcels[client][constants.distance]) * 2) <= (float(copydrones[x][constants.autonomy]) * 1000):
                if (int(copyParcels[client][constants.distance])) <= (float(copydrones[x][constants.maxDistance])):
                    if (int(copyParcels[client][constants.weightClient])) <= (float(copydrones[x][constants.weightDrones])):
                        possibilities.append(copy.deepcopy(copydrones[x]))

    if len(possibilities) > 1:
        biggestAutonomy = possibilities[0][constants.autonomy]
        smallestDistance = possibilities[0][constants.totalDistance]
        smallestTime = possibilities[0][constants.timeDrone]

        for x in possibilities: # check which is the shortest time
            if times.seconds(x[constants.timeDrone]) < times.seconds(smallestTime):
                smallestTime = x[constants.timeDrone]
        removeElements(possibilities, constants.timeDrone, smallestTime)
        if len(possibilities) > 1:
            for x in possibilities: # check what is the greatest autonomy
                if float(x[constants.autonomy]) > float(biggestAutonomy): 
                    biggestAutonomy = x[constants.autonomy]
            removeElements(possibilities, constants.autonomy, biggestAutonomy)
            if len(possibilities) > 1:
                for x in possibilities: # check what is the smallest accumulated distance
                    if float(x[constants.totalDistance]) < float(smallestDistance):
                        smallestDistance = x[constants.totalDistance]
                removeElements(possibilities, constants.totalDistance, smallestDistance)
                if len(possibilities) > 1:
                    possibilities.sort() # put in lexicographic order
                    cont = len(possibilities)
                    while cont != 1:
                        possibilities.pop(cont - 1)
                        cont = cont - 1
                createParcelsList(client, calendar, possibilities, copyParcels)
            else:
                createParcelsList(client, calendar, possibilities, copyParcels)
        else:
            createParcelsList(client, calendar, possibilities, copyParcels)
    elif len(possibilities) == 1: 
        createParcelsList(client, calendar, possibilities, copyParcels)
    else:
        calendar.append([copyParcels[client][constants.dateClient]])
        calendar[client].append(copyParcels[client][constants.timeClient])
        calendar[client].append(copyParcels[client][constants.nameClient])
        calendar[client].append("cancelled")

    if calendar[client][constants.nameDroneParcels] != 'cancelled': # verifica se houve atribuição de um drone à uma encomenda.
        times.attTimeCalendar(client, parcels, calendar, drones)
        attAutonomy(client, calendar, drones, parcels)
        attTotalDistance(client, calendar, drones, parcels)
        times.changeTime(client, drones, calendar, parcels)


def removeElements(possibilities, element, case):
    """
    Removes drones that do not fit required

    Requires: possibilities list, element and case int
    Ensures: Remove drones that are different from case
    """

    for i in possibilities:
        if i[element] != case:
            possibilities.remove(i)


def createParcelsList(client, calendar, possibilities, parcels):
    """
    Create order assignment list

    Requires: client int, calendar, possibilities and parcels list
    Ensures: Create a list within a list with the day, time, name of the client and the name of the drone
    """
    calendar.append([possibilities[0][constants.dateDrone]])
    calendar[client].append(possibilities[0][constants.timeDrone])
    calendar[client].append(parcels[client][constants.nameClient]) 
    calendar[client].append(possibilities[0][constants.nameDrone])


def attAutonomy(client, calendar, drones, parcels):
    """
    Updates the autonomy of a drone

    Requires: client int, calendar, drones e parcels list
    Ensures: Decreases the distance traveled to and from base to delivery address
    """

    for x in drones:
        if calendar[client][constants.nameDroneParcels] == x[constants.nameDrone]:
            x[constants.autonomy] = str(round(float(x[constants.autonomy]) - (int(parcels[client][constants.distance]) * 2) / 1000, 1))


def attTotalDistance(client, calendar, drones, parcels):
    """
    Updates the total distance traveled by a drone

    Requires: client int, calendar, drones e parcels list
    Ensures: It adds to the total distance traveled the distance traveled to go to the shipping 
    address and back to base
    """

    for x in drones:
        if calendar[client][constants.nameDroneParcels] == x[constants.nameDrone]:
            x[constants.totalDistance] = str(round(float(x[constants.totalDistance]) + (int(parcels[client][constants.distance]) * 2) / 1000, 1))


def organizeLists(desorganizedList):

    """
    Get a list of assigned drones and arrange it to specification

    Requires: a desorganizedList list
    Ensures: a list according to specification
    """

    organizedList = [ ]
    header = desorganizedList.pop(0)
    organizedList.append(header)
    
    newList = [ ]
    cancelledList = [ ]
    
    for i in desorganizedList:
        tempList = [ ]
        for e in i:
            e = e.replace(":", "")
            tempList.append(e)
        newList.append(tempList)     

    for i in newList:
        for e in i:
            if e == "cancelled":
                cancelledList.append(i)

                
    if len(cancelledList) >= 1:
        for i in range(len(cancelledList)):
            cancelledClient = organizeHours(cancelledList)
            organizedList.append(cancelledClient)
            cancelledList.remove(cancelledClient)
            newList.remove(cancelledClient)


    for i in range(len(newList)):
        clientName = organizeHours(newList)
        organizedList.append(clientName)
        newList.remove(clientName)
    
    for i in range(len(organizedList)):
        if i > 0:
            hour = organizedList[i][1][0:2] + ":" + organizedList[i][1][2:4]
            oldHour = organizedList[i][1]
            organizedList[i].remove(oldHour)
            organizedList[i].insert(1, hour)

    return organizedList

def organizeHours(hourList):

    """
    Arrange hours from early to later.

    Requires: a hourList list.
    Ensures: the list that contains the shortest time.
    """
    
    smallestHour = hourList[0]
    
    for i in hourList:
        
        if i[1] <= smallestHour[1]:
            if i[1] < smallestHour[1]:
                smallestHour = i
            elif i[1] == smallestHour[1]:
                smallestHour = organizeClients(i, smallestHour)
           
    return smallestHour


def organizeClients(smallestHour, oldSmallestHour):
    """
    Arranges the customer list in alphabetical order.

    Requires: smallestHour list and oldSmallestHour list
    Ensures: the list that contained the client that comes first in a alphabetic order
    """

    temp = [ ]
    temp.append(smallestHour[2])
    temp.append(oldSmallestHour[2])

    temp.sort()
    
    if temp[0] == smallestHour[2]:
        return smallestHour
    return oldSmallestHour


def organizeDroneList(dronesList, copyDrones, originalDrones):
    """
    Organize the updated drone list

    Requires: dronesList, copyDrones and originalDrones list
    Ensures: Organizes the updated list of drones according to time, autonomy or lexicographic order.
    """

    smallestTime = copyDrones[0]
    sameTime = []
    smallestDate = times.dateToInt(copyDrones[0][constants.dateDrone])

    for drone in copyDrones: # check the smallest date
        date = times.dateToInt(drone[constants.dateDrone])
        if date[2] < smallestDate[2]:
            if date[1] <= smallestDate[1]:
                if date[0] <= smallestDate[0]:
                    smallestDate[0] = date[0]
                    smallestDate[1] = date[1]
                    smallestDate[2] = date[2]


    for drone in copyDrones: # check the smallest time
        date = times.dateToInt(drone[constants.dateDrone])
        if (times.seconds(drone[constants.timeDrone]) <= times.seconds(smallestTime[constants.timeDrone])) and date[0] == smallestDate[0] and date[1] == smallestDate[1] and date[2] == smallestDate[2]:
            if times.seconds(drone[constants.timeDrone]) < times.seconds(smallestTime[constants.timeDrone]):
                sameTime = []
                smallestTime = drone
                sameTime.append(drone)
            else:
                sameTime.append(drone)
    
    
    if len(sameTime) > 1:
        biggestAutonomy(sameTime)
        if len(sameTime) > 1:
            sameTime.sort()
            cont = len(sameTime)
            while cont != 1:
                sameTime.pop(cont - 1)
                cont = cont - 1
            dronesList.append(sameTime[0])
            removeFromDrones(sameTime[0], originalDrones)
        else:
            dronesList.append(sameTime[0])
            removeFromDrones(sameTime[0], originalDrones)
    else:
        dronesList.append(smallestTime)
        removeFromDrones(smallestTime, originalDrones)
    

def biggestAutonomy(sameTime):
    """
    Check what is the greatest autonomy

    Requires: sameTime list
    Ensures: Checks for the highest autonomy and removes the lowest autonomy.
    """

    biggerAutonomy = sameTime[0]
  
    for drone in sameTime:
        if float(drone[constants.autonomy]) > float(biggerAutonomy[constants.autonomy]):
            sameTime = sameTime.remove(biggerAutonomy)
            biggerAutonomy = drone
        elif float(drone[constants.autonomy]) < float(biggerAutonomy[constants.autonomy]):
            sameTime = sameTime.remove(drone)
      


def removeFromDrones(sameTime, drones):
    """
    Remove from the drone list what has already been organized

    Requires: sameTime and drones list
    Ensures: Remove from the drone list what has already been organized
    """

    for drone in drones:
        if sameTime[constants.nameDrone] == drone[constants.nameDrone]:
            drones.remove(drone)

