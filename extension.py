import json
import requests
import turtle

url = "https://api.wheretheiss.at/v1/satellites/25544" #api used for ISS data

#get latitude and longitude of ISS at current epoch timestamp
response = requests.get(url)
json_payload = response.json()
latitude = float(json_payload["latitude"]) #turtles requires a float
longitude = float(json_payload['longitude'])
timestamp = (json_payload['timestamp'])

#Print results
print('ISS Current Location and Epoch Time')
print(longitude)
print(latitude)
print(timestamp)


#open turtle screen, set size and world coordinates
turtles = turtle.Screen()
turtles.setup(720,360)
turtles.setworldcoordinates(-180,-90,180,90) #world max long and lat
turtles.bgpic("NASAmap.gif") #background picture from NASA
iss = turtle.Turtle(shape='turtle') #set turtle to represent ISS
iss.color('green') #colour
iss.penup()
iss.goto(longitude,latitude) #turtle goes to ISS lat and long
turtle.mainloop()


