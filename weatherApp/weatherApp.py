import requests
from dotenv import load_dotenv
#load_dotenv()  # take environment variables from .env.
# By default, load_dotenv doesn't override existing environment variables.
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
Domain =  "http://api.openweathermap.org"


def get_lat_lon_by_city(CITY,STATE_CODE,COUNTRY):
    limit = '1'
    Lat_Lon_EndPoint = "/geo/1.0/direct" 
    r = requests.get(Domain+Lat_Lon_EndPoint+"?q="+CITY+","+STATE_CODE+","+COUNTRY+"&limit="+limit+"&appid="+API_KEY)

    #Practice# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
    #Practice# r = requests.get(Domain+Lat_Lon_EndPoint+"?q="+CITY+","+STATE_CODE+","+COUNTRY+"&limit="+limit+"&appid="+API_KEY)
    response_json=r.json()
    print(response_json)
    dict = {CITY: (response_json[0].get('lat'),response_json[0].get('lon'))}
    return dict

def get_temp_by_lat_lon(CITY,LAT,LON):
    limit = '1'
    Temp_EndPoint = "/data/2.5/weather"

    # https://api.openweathermap.org/data/2.5/weather?lat=57&lon=-2.15&appid={API key}&units=metric
    r1 = requests.get(Domain+Temp_EndPoint+"?lat="+str(LAT)+"&lon="+str(LON)+"&appid="+API_KEY+"&units=metric")

    response_json=r1.json()
    main_info=response_json.get('main')
    print("Today's Weather in %s is %s"%(CITY,response_json.get('weather')[0].get('description')))
    print("It feels like %s Celsius in %s"%(main_info.get('feels_like'),CITY))
    print("The pressure and humidity in %s  is %s Pa, %s%%'"%(CITY,main_info.get('pressure'),main_info.get('humidity')))


# why we use main function below 
# It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module


# if __name__ == "__main__":
    
#     lat_lon_dict = get_lat_lon_by_city('Boston','MA','USA')
#     get_temp_by_lat_lon('Boston',lat_lon_dict.get('Boston')[0],lat_lon_dict.get('Boston')[1])
