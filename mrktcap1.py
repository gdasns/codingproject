# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 16:21:45 2021

@author: Giada Sansonetto
"""

import json
from datetime import datetime
import matplotlib.pyplot as plt 
    
def average(n):
    total = 0
    count = 0
    for el in xs:
        total = total + el
        count = count + 1
    avg = total/count 
    return avg

def smooth(x):
    # create a list
    newlist = []
    
    # evaluate interval in which calculate the mean
    interval = range((x - onemonth),(x + onemonth))
    for el in interval:
        newlist.append(average(el))
    return newlist

    
f = open('market-cap.json')



# refer to the data
data = json.load(f)

#timestamp = data['values'][0]['x']
#datefrom = str(datetime.fromtimestamp(timestamp).date())

lasttimestamp = data['values'][1500]['x']
lastdate = str(datetime.fromtimestamp(lasttimestamp).date())

# define data and axes
values = data['values']
xs = [el['x'] for el in values]
ys = [el['y'] for el in values]

# convert timestamp to value
xss = [str(datetime.fromtimestamp(t).date()) for t in xs]

# build the plot and label it
fig, ax = plt.subplots()
ax.plot(xss, ys, color = 'yellow')
ax.set_title('Bitcoin market capitalization')
ax.set_xlabel('time')
ax.set_ylabel('Market Capitalization in USD')
ax.xaxis.set_major_locator(plt.MaxNLocator(5))

fig.autofmt_xdate()
plt.xticks(rotation = 90)

onemonth = 60*60*24*30


for i in range(0, 10):
    for ['values'][i] in xs:
        print(average(['values'][i]))


