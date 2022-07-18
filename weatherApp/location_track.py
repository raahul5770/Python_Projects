import requests 

api_key = "66a9efaa32d04e8c967abb141f4b4977"
api_key_weather = "ae875eee94f93e5b3f21991c0171b382"
url_local = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address="

response_local_raw = requests.get(url_local)
response_local = response_local_raw.json()

#print(response_local)

longi = response_local['longitude']
lat = response_local['latitude']

url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={longi}&units=imperial&appid={api_key_weather}"

response_raw = requests.get(url_weather)
response = response_raw.json() 

temp = response['main']['temp']
forecast = response['weather'][0]['description']
high = response['main']['temp_max']
low = response['main']['temp_min']
wind_speed = response['wind']['speed']
city = response['name']
country = response['sys']['country']

final_output =  f"""
    
City: {city}
Country: {country}
Forecast: {forecast}
Current Temp: {temp} F
High: {high} F
Low: {low} F
Wind Speed: {wind_speed}

    """
print(final_output)