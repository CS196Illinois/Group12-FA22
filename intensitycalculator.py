import json

# read file
with open('personal.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

date = int(input("Enter the day: "))
time = int(input("Enter the time: "))


# show values
print("Foot traffic: " + str(obj['analysis'][date]['hour_analysis'][time]['intensity_txt']))
