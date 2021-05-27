# thread를 직접 설정해줘야함.
import threading

import schedule
import time
import asyncio
def job():
    print("I'm working...")
def job2():
    print("I'm working...2")

schedule.every(1).seconds.do(job)
schedule.every(2).seconds.do(job2)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


