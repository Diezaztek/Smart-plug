#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 14:01:29 2021

@author: fracisco.torres
"""

import psutil
import requests
import os

from dotenv import load_dotenv
load_dotenv()

WEBHOOK_KEY = os.getenv('WEBHOOK_KEY')
TURN_OFF_URL = f'https://maker.ifttt.com/trigger/turn_plug_off/with/key/{WEBHOOK_KEY}'
TURN_ON_URL = f'https://maker.ifttt.com/trigger/turn_plug_on/with/key/{WEBHOOK_KEY}'

battery = psutil.sensors_battery()
is_plugged = battery.power_plugged
percent = battery.percent

if not is_plugged and percent <= 25:
    print("Turn on")
    r = requests.post(url=TURN_ON_URL)
    print(r.json)
elif is_plugged and percent >= 90:
    print("Turn off")
    r = requests.post(url=TURN_OFF_URL)
    print(r.json)
else:
    print('No action required')
