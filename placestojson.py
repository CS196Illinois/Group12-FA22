import requests
import json

url = "https://besttime.app/api/v1/forecasts"

places = ["Main Quad", "South Quad", "Ike", "Grainger", "Campustown", "ISR", "Bromley", "LAR", "PAR"]

place_names = ["Main Quad", "South Quad", "Ikenberry Commons Residence Hall Library", "Grainger Engineering Library", "McDonalds", "Circle K", "Illini Inn", "Stanley Illini Grove", "University of Illinois Arboretum"]
place_addresses = ["Urbana, Illinois", "Urbana, Illinois", "Urbana, Illinois", "Urbana, Illinois", "616 E Green St, Champaign, IL 61820", "810 W Green St Urbana, IL 61801 United States", "901 S 4th St Champaign, IL 61820 United States", "Urbana, IL", "2001 S Lincoln Ave Urbana, IL"]

index = 0
for place in places:
    params = {
        'api_key_private': 'pri_5ef80528b986479c86f45e6cfa2b11f0',
        'venue_name': place_names[index],
        'venue_address': place_addresses[index]
    }
    #print(str(place) +" "+ str(place_names[index]) + " " + str(place_addresses[index]))
    response = requests.request("POST", url, params=params)
    if (place == "Main Quad"):
#         with open('mainquad.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded Main Quad to Json")
    elif (place == "South Quad"):
#         with open('southquad.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded South Quad to Json")
    elif (place == "Ike"):
#         with open('ike.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded IKE to Json")
    elif (place == "Grainger"):
#         with open('grainger.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded Grainger to Json")
    elif (place == "Campustown"):
#         with open('campustown.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded Campustown to Json")
    elif (place == "ISR"):
#         with open('isr.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded ISR to Json")
    elif (place == "Bromley"):
#         with open('bromley.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded Bromley to Json")
    elif (place == "LAR"):
#         with open('lar.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded LAR to Json")
    elif (place == "PAR"):
#         with open('par.json', 'w') as json_file:
#             json.dump(response.json(), json_file)
        print("Loaded PAR to Json")
    else:
        print("Error")
    index += 1

print("Done")