import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
Domain =  "http://api.openweathermap.org"


def get_lat_lon_by_city(CITY,STATE_CODE,COUNTRY):
    limit = '1'
    Lat_Lon_EndPoint = "/geo/1.0/direct"
    r = requests.get(Domain+Lat_Lon_EndPoint+"?q="+CITY+","+STATE_CODE+","+COUNTRY+"&limit="+limit+"&appid="+API_KEY)
    response_json=r.json()
    dict = {CITY: (response_json[0].get('lat'),response_json[0].get('lon'))}
    return dict

def get_temp_by_lat_lon(LAT,LON):
    limit = '1'
    Temp_EndPoint = "/data/3.0/timemachine"
    r1 = requests.get(Domain+Temp_EndPoint+"?lat="+str(LAT)+"&lon="+str(LON)+"&dt=1643803200&appid="+API_KEY)
    response_json=r1.json()
    print(response_json)


if __name__ == "__main__":
    lat_lon_dict = get_lat_lon_by_city('Boston','MA','USA')
    get_temp_by_lat_lon(lat_lon_dict.get('Boston')[0],lat_lon_dict.get('Boston')[1])