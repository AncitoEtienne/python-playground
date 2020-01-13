#by Ancito and David
import csv
import json

#Read vegetables.csv
#(see previous section)

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    rows = [dict(row) for row in rows] # Convert OrderedDict to regular dict
    vegetables = rows

# Print the variable vegetables    
print(vegetables)

#write vegetables as a JSON file
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent = 4)