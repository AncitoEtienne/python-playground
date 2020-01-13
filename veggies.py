#by Ancito and David 

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

#Loops through each vegetable
import csv
with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length'])
    for vegetable in vegetables:
    	vegetable_name = vegetable['name']
    	vegetable_color = vegetable["color"]
    	vegetable_length = len(vegetable_name)
    	writer.writerow([vegetable_name, vegetable_color, vegetable_length])
   
#In the loop, write the name of each vegetable and the color into a CSV called vegetables.csv
#with open('vegetables.csv', 'w') as f:
#print(rows)