#given a time, outputs place has the lowest foot traffic

import json

with open('mainquad.json', 'r') as myfile:
        data1=myfile.read()
        
with open('southquad.json', 'r') as myfile:
        data2=myfile.read()

with open('ike.json', 'r') as myfile:
        data3=myfile.read()

with open('grainger.json', 'r') as myfile:
        data4=myfile.read()
        
with open('campustown.json', 'r') as myfile:
        data5=myfile.read()
        
with open('isr.json', 'r') as myfile:
        data6=myfile.read()

with open('bromley.json', 'r') as myfile:
        data7=myfile.read()

with open('lar.json', 'r') as myfile:
        data8=myfile.read()

with open('par.json', 'r') as myfile:
        data9=myfile.read()
        
mainquad = json.loads(data1)
southquad = json.loads(data2)
ike = json.loads(data3)
grainger = json.loads(data4)
campustown = json.loads(data5)
isr = json.loads(data6)
bromley = json.loads(data7)
lar = json.loads(data8)
par = json.loads(data9)

date = int(input("Enter the day: "))
time = int(input("Enter the time: "))

mainquad_traffic = mainquad['analysis'][date]['hour_analysis'][time]['intensity_txt']
southquad_traffic = southquad['analysis'][date]['hour_analysis'][time]['intensity_txt']
ike_traffic = ike['analysis'][date]['hour_analysis'][time]['intensity_txt']
grainger_traffic = grainger['analysis'][date]['hour_analysis'][time]['intensity_txt']
campustown_traffic = campustown['analysis'][date]['hour_analysis'][time]['intensity_txt']
isr_traffic = isr['analysis'][date]['hour_analysis'][time]['intensity_txt']
bromley_traffic = bromley['analysis'][date]['hour_analysis'][time]['intensity_txt']
lar_traffic = lar['analysis'][date]['hour_analysis'][time]['intensity_txt']
par_traffic = par['analysis'][date]['hour_analysis'][time]['intensity_txt']


foot_traffic = {"Main Quad" : mainquad_traffic,
                "South Quad" : southquad_traffic,
                "Ike" : ike_traffic,
                "Grainger" : grainger_traffic,
                "Campustown" : campustown_traffic,
                "ISR" : isr_traffic,
                "Bromley" : bromley_traffic,
                "LAR": lar_traffic,
                "PAR": par_traffic
                }
foot_traffic_values = {}
for place, traffic in foot_traffic.items():
    if traffic == "Low":
        traffic = 1
    elif traffic == "Below average":
        traffic = 2
    elif traffic == "Average":
        traffic = 3
    elif traffic == "Above Average":
        traffic = 4
    elif traffic == "Closed":
        traffic = 1
    else:
        traffic = 5
    foot_traffic_values[place] = traffic

greatest_foot_traffic = max(foot_traffic_values, key = foot_traffic_values.get)
lowest_foot_traffic = min(foot_traffic_values, key = foot_traffic_values.get)
print('Most foot traffic: ' + str(greatest_foot_traffic) + ' | Least foot traffic: ' + str(lowest_foot_traffic))