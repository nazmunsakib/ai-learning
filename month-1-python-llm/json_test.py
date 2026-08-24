#json

import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "isEmployed": True,
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

json_data = json.dumps(data)

print("JSON Data:")
print(json_data)

#Parsing JSON data
parsed_data = json.loads(json_data)
print("\nParsed Data:")
print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])
print("Skills:", parsed_data["skills"])
print("Is Employed:", parsed_data["isEmployed"])
print("Address:")
print("  Street:", parsed_data["address"]["street"])
print("  Zip:", parsed_data["address"]["zip"])

#Writing JSON data to a file
print("\nWriting JSON data to user.json file...")
with open("user.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nData has been written to user.json file.")

#Reading JSON data from a file
print("\nReading JSON data from user.json file...")
with open("user.json", "r") as file:
    file_data = json.load(file)
    
print("\nFile Data:")
print("Name:", file_data["name"])
print("Age:", file_data["age"])
print("City:", file_data["city"])
print("Skills:", file_data["skills"])
print("Is Employed:", file_data["isEmployed"])
print("Address:")
print("  Street:", file_data["address"]["street"])
print("  Zip:", file_data["address"]["zip"])