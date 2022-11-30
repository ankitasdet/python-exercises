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
print(get_lat_lon_by_city('Boston','MA','USA'))
