import math

import random

import json  

# math module
a=5

print(pow(a,2))

print(round(math.sqrt(5),2))


# random module 
num = random.randint(1, 10) 

print(f"Random integer between 1 and 10: {num}") 

programming_languages = ["Java", "C", "C++", "Python"] 

choosen_programming_language = random.choice(programming_languages) 

print(f"Randomly chosen language: {choosen_programming_language}") 

person_data = { 
    "name": "Jonny", 
    "age": 30, 
} 

json_string = json.dumps(person_data, indent=5) 
print(json_string)  