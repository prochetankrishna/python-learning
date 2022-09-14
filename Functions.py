def display():
    print("Hello World !")


def greet_user(user_name):
    print("Hello " + user_name)


def custom_sum(num_one, num_two):
    print(num_one + num_two)


def print_countries(*countries):
    print(type(countries))
    for country in countries:
        print(country)


def print_employee(name, age, location):
    print(name)
    print(age)
    print(location)


def print_country_capital(**country_capital):
    print(type(country_capital))
    print(country_capital)


def print_location(location="Delhi"):
    print(location)


def find_exponent(num_one, num_two):
    return num_one ** num_two


exponent_lambda = lambda num_one, num_two: num_one ** num_two


# Recursion
def print_natural_numbers(num):
    if num == 0:
        return
    print(num)
    print_natural_numbers(num - 1)


display()
greet_user("Chetan Krishna")
custom_sum(1, 2)
print_countries("India", "England", "Germany")
print_employee(name="Chetan", location="Delhi", age=28)
print_country_capital(India="Delhi", USA="Washington", England="London")
print_location()
print(find_exponent(2, 5))
# print_natural_numbers(10)
print(exponent_lambda(2, 5))
