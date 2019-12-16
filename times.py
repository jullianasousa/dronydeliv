# 2019-2020 Programação 1 (LTI)
# Grupo 13
# 53927 Julliana Sousa
# 54935 Tomás Neves

import constants

def timeToInt(time):
    """
    Transforms time on a list which the first element is the hour 
    and  the second is the minutes

    Requires: time str
    Ensures: List which first element is an hour and the second element
    is a minute
    """

    newTime = []

    time = time.split(':')

    hour = time[0]
    minutes = time[1]

    hour = int(hour)
    minutes = int(minutes)

    newTime.append(hour)
    newTime.append(minutes)

    return newTime

def dateToInt(date):
    """
    Transforms date on a list which the first element is the year, 
    the second is the month and the third is the day.

    Requires: date str
    Ensures: List which the first element is the year, 
    the second is the month and the third is the day.
    """

    newDate = []

    date = date.split('-')

    year = date[0]
    month = date[1]
    day = date[2]

    day = int(day)
    month = int(month)
    year = int(year)

    newDate.append(year)
    newDate.append(month)
    newDate.append(day)

    return newDate


def dateHeaderToStr(date):
    """
    Transforms the date header on a string.

    Requires: date list
    Ensures: string with day, month and year concatenated.
    """

    day = date[0]
    month = date[1]
    year = date[2]

    day = str(day)
    month = str(month)
    year = str(year)

    undoDate = day + '-' + month + '-' + year

    return undoDate



def timeHeaderToInt(time):
    """
    Transforms the time header on a list which the first element is the hour and 
    the second is the minutes.

    Requires: time str
    Ensures: list which first element is an hour and the second element
    is the minutes.
    """

    newTime = []

    time = time.split('h')

    hour = time[0]
    minutes = time[1]

    hour = int(hour)
    minutes = int(minutes)

    newTime.append(hour)
    newTime.append(minutes)

    return newTime

def seconds(time):
    """
    Transforms a given time in seconds.

    Requires: time str
    Ensures: Int with the sum of the first element of the list (hours) in seconds, 
    and of the second element of the list (minutes) in seconds.
    """

    time = timeToInt(time)
    time = (time[0] * 3600) + (time[1] * 60)

    return time


def secondsHeader(time):
    """
    Transforms the header time in seconds.

    Requires: time str
    Ensures: Int with the sum of the first element of the list (hours) in seconds, 
    and of the second element of the list (minutes) in seconds.
    """

    time = timeHeaderToInt(time)
    time = (time[0] * 3600) + (time[1] * 60)

    return time


def timeToStr(time):
    """
    Transforms a given time in string.

    Requires: time list
    Ensures: String with the elements of list time concatenated.
    """
    
    hour = time[0]
    minutes = time[1]

    minutes = str(minutes)
    hour = str(hour)

    undoTime = hour + ':' + minutes

    return undoTime


def sumThirtyMinutes(time):
    """
    Sums thirty minutes to time

    Requires: time str
    Ensures: String time with thirty minutes more
    """

    time = timeHeaderToInt(time)

    if (time[1] + 30) > 59:
        time[1] = (time[1] + 30) - 60
        if time[1] < 10:
            time[1] ='%02d' % time[1]
        if (time[0] + 1) < 24:
            time[0] = time[0] + 1
            if time[0] < 10:
                h = '%02d' % time[0]
        else:
            time[0] = (time[0] + 1) - 24
    else:
        time[1] += 30
    
    h = str(time[0])
    minutes = str(time[1])
  
    return h + 'h' + minutes


def attHeader(oldHeader):
    """
    Updates header

    Requires: oldHeader tuple
    Ensures: tuple with the first element being the updated day,
    the second element being the updated time, and the third element
    being the name of the company.
    """

    header = []

    if (secondsHeader(oldHeader[1]) + 30) >  secondsHeader("24h00"):
        header.append(attHeaderDate(oldHeader[0]))
        header.append(sumThirtyMinutes(oldHeader[1]))
        header.append(oldHeader[2])
    else:
        header.append(oldHeader[0])
        header.append(sumThirtyMinutes(oldHeader[1]))
        header.append(oldHeader[2])
    
    header = tuple(header)

    return header


def undoSeconds(seconds):
    """
    Turn seconds into hours and minutes and put in a list

    Requires: seconds int
    Ensures: list with the first element as hours and the second as minutes
    """

    time = []

    hour = seconds // 3600
    minutes = (seconds - (hour * 3600)) // 60

    time.append(hour)
    time.append(minutes)

    return time


def timeToDeliver(time, delivery): 
    """
    Sums a given drone time with the necessary time to deliver

    Requires: time and delivery str
    Ensures: string with the sum of the initial drone time with the time to deliver
    """

    time = seconds(time)
    time += (int(delivery) * 60)
    time = undoSeconds(time)

    if time[0] < 10:
        time[0] = '%02d' % time[0]
    if time[1] < 10:
        time[1] = '%02d' % time[1]

    return timeToStr(time)


def moreThan8(time):
    """
    Checks if delivery time is past 8pm

    Requires: time str
    Ensures: True if time is past 8pm, False otherwise.
    """

    time = timeToInt(time)

    if time[0] >= 20 and time[1] > 0:
        return True
    return False 
    


def changeTime(client, drones, calendar, parcels):
    """
    Adds required delivery time to drone time

    Requires: client int, drones, calendar and parcels list
    Ensures: Adds the required delivery minutes to the drone listing.
    """

    for x in drones:
        if calendar[client][constants.nameDroneParcels] == x[constants.nameDrone]:
            if moreThan8(timeToDeliver(calendar[client][constants.timeParcels], parcels[client][constants.necessaryTime])):
                x[constants.timeDrone] = "08:00"
            else:
                x[constants.timeDrone] = timeToDeliver(calendar[client][constants.timeParcels], parcels[client][constants.necessaryTime])



def attTimeCalendar(client, parcels, calendar, drones):
    """
    Modifies drone delivery time to order time if it's higher. 

    Requires: client int, parcels e calendar list
    Ensures: Modifies the drone delivery time to the longest time between the order time and the drone time.
    """

    for x in drones:
        if calendar[client][constants.nameDroneParcels] == x[constants.nameDrone]:
            if seconds(calendar[client][constants.timeParcels]) <= seconds(parcels[client][constants.timeClient]):
                calendar[client][constants.timeParcels] = parcels[client][constants.timeClient]
                if moreThan8(timeToDeliver(calendar[client][constants.timeParcels], parcels[client][constants.necessaryTime])):
                    calendar[client][constants.timeParcels] = "08:00"
                    calendar[client][constants.dateParcels] = attDate(calendar[client][constants.dateParcels])
                    x[constants.dateDrone] = attDate(x[constants.dateDrone])
            else:
                calendar[client][constants.timeParcels] = x[constants.timeDrone]
                if moreThan8(timeToDeliver(calendar[client][constants.timeParcels], parcels[client][constants.necessaryTime])):
                    calendar[client][constants.timeParcels] = "08:00"
                    calendar[client][constants.dateParcels] = attDate(calendar[client][constants.dateParcels])



def attHeaderDate(date):
    """
    Updates header's date

    Requires: date str
    Ensures: str with the updated header's date

    """

    date = dateToInt(date)

    if date[0] + 1 > 30:
        date[0] = 1
        if date[1] + 1 > 12:
            date[1] = 1
            date[2] += 1
        else:
            date[1] += 1
    else: 
        date[0] += 1
    
    date = dateHeaderToStr(date)

    return date


def attDate(date):
    """
    Updates general dates

    Requires: date str
    Ensures: str with the updated date
    """

    date = dateToInt(date)

    if date[2] + 1 > 30:
        date[2] = 1
        date[2] = '%02d' % date[2]
        if date[1] + 1 > 12:
            date[1] = 1
            date[1] = '%02d' % date[1]
            date[0] += 1
        else:
            if date[1] < 10:
                date[1] += 1
                date[1]= '%02d' % date[1]
            else:
                date[1] += 1
    else: 
        if date[2] < 10:
            date[2] += 1
            date[2] = '%02d' % date[2]
        else:
            date[2] += 1
    
    year = str(date[0])
    month = str(date[1])
    day = str(date[2])

    return year + '-' + month + '-' + day
