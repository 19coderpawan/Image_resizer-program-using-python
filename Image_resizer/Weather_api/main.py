# This project is a weather application a very smaller version of it in which i am going to learn how to
# handle http request in python.

# so handle the http request we have a python library called requests.

'''
The Requests library in Python is one of the integral parts of Python for making HTTP requests to a specified
URL. Whether it be REST APIs or Web Scraping, requests are a must to be learned for proceeding further
with these technologies. When one makes a request to a URI, it returns a response.
Python requests provide inbuilt functionalities for managing both the request and response.
'''

import requests
import json #Python has a built-in package called json, which can be used to work with JSON data.
import win32com.client
cityname=input("enter the name of the city-:")
url="https://api.openweathermap.org/data/2.5/weather?q=delhi&appid=c5ebeb791c1dc96d86814f729a340dbf"

result=requests.get(url)  #used to get the response from the url
# print(result.text) #this data is in the string fromat i can convert it into the dict fromat also using json library.
dict=json.loads(result.text)#convert the string json into dict form.
temp=dict["main"]["temp"]
# print(dict["main"]["temp"])# just pass the key to access the value here the temp value is in the nested keys.
speak=win32com.client.Dispatch("SAPI.SpVoice")
speak.Speak(f"the temperature of city {cityname} is {temp} degree celsius")