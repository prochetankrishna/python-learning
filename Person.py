class Person:

    def __init__(self):
        self.name = "Unavailable"
        self.gender = "Unavailable"

    # def __init__(self, name, gender):
    #    self.name = name
    #    self.gender = gender

    def print_person(self):
        print("Name : " + self.name)
        print("Gender : " + self.gender)

    def __set_name__(self, owner, name):
        self.name = name


unavailable = Person()
# chetan = Person("Chetan", "M")
# riya = Person("Riya", "F")

# chetan.__set_name__(chetan, "Chetan Krishna")
# chetan.print_person()
# riya.print_person()
unavailable.print_person()
