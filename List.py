countries = ["India", "England", "Germany"]
print(countries)
print(type(countries))

# Length of the list
print(len(countries))
print(countries[1])
print(countries[-3])

countries.append("USA")
print(countries)
countries[3] = "Australia"
print(countries)

countries.insert(2, "Canada")
print(countries)

random_list = ["Chetan Krishna", 101, 30000.0, True]
print(random_list)

print("*" * 50)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_list[:3])
print(num_list[3:])

print("India" in countries)
print("Pakistan" in countries)
print("Sri Lanka" not in countries)