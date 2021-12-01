# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:38:41 2021

@author: Giada Sansonetto
"""

import json
from datetime import datetime

f = open('market-cap.json')

#interval = list(range(x-30

# cito i dati
data = json.load(f)

def day(n):
    date = data['values'][0]['x']
    fixeddate = datetime.fromtimestamp(date)
    #print(fixeddate)

for data in day(n):
    el = fixeddate.split('-')
    fixedyear = int(el[0])
    fixedmonth = int(el[1])
    
        

#for day(el[0]) in data:
    print(fixedyear)
