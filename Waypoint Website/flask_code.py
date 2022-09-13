from pdb import post_mortem
from flask import Flask, render_template, request, session, redirect
from datetime import timedelta
import requests
import sys 


def get_data(city_name, fastfood_category, restaurant_category, user_category, limit, location_option, limit_option):

    global response_here
    global url_function_response  

    api_key_here = "SK9uEWCmrCYpvIKqS9FIOsTe7b5Jrhb5AFf_fnQF5VM"

    #print(response_local)
    
    def find_city():

        
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

        global fastfood_code
        

        fastfood_dict = {"Search All":'0',"Vegetarian":'800-077',"Vegan":'800-076',"Pizza":'800-057',"Burgers":'800-067',"Noodles":'800-085',"Ice Cream":'800-063',}

        fastfood_code = fastfood_dict[fastfood_category]

        return fastfood_code
        
    
            
    def find_restaurant():
       
        global restaurant_code
        
        
        restaurant_dict = { 'Search All': '0', "Vegetarian":"800-077","Vegan":"800-076","Breakfast":'800-061','American':'101-000', "Mexican":'102-000',"Chinese":'201-000','Indian':'202-000','North Indian':'202-023','South Indian':'202-021',
    "Japanese":'203-000',"Southeast Asian":'204-000','Middle-Eastern':'250-000',"Sri Lankan":'258-000',"Thai":"205-000","French":"301-000","Spanish":'311-000',"Greek":'303-000','Italian':'304-000','German':'302-000',"Mediterranean":'372-000',"Russian":'377-000',
    "Sweedish":'352-000',"South American":'400-000',"African":'500-000',"Ethiopian":'503-000',"Irish":'305-000',"Oceanic":'600-000','Pizza':'800-057',"Noodles":'800-085',"Ice Cream":'800-063'}

        restaurant_code = restaurant_dict[restaurant_category]

        return restaurant_code
        
       
    def find_category():
        
        
        
        
    
        global foodType
        foodType = "0"
        category_dict = {"Restaurants":"100-1000-0000","Coffee Tea":"100-1100-0000","Fast Food":"100-1000-0009","Movie Theaters":"200-2100-0019","Sights and Museums":"300-3000-0000,300-3100-0000","Religious Places":"300-3200",
    "Nature Sights":"350","Public Transport":"400-4100-0035,400-4100-0039,400-4100-0038,400-4100-0036,400-4100-0037,400-4100-0040", "Transportation Services": "400-4100-0041", "Airports":"400-4000-4581","Rest Areas":"400-4300",
    "Accommodations":"500","Land Activities/Theme Parks":"550-5520-0207","Fun Attractions": "550-5520-0208,550-5520-0211,550-5520-0212,550-5520-0357","Natural Parks":"550-5510","Department Stores":'600-6200',"Malls":"600-6100","Pharmacies":"600-6400","Food Shops/Bakeries":"600-6300-0064,600-6300-0067,600-6300-0244,600-6300-0245,600-6300-0246,600-6300-0363,600-6300-0364","Grocery":"600-6300-0066",
    "Electronics":"600-6500","Home/Hardware":"600-6600","Clothing Shops":"600-6800","Consumer Goods":"600-6900","Barber":"600-6950-0399","ATM":"700-7010","Banks":"700-7000","Consumer Services":"700-7400","Post Office":"700-7450",
    "Gas Stations":"700-7600-0116","EV Charging Stations":"700-7600-0322","Car Dealers":"700-7800-0118,700-7800-0120","Car Repair":"700-7850","Car Rentals":"700-7851","Healthcare":"800-8000-0000","Schools":"800-8250","Libraries":"800-8300","Parking":"800-8500",
    "Public Outdoor Restrooms":"800-8700-0198","Covid-19 Testing":"800-8000-0400"}

        global category_code 

        if user_category == "Restaurants":
            category_code = category_dict[user_category]
            foodType = find_restaurant()
        
        elif user_category == "Fast Food":
            category_code = category_dict[user_category]
            foodType = find_fastfood()
            
        else:
            category_code = category_dict[user_category]
            
        return [category_code, foodType]
        
    
    def find_parameters():
        #print("What is the radius of the circle of area you would like to search in?")
        #radius = input()

        

                
        return limit

            
    
    def url_function(): 

        if request.method == "POST":
            

            
            #output = request.form.to_dict()
            #print(output)
            #location_option = output["location_option"]
    
            print(location_option)
            print(limit_option)
            global url_here
            global is_city
            global is_food

            if location_option == "use_location":
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
            elif location_option == "use_city":
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
                    is_food = False
                    url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&apikey={api_key_here}"
                     
                else:
                    is_food = True
                    url_here = f"https://browse.search.hereapi.com/v1/browse?at={latitude},{longitude}&limit={lim}&categories={url_category}&foodTypes={url_foodType}&apikey={api_key_here}"
                   
            else:
                print("Enter a valid input")
                url_here = ""
                is_city = ""
                is_food = ""

        
        print(url_here)   
        
        return [url_here, is_city, is_food]


    #url_here = f"https://discover.search.hereapi.com/v1/discover?in=circle:{latitude},{longitude};r={rad}&q={type}&limit={lim}&apikey={api_key_here}"
    #print(response_here)
     
    
    url_function_response = url_function()
        
    response_here_raw = requests.get(url_function_response[0]) 
        
    response_here = response_here_raw.json()

    
        


        

    
 
def get_weather_data(longi_arg, lat_arg):

    api_key_weather = "ae875eee94f93e5b3f21991c0171b382"

    longi = longi_arg
    lat = lat_arg
    
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={longi}&units=imperial&appid={api_key_weather}"

    response_weather_raw = requests.get(url_weather)
    response_weather = response_weather_raw.json()

    return response_weather



app = Flask(__name__)
app.secret_key = "21010"
app.permanent_session_lifetime = timedelta(minutes = 3)


global name 
global category 
global food_name
global distance
global openstatus
global openhours
global address
global phone
global website
global email
global url_valid

global response_here
global url_function_response 


response_here = {'hi':'yoooo'}
url_function_response = []

def call_fn_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/location', methods=["POST", "GET"])
def get_inputs():
    name = "hiiii"
    category = ""
    food_name = ""
    distance = ""
    openstatus = ""
    openhours = ""
    address = ""
    phone = ""
    website = ""
    email = ""
    url_valid = ""

    city_name = request.form.get('city_button')
    session['city_name'] = city_name

    fastfood_category = request.form.get('fastfood_button')
    session['fastfood_category'] = fastfood_category

    restaurant_category = request.form.get('restaurant_button')
    session['restaurant_category'] = restaurant_category
    
    user_category= request.form.get("category_button") 
    session['user_category'] = user_category
    
    limit = request.form.get('limit_button')
    session['limit'] = limit

    location_option = request.form.get('location_option')
    session['location_option'] = location_option

    limit_option = request.form.get('limit_button')
    session['limit_option'] = limit_option

   
    return render_template("location.html")
                 
     

@app.route("/about")
def about():
    return render_template("about.html")


print(response_here)

@app.route("/results", methods=['POST', 'GET'])
def results():

    global city_name
    global fastfood_category
    global restaurant_category
    global user_category
    global limit
    global location_option
    global limit_option

    if "city_name" in session:
        city_name = session['city_name'] 
        
    if "fastfood_category" in session:
        fastfood_category = session['fastfood_category'] 

    if "restaurant_category" in session:
        restaurant_category = session['restaurant_category'] 

    if "user_category" in session:
        user_category = session['user_category'] 
        print(user_category)

    if "limit" in session:
        limit = session['limit'] 

    if "location_option" in session:
        location_option = session['location_option'] 

    if "limit_option" in session:
        limit_option = session['limit_option'] 


    if request.method == "POST":
        if request.form['submit_button'] == "Search Now":

            city_name = request.form.get('city_button')
            session['city_name'] = city_name

            fastfood_category = request.form.get('fastfood_button')
            session['fastfood_category'] = fastfood_category

            restaurant_category = request.form.get('restaurant_button')
            session['restaurant_category'] = restaurant_category
    
            user_category= request.form.get("category_button") 
            session['user_category'] = user_category
    
            limit = request.form.get('limit_button')
            session['limit'] = limit

            location_option = request.form.get('location_option')
            session['location_option'] = location_option

            limit_option = request.form.get('limit_button')
            session['limit_option'] = limit_option

            try:   
                get_data(city_name, fastfood_category, restaurant_category, user_category, limit, location_option, limit_option)
            except:
                return redirect("./error", code=302)

    return render_template("results.html", hresponse_here=response_here, hurl_function_response=url_function_response)

@app.route("/moreinfo", methods=['POST', 'GET'])
def moreinfo():

    if "city_name" in session:
        city_name = session['city_name'] 
        

    if "fastfood_category" in session:
        fastfood_category = session['fastfood_category'] 

    if "restaurant_category" in session:
        restaurant_category = session['restaurant_category'] 

    if "user_category" in session:
        user_category = session['user_category'] 
        print(user_category)

    if "limit" in session:
        limit = session['limit'] 

    if "location_option" in session:
        location_option = session['location_option'] 

    if "limit_option" in session:
        limit_option = session['limit_option'] 
    
    get_data(city_name, fastfood_category, restaurant_category, user_category, limit, location_option, limit_option)
  

    more_info_value = request.form['more_info_button']
    print(more_info_value)
    counter = 0
    counter_weather = 0

    global k

    response_weather = {}

    for k in response_here['items']:
        counter_weather += 1
        if (counter_weather == int(more_info_value)):
            longi = response_here['items'][0]['position']['lng']
            lat = response_here['items'][0]['position']['lat']
            response_weather = get_weather_data(longi, lat)

    return render_template("moreinfo.html", hresponse_here=response_here, hurl_function_response=url_function_response, hmore_info_value=more_info_value, hcounter = counter, hresponse_weather = response_weather)
    
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)

