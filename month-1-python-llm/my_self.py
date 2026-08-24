#Practice with My Self data

import json

my_self = {
    "name": "Nazmun Sakib",
    "profession": "Software Developer",
    "age": 25,
    "country": "Bangladesh",
    "skills": ["PHP", "Python", "JavaScript", "SQL"]
}

with open("developer_info.json", "w") as file:
    json.dump(my_self, file, indent=4)

    print("My self data has been written to developer_info.json file.")


with open("developer_info.json", "r") as file:
    developer_info = json.load(file)

print("\nDeveloper Information:")
print("Name:", developer_info["name"])
print("Profession:", developer_info["profession"])
print("Age:", developer_info["age"])
print("Country:", developer_info["country"])
print("\nSkills:")

for skill in developer_info["skills"]:
    print(skill)
