# SUPER FUNCTION
# super() is used to call methods from the parent class.

# Example 1: Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Example 2: Child class using super()
class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def show_student_info(self):
        self.show_person_info()
        print(f"University: {self.university}")


student1 = Student("Yeskendir", 19, "KBTU")
student1.show_student_info()


# Example 3: Parent class for vehicles
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine started.")


# Example 4: Child class extending parent behavior
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_car(self):
        print(f"Car: {self.brand} {self.model}")


car1 = Car("Mercedes", "W124")
car1.start_engine()
car1.show_car()