"""
Daily alarm
Format used: H:M e.g. 10:12
24H format
"""
from datetime import datetime
import re


def return_time():
    date_and_time = datetime.now().strftime('%H:%M')
    return date_and_time


def start_clock():
    i = 1
    wake_up_time = raw_input("Enter time format \"H:M\": ")
    if not (re.match("[0-1][0-9]:[0-5][0-9]", wake_up_time) or re.match("2[0-3]:[0-5][0-9]", wake_up_time)):
        print "did not understand the time format please use the following format H:M e.g. 10:12"
        return
    while i:
        now = return_time()
        if now == wake_up_time:
            print "wake up"
            i = 0


start_clock()
