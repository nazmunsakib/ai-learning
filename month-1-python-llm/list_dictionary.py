#List

skills = ["Python", "Java", "C++", "JavaScript"]

print("My skills are:")

for skill in skills:
    print(skill)


#Dictionary
developer = {
    "name": "Nazmun Sakib",
    "role": "Software Developer",
    "experience": 8,
    "skills": skills,
    "country": "Bangladesh"
}

print("\nDeveloper Information:")
print("Name:", developer["name"])
print("Role:", developer["role"])
print("Experience:", developer["experience"], "years")
print("Country:", developer["country"])

print("\nSkills:")

for skill in developer["skills"]:
    print(skill)


#List methods
#Adding an element to the list
skills.append("LLM")
print("\nUpdated Skills after adding LLM:")
for skill in skills:
    print(skill)

#Inserting an element at a specific position
skills.insert(2, "WordPress")
print("\nUpdated Skills after inserting WordPress at index 2:")
for skill in skills:
    print(skill)

#Modifying an element in the list
skills[1] = "Java (Updated)"
print("\nUpdated Skills after modifying Java:")
for skill in skills:
    print(skill)

#Removing an element from the list
skills.remove("C++")
print("\nUpdated Skills after removing C++:")
for skill in skills:
    print(skill)

#Removing an element by index
skills.pop(3);
print("\nUpdated Skills after deleting the element at index 3:")
for skill in skills:
    print(skill)

#Length of the list
print("\nTotal number of skills:", len(skills))

#checking if an element exists in the list
if "Python" in skills:
    print("Python is in the skills list.")

#Slicing the list
print("\nSliced Skills (from index 1 to 3):", skills[1:4])

#Sorting the list
skills.sort()
print("\nSorted Skills:")
for skill in skills:
    print(skill)


#Dictionary methods
#Adding a new key-value pair to the dictionary
developer["email"] = "nazmunsakib81@gmail.com"
print("\nUpdated Developer Information after adding email:")
for key, value in developer.items():
    print(key + ":", value)

#Modifying an existing key-value pair in the dictionary
developer["experience"] = 9
print("\nUpdated Developer Information after modifying experience:")
for key, value in developer.items():
    print(key + ":", value)

#Removing a key-value pair from the dictionary
del developer["country"]
print("\nUpdated Developer Information after removing country:")
for key, value in developer.items():
    print(key + ":", value)

#Checking if a key exists in the dictionary
if "name" in developer:
    print("\nName exists in the developer dictionary.")

#Getting the keys and values of the dictionary
print("\nKeys in the developer dictionary:", developer.keys())
print("Values in the developer dictionary:", developer.values())

#removing a key-value pair using pop()
developer.pop("role")
print("\nUpdated Developer Information after popping role:")
for key, value in developer.items():
    print(key + ":", value)

#Remove key
del developer["email"]
print("\nUpdated Developer Information after removing email:")
for key, value in developer.items():
    print(key + ":", value)
    