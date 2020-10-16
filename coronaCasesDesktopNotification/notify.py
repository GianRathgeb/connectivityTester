# Import modules (overview in readme.md)

import datetime
import time
import requests
from plyer import notification
import os

# Set variables
cData = None

strDirName, strFileName = os.path.split(os.path.abspath(__file__))

# Try to get the data from the api
try:
    # Get data from api
    cData = requests.get(
        "https://corona-rest-api.herokuapp.com/Api/Switzerland")
except:
    # Message if script can't get the data from  the api
    print("System is busy, try later again or check your internet connection")

# If data is downloaded
if (cData != None):

    # Get the root json object
    data = cData.json()['Success']

    while True:
        # Create the notification
        notification.notify(
            # Title of the notification
            title = f"COVID19 Stats of Switzerland on {datetime.date.today()}",
            # Message of the notification, can be multiline
            message = f"Total cases : {data['cases']}\nToday cases: {data['todayCases']}\nToday deaths : {data['todayDeaths']}\nTotal active : {data['active']}",
            # App name in the notification
            app_name = "Gian Rathgeb Corona Notification",
            # Icon that shows up in the notifiaction
            app_icon = os.path.join(strDirName, "icon.ico"),
            # Time until the notification fades away
            timeout = 30
        )
        # Time until the notification shows up again
        time.sleep(60*60)
