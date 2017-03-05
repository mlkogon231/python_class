import datetime
from datetime import *
import pytz
from pytz import timezone
import time
now_utc = datetime.now(timezone('UTC'))


def getCurrentTimePortland():
    now_utc = datetime.now(timezone('UTC'))
    now_western = now_utc.astimezone(timezone('US/Pacific'))
    portland_Time = now_western.strftime('%H : %M : %S')
    print ('The current time at Portland Headquarters is  '+ portland_Time)
    if now_western.hour > 9 and now_western.hour < 21:
        print ("The Portland Headquarters is now Open.")
    else:
        print ("The Headquarters is now Closed.")

def nycTime():
    now_utc = datetime.now(timezone('UTC'))
    now_eastern = now_utc.astimezone(timezone('US/Eastern'))
    nyc_Time = now_eastern.strftime('%H : %M : %S')
    print ('The current time at the NYC branch is  '+ nyc_Time)
    if now_eastern.hour > 9 and now_eastern.hour < 21:
        print ("The NYC branch is now Open.")
    else:
        print ("The NYC branch is now Closed.")

def londonTime():
    now_utc = datetime.now(timezone('UTC'))
    now_europe = now_utc.astimezone(timezone('Europe/London'))
    london_Time = now_europe.strftime('%H : %M : %S')
    print ('The current time at the London branch is  '+ london_Time)
    if now_europe.hour > 9 and now_europe.hour < 21:
        print ("The London branch is now Open.")
    else:
        print ("The London branch is now Closed.")


getCurrentTimePortland()
nycTime()
londonTime()
