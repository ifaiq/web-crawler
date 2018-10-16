
import urllib.request
import bs4 as bs
import requests
import time
import schedule
from datetime import datetime
from functools import partial

url = "http://linked-things-events.eu-gb.mybluemix.net/api/v1/events/bulk"


def get():

    uvdata = []
    names = []
    s = urllib.request.urlopen('https://www.wunderground.com/personal-weather-station/dashboard?ID=IKARACHI19#history').read()
    soup = bs.BeautifulSoup(s, 'lxml')

    for info in soup.find_all('span', {'class': 'wx-value'}):
    # print(info)
        names.append(info.text)

    print(names)
    info = soup.find_all('div', {"class": "row collapse"})
    for tag in info:
        tdTags = tag.find_all("div", {"class": "small-5 medium-6 columns"})
        for tag in tdTags:
            uvdata.append(tag.text)

    print(uvdata[5])

    T = float(names[0])
    FL = float(names[1])
    W = float(names[2])
    G = float(names[4])
    U = float(uvdata[5])
    D = float(names[5])
    H = float(names[6])
    P = float(names[9])
    S = float(names[10])


    Gust = {
    "deviceId": "WeatherWise_IKARACHI19_Gust",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "Gust_Status",
    "value": G
    }
    DewPoint = {
    "deviceId": "WeatherWise_IKARACHI19_DewPoint",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "DewPoint_Status",
    "value": D
    }
    Temperature = {
    "deviceId": "WeatherWise_IKARACHI19_Temperature",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "Temperature_Status",
    "value": T
    }
    WindSpeed = {
    "deviceId": "WeatherWise_IKARACHI19_WindSpeed",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "WindSpeed_Status",
    "value": W
    }
    UV = {
    "deviceId": "WeatherWise_IKARACHI19_UV",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "UV_Status",
    "value": U
    }
    SolarRadiation = {
    "deviceId": "WeatherWise_IKARACHI19_SolarRadiation",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "SolarRadiation_Status",
    "value": S
    }
    Humidity = {
    "deviceId": "WeatherWise_IKARACHI19_Humidity",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "Humidity_Status",
    "value": H
    }
    Pressure = {
    "deviceId": "WeatherWise_IKARACHI19_Pressure",
    "hubId": "WeatherWise_IKARACHI19",
    "type": "Pressure_Status",
    "value": P
    }
    packet = [Gust, DewPoint, Temperature, WindSpeed,
          UV, SolarRadiation, Humidity, Pressure]
    return packet      

def pack(p):
    r = requests.post(url, json=p)
    print(r)



while True:
    packet = get()
    pack(packet)
    time.sleep(300)
