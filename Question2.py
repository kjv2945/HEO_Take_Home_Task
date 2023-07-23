import json
import requests
import requests_cache
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.wheretheiss.at/v1/satellites/25544" #api used for ISS data

requests_cache.install_cache('demo_cache') #cache response from api
altitudea = [] #array for morning altitude
altitudeb = [] #array for night altitude
averages = [] #array for average of altitudes
time1 = np.arange(1658561206,1690097206,86400) #epoch time 24/7/22 - 23/7/22 with 24 hour intervals
time2 = np.arange(1658518006,1690054006,86400) #time 1 = morning, time 2= night
days = pd.date_range(start='2022-07-24',end='2023-07-23') #year range for plot

for x in time1 : #loop to return altitudes for time range 1
     params = {
     'timestamps' : x,
     }
     response = requests.get(url, params=params)
     json_payload = response.json()
     altitude = (json_payload["altitude"])
     altitudea.append(altitude)

for x in time2 : #loop to return altitudes for time range 2
     params = {
     'timestamps' : x,
     }
     response = requests.get(url, params=params)
     json_payload = response.json()
     altitude = (json_payload["altitude"])
     altitudeb.append(altitude)

for (a, b) in zip(altitudea, altitudeb) : #loop to find daily average
    average = (a + b)/2
    averages.append(average)


fig, ax = plt.subplots() #plot output
ax.plot(days,averages)

ax.set(xlabel = 'Day of the Last Year', ylabel = 'Average Altitude', 
       title = 'Average Altitude of the ISS')

plt.show()
