import requests

api_key_here = "SK9uEWCmrCYpvIKqS9FIOsTe7b5Jrhb5AFf_fnQF5VM"


#print(response_local)
def find_city():
    print("Enter City Name and State Initials (Boston,MA):")
    city_name = input()
    print("\n")
    url_city = f"https://geocode.search.hereapi.com/v1/geocode?q={city_name}&apikey={api_key_here}"
    response_city_raw = requests.get(url_city)
    response_city = response_city_raw.json()
    
    return (response_city)



def find_location():

    api_key = "66a9efaa32d04e8c967abb141f4b4977"
    url_local = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address="


    response_local_raw = requests.get(url_local)
    response_local = response_local_raw.json()

    return(response_local)

    


def find_fastfood():
    print("""What type of fastfood are you looking for? Please choose one of the following or choose ALL:
    ALL
    Vegetarian
    Vegan
    Pizza
    Burgers
    Noodles
    Ice Cream""")

    fastfood_category = input()
    if fastfood_category == "ALL":
        fastfood_code="0"
    elif fastfood_category == "Vegetarian":
        fastfood_code = "800-077"
    elif fastfood_category == "Vegan":
        fastfood_code = "800-076"
    elif fastfood_category == "Pizza":
        fastfood_code = "800-057"
    elif fastfood_category == "Burgers":
        fastfood_code = "800-067"
    elif fastfood_category == "Noodles":
        fastfood_code = "800-085"
    elif fastfood_category == "Ice Cream":
        fastfood_code = "800-063"
    else:
        print("Enter a valid input")
        find_fastfood()
    
    return fastfood_code
        
def find_restaurant():
    print("""What type of restaurant would you like? Please choose one of the following or choose ALL:
ALL
Vegetarian
Vegan
Breakfast
American
Mexican
Chinese
North Indian
South Indian
Japanese
Southeast Asian
Middle-Eastern
Sri Lankan
French
Spanish
Greek
Italian
German
Mediterranean
Russian
Sweedish
South American
African
Ethiopian
Irish 
Oceanic
Pizza
Noodles
Ice Cream
""")
    restaurant_category = input()
    print("\n")
    if restaurant_category == "ALL":
        restaurant_code = "0"
    elif restaurant_category == "Vegetarian":
        restaurant_code = "800-077"
    elif restaurant_category == "Vegan":
        restaurant_code = "800-076"
    elif restaurant_category == "Breakfast":
        restaurant_code = "800-061"
    elif restaurant_category == "American":
        restaurant_code = "101-000"
    elif restaurant_category == "Mexican":
        restaurant_code = "102-000"
    elif restaurant_category == "Chinese":
        restaurant_code = "201-000"
    elif restaurant_category == "North Indian":
        restaurant_code = "202-023"
    elif restaurant_category == "South Indian":
        restaurant_code = "202-021"
    elif restaurant_category == "Japanese":
        restaurant_code = "203-000"
    elif restaurant_category == "Southeast Asian":
        restaurant_code = "204-000"
    elif restaurant_category == "Middle-Eastern":
        restaurant_code = "205-000"
    elif restaurant_category == "Sri Lankan":
        restaurant_code = "258-000"
    elif restaurant_category == "French":
        restaurant_code = "301-000"
    elif restaurant_category == "Spanish":
        restaurant_code = "311-000"
    elif restaurant_category == "Greek":
        restaurant_code = "303-000"
    elif restaurant_category == "Italian":
        restaurant_code = "304-000"
    elif restaurant_category == "Irish":
        restaurant_code = "305-000"
    elif restaurant_category == "Sweedish":
        restaurant_code = "352-000"
    elif restaurant_category == "German":
        restaurant_code = "302-000"
    elif restaurant_category == "Mediterranean":
        restaurant_code = "372-000"
    elif restaurant_category == "Russian":
        restaurant_code = "377-000"
    elif restaurant_category == "South American":
        restaurant_code = "400-000"
    elif restaurant_category == "African":
        restaurant_code = "500-000"
    elif restaurant_category == "Ethiopian":
        restaurant_code = "503-000"
    elif restaurant_category == "Oceanic":
        restaurant_code = "600-000"
    elif restaurant_category == "Pizza":
        restaurant_code = "800-057"
    elif restaurant_category == "Noodles":
        restaurant_code = "800-085"
    elif restaurant_category == "Ice Cream":
        restaurant_code = "800-063"
    else:
        print("Enter a valid input")
        find_restaurant()

    return restaurant_code 




def find_category():
    
    print(""""What would you like to search? Please choose one of the following:
Restaurants
Coffee Tea
Fast Food
Movie Theaters
Sights and Museums
Religious Places
Nature Sights
Public Transport
Airports
Rest Areas
Accommodations
Amusement Parks
Natural Parks
Department Stores
Malls
Pharmacies
Food Shops/Bakeries
Grocery
Electronics
Home/Hardware
Clothing Shops
Consumer Goods
Barber
ATM
Banks
Consumer Services
Post Office
Gas Stations
EV Charging Stations
Car Dealers
Car Repair
Car Rentals
Hospitals
Schools
Libraries
Parking
Restrooms
Covid-19 Testing
""")
    user_category= input()
    print('\n')
    foodType = "0"

    if user_category == "Restaurants":
        foodType = find_restaurant()
        category = "100-1000-0000"
    elif user_category == "Coffee Tea":
        category = "100-1100-0000"
    elif user_category == "Fast Food":
        foodType = find_restaurant()
        category = "100-1000-0009"
    elif user_category == "Movie Theaters":
        category = "200-2100-0019"
    elif user_category == "Sights and Museums":
        category = "300-0000-0000"
    elif user_category == "Religious Places":
        category = "300-3200-0000"
    elif user_category == "Nature Sights":
        category = "350-0000-0000"
    elif user_category == "Public Transport":
        category = "400-4100-0000"
    elif user_category == "Airports":
        category = "400-4000-4581"
    elif user_category == "Rest Areas":
        category = "400-4300-0000"
    elif user_category == "Accommodations":
        category = "500-0000-0000"
    elif user_category == "Amusement Parks":
        category = "500-5520-0000"
    elif user_category == "Natural Parks":
        category = "500-5510-0000"
    elif user_category == "Department Stores":
        category = '600-6200-0000'
    elif user_category == "Malls":
        category = "600-6100-0000"
    elif user_category == "Pharmacies":
        category = "600-6400-0000"
    elif user_category == "Food Shops/Bakeries":
        category = "600-6300-0000"
    elif user_category == "Grocery":
        category = "600-6300-0066"
    elif user_category == "Electronics":
        category = "600-6500-0000"
    elif user_category == "Home/Hardware":
        category = "600-6600-0000"
    elif user_category == "Clothing Shops":
        category = "600-6800-0000"
    elif user_category == "Consumer Goods":
        category = "600-6900-0000"
    elif user_category == "Barber":
        category = "600-6950-0399"
    elif user_category == "ATM":
        category = "700-7010-0000"
    elif user_category == "Banks":
        category = "700-7000-0000"
    elif user_category == "Consumer Services":
        category = "700-7400-0000"
    elif user_category == "Post Office":
        category = "700-7450-0000"
    elif user_category == "Gas Stations":
        category = "700-7600-0116"
    elif user_category == "EV Charging Stations":
        category = "700-7600-0322"
    elif user_category == "Car Dealers":
        category = "700-7850-0000"
    elif user_category == "Car Repair":
        category = "700-7850-0000"
    elif user_category == "Car Rentals":
        category = "700-7851-0000"
    elif user_category == "Hospitals":
        category = "800-8000-0000"
    elif user_category == "Schools":
        category = "800-8250-0000"
    elif user_category == "Libraries":
        category = "800-8300-0000"
    elif user_category == "Parking":
        category = "800-8500-0000"
    elif user_category == "Restrooms":
        category = "800-8700-0198"
    elif user_category == "Covid-19 Testing":
        category = "800-8000-0400"
    else:
        print("Enter a valid input")
        find_category()
    
    return [category, foodType]

def find_parameters():
    #print("What is the radius of the circle of area you would like to search in?")
    #radius = input()
    print("How many results would you like?")
    limit = input()
    print("\n")

    #return [radius, limit]
    return (limit)

        

def url_function():   
    print("""Would you like us to use your location or would you like to enter a city name? 
Enter 'Use Location' or 'Enter City'""")
    user_location = input()
    print('\n')
    if user_location == "Use Location":
        is_city = False
        location = find_location()
        longitude = location['longitude']
        latitude = location['latitude']
        category_type = find_category()
        url_category = category_type[0]
        url_foodType = category_type[1]
        #rad = find_parameters()[0]
        lim=find_parameters()
        if url_foodType == "0":
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&apikey={api_key_here}"
            #print(url_here)
        else:
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&foodTypes={url_foodType}&apikey={api_key_here}"
    elif user_location == "Enter City":
        is_city = True
        location = find_city()
        longitude = location['items'][0]['position']['lng']
        latitude = location['items'][0]['position']['lat']#might be list
        category_type = find_category()
        url_category = category_type[0]
        url_foodType = category_type[1]
        #rad = find_parameters()[0]
        lim = find_parameters()
        if url_foodType == "0":
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&apikey={api_key_here}"
        else:
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&foodTypes={url_foodType}&apikey={api_key_here}"
    else:
        print("Enter a valid input")
        url_function()

    return [url_here, is_city]



#url_here = f"https://discover.search.hereapi.com/v1/discover?in=circle:{latitude},{longitude};r={rad}&q={type}&limit={lim}&apikey={api_key_here}"



def print_function():
    url_function_response = url_function()
    response_here_raw = requests.get(url_function_response[0])
    response_here = response_here_raw.json()
    
    for i in response_here['items']:
        if 'title' in i:
            print("Name: " + i['title'])
        else:
            print("Name: Unknown Title")
        if 'categories' in i:
            if 'name' in i['categories'][0]:
                print("Category: " + i['categories'][0]['name'])
            else:
                print("Catergory: Not Known")
        else:
            print("Category: Not Known")
            
        if 'distance' in i and url_function_response[1] == False:
            print("Distance From You: " + str(i['distance']) + " meters")
        else: 
            print("Distance From You: Unkwown")
            
        if 'openingHours' in i:
            if 'isOpen' in i['openingHours'][0]:
                if i['openingHours'][0]['isOpen'] == True:
                    print("Status: Open Now")
                if i['openingHours'][0]['isOpen'] == False:
                    print('Status: Closed')
            else:
                print("Status: Unknown if Open Now")
            if 'text' in i['openingHours'][0]:
                print("Opening Hours: ", end="")
                print(*i['openingHours'][0]['text'])  
            else: 
                print("Opening Hours: Not Found")
        else: 
            print("Opening Hours: Not Found")
        
        if 'address' in i:
            if 'label' in i['address']:
                print("Address: "+i['address']['label'])
            else:
                print("Address: Not Found")
        else:
            print("Address: Not Found")
            
        if 'contacts' in i:
            if 'phone' in i['contacts'][0]:
                print("Phone: "+i['contacts'][0]['phone'][0]['value'])
            else:
                print("Phone Number Not Found")
        
            if 'www' in i['contacts'][0]:
                print("Website: "+i['contacts'][0]['www'][0]['value'])
            else:
                print("Website: Not Found")
        
            if 'email' in i['contacts'][0]:
                print("Email: " + i['contacts'][0]['email'][0]['value'])
            else:  
                print("Email Not Found")
        else: 
            print("No Contact Information Available")
            
        print("\n")


print_function()