import datetime


def getToday():
    time = datetime.datetime.now()
    return datetime.datetime(time.year, time.month, time.day)

if getToday() == getToday():
    print("dd")