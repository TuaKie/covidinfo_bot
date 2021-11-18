#import library
import requests
from win10toast import ToastNotifier
import json
import time 
#Function Update
def update():
    #World
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'Cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'
    #VietNam
    r1=requests.get("https://coronavirus-19-api.herokuapp.com/countries/vietnam")
    data=r1.json()
    text1=f'Country: {data["country"]}\nCases: {data["cases"]} \nToday_Cases: {data["todayCases"]} \nDeaths: {data["deaths"]} \nToday_Deaths: {data["todayDeaths"]} \nRecovered: {data["recovered"]}'
    #Output
    while True:
        t=ToastNotifier()
        t.show_toast("Covid 19 Update ",text, duration=20)
        t.show_toast("Covid 19 Update ",text1, duration=20)
        time.sleep(300)
update()
