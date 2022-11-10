#asks user location, time, and date and outputs a "safety score"

import json
import placekey as pk
from placekey.api import PlacekeyAPI
placekey_api_key = "U2zPisU64vsj6GOI2CgFhqE7pbCDj12B"

pk_api = PlacekeyAPI(placekey_api_key)
lat = float(input("Enter a latitude: "))
lon = float(input("Enter a longitude: "))

user_location = pk_api.lookup_placekey(latitude=lat, longitude=lon)['placekey']

south_quad_placekey = '@5pv-wr5-dy9'
main_quad_placekey = '@5pv-wr5-gtv'
ike_placekey = '@5pv-wr5-r6k'
grainger_placekey = '@5pt-y8c-pqf'
campustown_placekey = '@5pt-y8c-nkf'
isr_placekey = '@5pt-y8c-92k'
bromley_placekey = '@5pv-wr5-tqf'
lar_placekey = "@5pv-wr5-mp9"
par_placekey = "@5pv-wr7-9vf"

#calculates distance between user and locations
main_quad_distance = pk.placekey_distance(user_location, main_quad_placekey)
south_quad_distance = pk.placekey_distance(user_location, south_quad_placekey)
ike_distance  = pk.placekey_distance(user_location, ike_placekey)
grainger_distance  = pk.placekey_distance(user_location, grainger_placekey)
campustown_distance = pk.placekey_distance(user_location, campustown_placekey)
isr_distance = pk.placekey_distance(user_location, isr_placekey)
bromley_distance = pk.placekey_distance(user_location, bromley_placekey)
lar_distance = pk.placekey_distance(user_location, lar_placekey)
par_distance = pk.placekey_distance(user_location, par_placekey)

distances = {
    "Main Quad" : main_quad_distance,
    "South Quad" : south_quad_distance,
    "Ike" : ike_distance,
    "Grainger" : grainger_distance,
    "Campustown" : campustown_distance,
    "ISR" : isr_distance,
    "Bromley" : bromley_distance,
    "LAR" : lar_distance,
    "PAR" : par_distance
}

lowest_distance = min(distances, key = distances.get);

# MAIN QUAD
if lowest_distance == "Main Quad":
    with open('mainquad.json', 'r') as myfile:
        data=myfile.read()
# SOUTH QUAD
elif lowest_distance == "South Quad":
    with open('southquad.json', 'r') as myfile:
        data=myfile.read()
#IKE
elif lowest_distance == "Ike":
    with open('ike.json', 'r') as myfile:
        data=myfile.read()
#GRAINGER
elif lowest_distance == "Grainger":
    with open('grainger.json', 'r') as myfile:
        data=myfile.read()
#Campustown
elif lowest_distance == "Campustown":
    with open('campustown.json', 'r') as myfile:
        data=myfile.read()
#ISR
elif lowest_distance == "ISR":
    with open('isr.json', 'r') as myfile:
        data=myfile.read()
#Bromley
elif lowest_distance == "Bromley":
    with open('bromley.json', 'r') as myfile:
        data=myfile.read()
#LAR
elif lowest_distance == "LAR":
    with open('lar.json', 'r') as myfile:
        data=myfile.read()
#PAR
elif lowest_distance == "PAR":
    with open('par.json', 'r') as myfile:
        data=myfile.read()
else:
    print("Error")
# parse file
obj = json.loads(data)

#ask user what day and time
date = int(input("Enter the day: "))
time = int(input("Enter the time: "))
# show values
print("Foot traffic: " + str(obj['analysis'][date]['hour_analysis'][time]['intensity_txt']))