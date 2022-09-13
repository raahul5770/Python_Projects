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
    global fastfood_code
    fastfood_category = input()
    print("\n")
    fastfood_dict = {"ALL":'0',"Vegetarian":'800-077',"Vegan":'800-076',"Pizza":'800-057',"Burgers":'800-067',"Noodles":'800-085',"Ice Cream":'800-063',}

    if fastfood_category in fastfood_dict:
        fastfood_code = fastfood_dict[fastfood_category]
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
Indian
North Indian
South Indian
Japanese
Southeast Asian
Middle-Eastern
Sri Lankan
Thai
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
    global restaurant_code
    restaurant_category = input()
    print("\n")
    restaurant_dict = { 'ALL': '0', "Vegetarian":"800-077","Vegan":"800-076","Breakfast":'800-061','American':'101-000', "Mexican":'102-000',"Chinese":'201-000','Indian':'202-000','North Indian':'202-023','South Indian':'202-021',
"Japanese":'203-000',"Southeast Asian":'204-000','Middle-Eastern':'250-000',"Sri Lankan":'258-000',"Thai":"205-000","French":"301-000","Spanish":'311-000',"Greek":'303-000','Italian':'304-000','German':'302-000',"Mediterranean":'372-000',"Russian":'377-000',
"Sweedish":'352-000',"South American":'400-000',"African":'500-000',"Ethiopian":'503-000',"Irish":'305-000',"Oceanic":'600-000','Pizza':'800-057',"Noodles":'800-085',"Ice Cream":'800-063'}

    if restaurant_category in restaurant_dict:
        restaurant_code = restaurant_dict[restaurant_category]
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
Transportation Services
Airports
Rest Areas
Accommodations
Land Activities/Theme Parks
Fun Attractions
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
Healthcare
Schools
Libraries
Parking
Public Outdoor Restrooms
Covid-19 Testing
""")
    user_category= input()
    print('\n')
    global foodType
    foodType = "0"
    category_dict = {"Restaurants":"100-1000-0000","Coffee Tea":"100-1100-0000","Fast Food":"100-1000-0009","Movie Theaters":"200-2100-0019","Sights and Museums":"300-3000-0000,300-3100-0000","Religious Places":"300-3200",
"Nature Sights":"350","Public Transport":"400-4100-0035,400-4100-0039,400-4100-0038,400-4100-0036,400-4100-0037,400-4100-0040", "Transportation Services": "400-4100-0041", "Airports":"400-4000-4581","Rest Areas":"400-4300",
"Accommodations":"500","Land Activities/Theme Parks":"550-5520-0207","Fun Attractions": "550-5520-0208,550-5520-0211,550-5520-0212,550-5520-0357","Natural Parks":"550-5510","Department Stores":'600-6200',"Malls":"600-6100","Pharmacies":"600-6400","Food Shops/Bakeries":"600-6300-0064,600-6300-0067,600-6300-0244,600-6300-0245,600-6300-0246,600-6300-0363,600-6300-0364","Grocery":"600-6300-0066",
"Electronics":"600-6500","Home/Hardware":"600-6600","Clothing Shops":"600-6800","Consumer Goods":"600-6900","Barber":"600-6950-0399","ATM":"700-7010","Banks":"700-7000","Consumer Services":"700-7400","Post Office":"700-7450",
"Gas Stations":"700-7600-0116","EV Charging Stations":"700-7600-0322","Car Dealers":"700-7800-0118,700-7800-0120","Car Repair":"700-7850","Car Rentals":"700-7851","Healthcare":"800-8000-0000","Schools":"800-8250","Libraries":"800-8300","Parking":"800-8500",
"Public Outdoor Restrooms":"800-8700-0198","Covid-19 Testing":"800-8000-0400"}

    global category_code 

    if user_category in category_dict and user_category == "Restaurants":
        category_code = category_dict[user_category]
        foodType = find_restaurant()
    
    elif user_category in category_dict and user_category == "Fast Food":
        category_code = category_dict[user_category]
        foodType = find_fastfood()
        
    elif user_category in category_dict:
        category_code = category_dict[user_category]
        
    else:  
        print("You are a Stupid BOZO + L + ratio")# Dont forget to change
        print("/n")
        find_category()
    return [category_code, foodType]
    

def find_parameters():
    #print("What is the radius of the circle of area you would like to search in?")
    #radius = input()

    global limit

    print("How many results would you like?")
    limit = input()
    if limit.isnumeric() == True:
        print("\n")
    else:
        print("\nPlease enter in a valid input\n")
        find_parameters()
            
    return limit

        

def url_function(): 

    global url_here
    global is_city
    global is_food

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
            is_food = False
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&apikey={api_key_here}"
            #print(url_here)
        else:
            is_food = True
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&foodTypes={url_foodType}&apikey={api_key_here}"
    elif user_location == "Enter City":
        is_city = True
        location = find_city()
        try:
            longitude = location['items'][0]['position']['lng']
        except:
            print("Please Enter Location again. (ex. Boston,MA)\n")
            print_function()
        latitude = location['items'][0]['position']['lat']#might be list
        category_type = find_category()
        url_category = category_type[0]
        url_foodType = category_type[1]
        #rad = find_parameters()[0]
        lim = find_parameters()
        if url_foodType == "0":
            is_food = False
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&apikey={api_key_here}"
        else:
            is_food = True
            url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&foodTypes={url_foodType}&apikey={api_key_here}"
    else:
        print("Enter a valid input")
        url_function()

    return [url_here, is_city, is_food]



#url_here = f"https://discover.search.hereapi.com/v1/discover?in=circle:{latitude},{longitude};r={rad}&q={type}&limit={lim}&apikey={api_key_here}"



def print_function():
    url_function_response = url_function()
    try:
        response_here_raw = requests.get(url_function_response[0])
    except:
        print("Error: Search could not be made. Please check if you put your inputs correctly")
        print_function()
   
    response_here = response_here_raw.json()

    #print(response_here)

    if(len(response_here['items'])) == 0:
        print("No Places Found Nearby, Please Try a Different Search")
    else:
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

            if url_function_response[2] == True:
                if 'foodTypes' in i:
                    if 'name' in i['foodTypes'][0]:
                        print("Food Type: " + i['foodTypes'][0]['name'])
                    else:
                        print("Food Type: Unknown1")
                else:
                    print("Food Type: Unknown")
                
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