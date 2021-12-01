# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:38:41 2021

@author: Giada Sansonetto
"""

import json
from datetime import datetime

f = open('market-cap.json')

data = json.load(f)

# definisco anno-mese-giorno 
def day(n):
    date = data['values'][0]['x']
    fixeddate = datetime.fromtimestamp(date)
    #print(fixeddate)

# suddivido elementi
for data in day(n):
    el = fixeddate.split('-')
    fixedyear = int(el[0])
    fixedmonth = int(el[1])
    
        

#for day(el[0]) in data:
    print(fixedyear)
