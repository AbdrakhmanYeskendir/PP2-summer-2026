# INHERITANCE BASICS
# Inheritance allows one class to use properties and methods of another class.

# Example 1: Parent class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")


# Example 2: Child class
class Student(Person):
    pass


student1 = Student("Yeskendir")
student1.introduce()


# Example 3: Child class with its own method
class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching Python.")


teacher1 = Teacher("Mikhail Georgievich")
teacher1.introduce()
teacher1.teach()


# Example 4: Another child class
class Developer(Person):
    def code(self):
        print(f"{self.name} is writing backend code.")


developer1 = Developer("Ali")
developer1.introduce()
developer1.code()