# dates are easily constructed and formatted
import os
from datetime import date, datetime, timedelta
import pytz


today = date.today() # this is same with now()
now = datetime.now()

def timezones():
    os.environ['TZ'] = 'Asia/Seoul' #change system default timezone
    datetime.now(tz=pytz.utc)
    datetime.now(tz=pytz.timezone('Asia/Seoul'))

date_jun_1 = datetime(2021, 6, 1)
nine_hour = now + timedelta(hours=9)
midnight = datetime(now.year, now.month, now.date())

# https://strftime.org/
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")  # '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
now.strftime("%y-%m-%d")  # '21-05-27
now.strftime("%y-%m-%d %H:%M:%S")  # '21-05-27 07:06:01

#%%
datetime.now().strftime("%Y-%m-%d") # '2021-09-27'
#%%

date_time = datetime.strptime("2021-06-01", '%Y-%m-%d')

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = today - birthday
age.days  # 14368



# %%
# milliseconds to date
ms = 0
dt = datetime.fromtimestamp(ms/1000)

# datetime to seconds
import time
time.mktime(now.timetuple())