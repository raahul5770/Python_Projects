import requests
api_key_bing = "Ar_Yyfil6qbwgcLt9Gtmt4hbXfBgN9aia4dt1KrJ-bFLulP87FswWBYjOxVWbICs"
api_key_here = "SK9uEWCmrCYpvIKqS9FIOsTe7b5Jrhb5AFf_fnQF5VM"

api_key = "66a9efaa32d04e8c967abb141f4b4977"
url_local = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address="

response_local_raw = requests.get(url_local)
response_local = response_local_raw.json()

#print(response_local)

longi = response_local['longitude']
lat = response_local['latitude']


type = 'EatDrink'
radius = 5000
bing_url = f'https://dev.virtualearth.net/REST/v1/LocalSearch/?type={type}&userCircularMapView=42.2546,-71.4564,5000&key={api_key_bing}'
response_bing_raw = requests.get(bing_url)
response_bing = response_bing_raw.json()

print(response_bing)

