# __INIT__ METHOD
# The __init__ method is called automatically when an object is created.

# Example 1: Class with __init__
class Student:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university

    def show_info(self):
        print(f"{self.name}, {self.age} years old, studies at {self.university}")


student1 = Student("Yeskendir", 19, "KBTU")
student1.show_info()


# Example 2: Another object with different data
student2 = Student("Ali", 20, "KBTU")
student2.show_info()


# Example 3: Class for a car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_car(self):
        print(f"{self.brand} {self.model}, {self.year}")


car1 = Car("Mercedes", "W124", 1994)
car1.show_car()


# Example 4: Modifying object property
student1.age = 20
student1.show_info()