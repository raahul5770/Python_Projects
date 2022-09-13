      if(len(response_here['items'])) == 0:
                print("No Places Found Nearby, Please Try a Different Search")
            else:
                for i in response_here['items']: 

                    if 'title' in i:
                        name = "Name: " + i['title']
                    else:
                        name = "Name: Unknown Title"
                    if 'categories' in i:
                        if 'name' in i['categories'][0]:
                            category = "Category: " + i['categories'][0]['name']
                        else:
                            category = "Catergory: Not Known"
                    else:
                        category = "Category: Not Known"

                    if url_function_response[2] == True:
                        if 'foodTypes' in i:
                            if 'name' in i['foodTypes'][0]:
                                food_name = "Food Type: " + i['foodTypes'][0]['name']
                            else:
                                food_name = "Food Type: Unknown1"
                        else:
                            food_name = "Food Type: Unknown"
                        
                    if 'distance' in i and url_function_response[1] == False:
                        distance = "Distance From You: " + str(i['distance']) + " meters"
                    else: 
                        distance = "Distance From You: Unkwown"
                        
                    if 'openingHours' in i:
                        if 'isOpen' in i['openingHours'][0]:
                            if i['openingHours'][0]['isOpen'] == True:
                                openstatus = "Status: Open Now"
                            if i['openingHours'][0]['isOpen'] == False:
                                openstatus = 'Status: Closed'
                        else:
                            openstatus = "Status: Unknown if Open Now"
                        if 'text' in i['openingHours'][0]:
                            openhours = "Opening Hours: " + str(i['openingHours'][0]['text'])
                        else: 
                            openhours = "Opening Hours: Not Found"
                    else: 
                        openhours = "Opening Hours: Not Found"
                    
                    if 'address' in i:
                        if 'label' in i['address']:
                            address = "Address: "+i['address']['label']
                        else:
                            address = "Address: Not Found"
                    else:
                        address = "Address: Not Found"
                        
                    if 'contacts' in i:
                        if 'phone' in i['contacts'][0]:
                            phone = "Phone: "+i['contacts'][0]['phone'][0]['value']
                        else:
                            phone = "Phone Number Not Found"
                    
                        if 'www' in i['contacts'][0]:
                            website = "Website: "+i['contacts'][0]['www'][0]['value']
                        else:
                            website = "Website: Not Found"
                    
                        if 'email' in i['contacts'][0]:
                            email = "Email: " + i['contacts'][0]['email'][0]['value']
                        else:  
                            email = "Email Not Found"
                    else: 
                        phone = "Phone Number Not Found"
                        website = "Website: Not Found"
                        email = "Email Not Found"


        {%if 'items' in hresponse_here%}
            {% counter = 0 %}
            {% for i in hresponse_here['items']%}
                {% counter = counter + 1%}
                {%if 'title' in i%}
                    <p class="results">Name: {{i['title']}}</p>
                {%else%}
                    <p class="results">Name: Unknown Title</p>
                {%endif%}


                {%if 'categories' in i%}
                    {%if 'name' in i['categories'][0]%}
                        <p class="results">Category: {{i['categories'][0]['name']}}</p>
                    {%else%}
                        <p class="results">Category: Not Known</p>
                    {%endif%}
                {%else%}
                    <p class="results">Category: Not Known</p>
                {%endif%}


                {%if hurl_function_response[2] == True%}
                    {%if 'foodTypes' in i%}
                        {%if 'name' in i['foodTypes'][0]%}
                            <p class="results">Food Type: {{i['foodTypes'][0]['name']}}</p>
                        {%else%}
                            <p class="results">Food Type: Unknown 1</p>
                        {%endif%}
                    {%else%}
                        <p class="results">Food Type: Unknown</p>
                    {%endif%}
                {%endif%}


                {%if 'distance' in i and hurl_function_response[1] == False%}
                    <p class="results">Distance From You: {{(i['distance'])}} Meters</p>
                {%else%}
                    <p class="results">Distance From You: Unknown</p>
                {%endif%}


                {%if 'openingHours' in i%}
                    {%if 'isOpen' in i['openingHours'][0]%}
                        {%if i['openingHours'][0]['isOpen'] == True%}
                            <p class="results">Status: Open Now</p>
                        {%endif%}

                        {%if i['openingHours'][0]['isOpen'] == False%}
                            <p class="results">Status: Closed</p>
                        {%endif%}

                    {%else%}
                        <p class="results">Status: Unknown if Open Now</p>
                    {%endif%}
                    {%if 'text' in i['openingHours'][0]%}
                        <p class="results">Opening Hours: {{i['openingHours'][0]['text']}}</p>
                    {%else%}
                        <p class="results">Opening Hours: Not Found</p>
                    {%endif%}
                {%else%}
                    <p class="results">Opening Hours: Not Found</p>
                {%endif%}


                {%if 'address' in i%}
                    {%if 'label' in i['address']%}
                        <p class="results">Address: {{i['address']['label']}}</p>
                    {%else%}
                        <p class="results">Address: Not Found</p>
                    {%endif%}
                {%else%}
                    <p class="results">Address: Not Found</p>
                {%endif%}


                {%if 'contacts' in i%}
                    {%if 'phone' in i['contacts'][0]%}
                        <p class="results">Phone: {{i['contacts'][0]['phone']['value']}}</p>
                    {%else%}
                        <p class="results">Phone Number Not Found</p>
                    {%endif%}

                    {%if 'www' in i['contacts'][0]%}
                        <p class="results">Website: {{i['contacts'][0]['www']['value']}}</p>
                    {%else%}
                        <p class="results">Website: Not Found</p>
                    {%endif%}

                    {%if 'email' in i['contacts'][0]%}
                        <p class="results">Email: {{i['contacts'][0]['email']['value']}}</p>
                    {%else%}
                        <p class="results">Email Not Found</p>
                    {%endif%}

                {%else%}
                    <p class="results">No Contact Information Available</p>
                {%endif%}

                <br>


            {%endfor%}
        {%endif%}