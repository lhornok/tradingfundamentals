# coding: utf-8
# https://www.bls.gov/developers/api_python.htm

from datetime import datetime
from datetime import timedelta

import requests
import ics
import pytz
import findTimeZone


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

calendarURL = "https://www.bls.gov/schedule/news_release/bls.ics"

# Just in case we want to get calendar for another day
date = datetime.now() + timedelta(days=0)
datefor = "%s" % date.strftime("%Y-%m-%d")

r = requests.get(calendarURL,headers=headers)
calendar = ics.Calendar(r.text)
lstEvents = []
for event in calendar.events:
    if (event.name not in lstEvents):
        lstEvents.append(event.name)
    if (event.name == 'Producer Price Index'):
        timezone = findTimeZone.getTimeZoneCity(strCityName=event.location)
        print (event.location, timezone, event.name, event.begin)
        print ('-'*80)

#for eventName in lstEvents:
    #print (eventName)