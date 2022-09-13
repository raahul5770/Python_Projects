import requests

api_key_weather = "ae875eee94f93e5b3f21991c0171b382"



def find_city_weather():
    print("Enter City")
    city_name = input()
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key_weather}"
    return url_weather

def find_local_weather():
    api_key = "66a9efaa32d04e8c967abb141f4b4977"

    url_local = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address="

    response_local_raw = requests.get(url_local)
    response_local = response_local_raw.json()

    longi = response_local['longitude']
    lat = response_local['latitude']
    
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={longi}&units=imperial&appid={api_key_weather}"
    return url_weather

def print_weather(url):

    response_raw = requests.get(url)
    response = response_raw.json() 

    temp = response['main']['temp']
    forecast = response['weather'][0]['description']
    high = response['main']['temp_max']
    low = response['main']['temp_min']
    wind_speed = response['wind']['speed']
    city = response['name']
    country = response['sys']['country']

    final_output =  f"""

City/Town: {city}
Country: {country}
Forecast: {forecast}
Current Temp: {temp} F
High: {high} F
Low: {low} F
Wind Speed: {wind_speed}

    """
    print(final_output)

def find_weather():
    print("Would you like us to use your current location? (Yes/No)")
    user_input = input()
   
    if user_input == "Yes":
        url_local = find_local_weather()
        print_weather(url_local)
    elif user_input == "No":
        url_city = find_city_weather()
        print_weather(url_city)
    else:
        print("Please enter in a valid input")
        find_weather()

find_weather()




    



