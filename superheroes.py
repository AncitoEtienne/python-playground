#By Ancito and David
#Reads superheroes.json (in this folder)
import json
from pprint import pprint
import csv


#read superheroes.json
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

#Write header to the csv file
with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    headers = ["name", "age", "secretIdentity", "powers", "squadName", "homeTown", "formed", "secretBase", "active"]
    writer.writerow(headers)

#Loop over the numbers
    members = superheroes ['members']
    squadName = superheroes ['squadName']
    homeTown = superheroes ['homeTown']
    formed = superheroes ['formed']
    secretBase = superheroes ['secretBase']
    active = superheroes ['active']
    for member in members:
    #define variables
        name = member['name']
        age = member["age"]
        secretIdentity = member["secretIdentity"]
        powers = member ['powers']
        for power in powers:
            row = [name, age, secretIdentity, powers, squadName, homeTown, formed, secretBase, active]
            writer.writerow(row)
    
#Prints those powers to the terminal


