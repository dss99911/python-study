# dates are easily constructed and formatted
from datetime import date, datetime, timedelta
today = date.today() # datetime.date(2003, 12, 2)
now = datetime.now()
nine_hour = now + timedelta(hours=9)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")  # '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
π
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = today - birthday
age.days  # 14368

# %%
# milliseconds to date
ms = 0
dt = datetime.fromtimestamp(ms/1000)