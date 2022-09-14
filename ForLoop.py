countries_list = ["India", "England", "Germany", "England"]
countries_tuple = ("India", "England", "Germany")
countries_set = {"India", "England", "Germany"}

print("*" * 50)

length_of_list = len(countries_list)
for i in range(length_of_list):
    print(countries_list[i])

print("*" * 50)

for country in countries_list:
    print(country)

print("*" * 50)
for character in "CHETAN":
    print(character)

print("*" * 50)

for country in countries_list:
    if country == "England":
        print(country)
        break

print("*" * 50)

for country in countries_list:
    if country == "England":
        continue
    print(country)

print("*" * 50)

for x in range(1, 11, 1):
    if x == 5:
        break
    print(x)
else:
    print("Loop Finished")
print("*" * 50)

for country in countries_set:
    print(country)
