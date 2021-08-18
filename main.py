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
LOWER_BOUND = int(os.getenv('LOWER_BOUND', 25))
UPPER_BOUND = int(os.getenv('UPPER_BOUND', 90))
TURN_OFF_URL = f'https://maker.ifttt.com/trigger/turn_plug_off/with/key/{WEBHOOK_KEY}'
TURN_ON_URL = f'https://maker.ifttt.com/trigger/turn_plug_on/with/key/{WEBHOOK_KEY}'

battery = psutil.sensors_battery()
is_plugged = battery.power_plugged
percent = battery.percent

if not is_plugged and percent <= LOWER_BOUND:
    r = requests.post(url=TURN_ON_URL)
elif is_plugged and percent >= UPPER_BOUND:
    r = requests.post(url=TURN_OFF_URL)