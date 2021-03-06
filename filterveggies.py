#Ancito and David
import csv
import json

greenveggies = []
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict
for vegetable in rows:
    if vegetable["color"] == "green":
            #print(vegetable)
        greenveggies.append(vegetable)
        writer.writerow((vegetable['name'], vegetable['color'])
with open('greenveggies.json', 'w') as f:
     json.dump(greenveggies, f)

with open('greenveggies.csv', "w") as f:
    writer = csv.writer(f)
    writer.whiterow(['name', 'color'])
    vegetable_name = vegetable['name']
    vegetable_color = vegetable["color"]


