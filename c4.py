import csv
from pprint import pprint

database = {}

survey = open("survey.csv", newline="")
survey_reader = csv.reader(survey)

for row in survey_reader:
    name, age, height, colour_eyes = row
    database[name] = int(age), float(height), colour_eyes

pprint(database)
name = input("Name: ")
record = database[name]
age, height, colour_eyes = record
print("You have", colour_eyes, "eyes")
print("You are", age, "Years old")
print("You are", height, "metres tall")