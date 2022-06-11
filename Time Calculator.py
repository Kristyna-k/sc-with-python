#Write a function named add_time that takes in two required parameters and one optional parameter:
#a start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive

#The function should add the duration time to the start time and return the result.
#If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.


def add_time(time, duration, day = None):
    if 'AM' in time:
        noon = "AM"         #part of day
    else:
        noon = "PM"
    
    len_time = len(time)
    time = time[:len_time-3]           #get the time
    time = time.split(':')
    hour = int(time[0])         #get the hour
    minute = int(time[1])            #get minutes
    #print(hour, minute)

    duration = duration.split(':')
    dhour = int(duration[0])
    dminute = int(duration[1])
    #print(dhour, dminute)

    if noon == 'PM':
        hour = hour + 12          #make stupid PM and AM into normal 24-hours time
        #print(hour)
    
    hour = hour + dhour         #total hours
    minute = minute + dminute           #total minutes
    if minute > 59:
        hour = hour + 1
        minute = minute - 60
        if minute < 10:
            minute = "0" + str(minute)

    x = 0
    while hour > 12:
        x += 1
        hour -= 12          #taking it back to AM and PM

    time = str(hour) + ':' + str(minute)            #give total time
    #print(time)         

    #print(x)

    if x == 0 or x%2 == 0:          #deciding between AM and PM    
        noon = "AM"
    else:
        noon = "PM"
        x = x - 1

    #print(time, noon)           #FINAL TIME

    when = None
    if x == 2 or x == 3:
        when = 'next day'
        x == 1
    elif x > 3:
        if x%2 != 0:
            x -= 1
        x = x / 2
        when = str(int(x)) + ' days later.'          #how many days later
    elif x < 2:
        x == 0

    #print(when)

    fday = None
    if day != None:
        if day.lower() == 'monday':
            fday = 0 + x 
        elif day.lower() == 'tuesday':
            fday = 1 + x
        elif day.lower() == 'wednesday':
            fday = 2 + x
        elif day.lower() == 'thursday':
            fday = 3 + x 
        elif day.lower() == 'friday':
            fday = 4 + x
        elif day.lower() == 'saturday':
            fday = 5 + x
        elif day.lower() == 'sunday':
            fday = 6 + x
    
        if fday%7 == 0:
            day = 'Monday'
        elif fday%7 == 1:
            day = 'Tuesday'
        elif fday%7 == 2:
            day = 'Wednesday'
        elif fday%7 == 3:
            day = 'Thursday'
        elif fday%7 == 4:
            day = 'Friday'
        elif fday%7 == 5:
            day = 'Saturday'
        elif fday%7 == 6:
            day = 'Sunday'

       # print(day, x)

    if day == None and when == None:
        print(time, noon)
    elif day == None and when != None:
        print(time, noon, '(' + when + ')' )
    elif day != None and when == None:
        print(time, noon + ',', day)
    else:
        print(time, noon + ',', day, '(' + when + ')' )

    return()


add_time("10:10 PM", "3:30")
