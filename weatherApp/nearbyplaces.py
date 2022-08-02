import requests 

api_key = "66a9efaa32d04e8c967abb141f4b4977"
url_local = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address="

response_local_raw = requests.get(url_local)
response_local = response_local_raw.json()

longi = response_local['longitude']
lat = response_local['latitude']

api_key_tom = "UUXskQZLuA3GeEGqhrnIRZ6WnElSdSqG"
tomtom_url = "api.tomtom.com"
version_num = 2
ext = "json"
openingHours= 'nextSevenDays'
categoryset=7315025,7315017
rad = 50000
limit = 100
url_places = f"https://{tomtom_url}/search/{version_num}/nearbySearch/.{ext}?key={api_key_tom}&lat={lat}&lon={longi}&radius={rad}&limit={limit}&categoryset={categoryset}"

response_tom_raw = requests.get(url_places)
response_tom = response_tom_raw.json()

#print(response_tom)


for i in response_tom['results']:
    
    try: 
        print(i['poi']['name'])
    except:
        print('Unknown Name')
    try:
        print(i['poi']['phone'])
    except:
        print('Unknown Phone Number')    
    try:
        print(i['poi']['url'])
    except:
        print('No Website URL Found')
    try:
        print(i['poi']['classifications'][0]['code'])
    except:
        print('Unkown Type')
    try:
        print(i['address']['freeformAddress'] + "\n")
        print("")
    except:
        print('Unknown Address')
        print("")



    

