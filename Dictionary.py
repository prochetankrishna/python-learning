employeeDict = {
    "name": "Chetan",
    "age": 28,
    "location": "Delhi",
    "language": ["Java", "C++", "JavaScript"]
}
print(employeeDict)

print(employeeDict["location"])
# print(employeeDict["address"])
employeeDict["age"] = 29
print(employeeDict)
print(type(employeeDict))

print(employeeDict.get("name"))
print(employeeDict.keys());
print(employeeDict.values())
print(employeeDict.items())