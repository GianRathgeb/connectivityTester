import datetime
import time
import requests
from plyer import notification
import os

cData = None

strDirName, strFileName = os.path.split(os.path.abspath(__file__))

try:
    cData = requests.get(
        "https://corona-rest-api.herokuapp.com/Api/Switzerland")
except:
    print("System is busy, try later again or check your internet connection")

if (cData != None):
    data = cData.json()['Success']

    while True:
        notification.notify(
            title = f"COVID19 Stats of Switzerland on {datetime.date.today()}",

            message = f"Total cases : {data['cases']}\nToday cases: {data['todayCases']}\nToday deaths : {data['todayDeaths']}\nTotal active : {data['active']}",

            app_name = "Gian Rathgeb Corona Notification",

            app_icon = os.path.join(strDirName, "icon.ico"),

            timeout = 60
        )

        time.sleep(60*60)
