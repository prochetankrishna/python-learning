countries = ("India", "England", "Germany")
print(type(countries))

print(len(countries))

num_list = [1]
print(type(num_list))

num_tuple = (1, )
print(type(num_tuple))

name_list = ["John", "James"]
name_tuple = tuple(name_list)
print(name_tuple)
tuple_to_list = list(name_tuple)
print(tuple_to_list)

countries_list = list(countries)
countries_list.append("USA")
countries = tuple(countries_list)
print(countries)

# Unpacking of tuple
employee = ("Chetan Krishna", 28, "Delhi")
(name, age, location) = employee
print(name)
print(age)
print(location)

print(countries[1:2])