#import library
import requests
#pip install win10toast
from win10toast import ToastNotifier 
import json
import time 
#Function Update
def update():
    #this is world's covid-19 information
    #World
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f'Cases: {data["cases"]} \nDeaths: {data["deaths"]} \nRecovered: {data["recovered"]}'
    #You can change your country by change API https://coronavirus-19-api.herokuapp.com/countries/{yourcountry}
    #VietNam
    r1=requests.get("https://coronavirus-19-api.herokuapp.com/countries/vietnam")
    data=r1.json()
    #2 type data !! Choose 1 or 2 
    #text1=f'Cases: {data["cases"]} \n \nDeaths: {data["deaths"]}  \nRecovered: {data["recovered"]}'
    text1=f'Today_Cases: {data["todayCases"]} \nToday_Deaths: {data["todayDeaths"]} \nRecovered: {data["recovered"]}'
    #Output
    while True:
        t=ToastNotifier()
        t.show_toast("Covid 19 Update ",text, duration=20)
        t.show_toast(("Covid 19 Update "+ "-" +  f'{data["country"]}'),text1, duration=20)
        #300 seconds later, there is an announcement. You can change time if you want
        time.sleep(300)
update()
