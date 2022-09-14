class Car:

    color = "Black"
    registration_number = "DL12CR8604"

    def print_car(self):
        print("Registration Number : " + self.registration_number)
        print("Color : " + self.color)


my_car = Car()
my_car.print_car()