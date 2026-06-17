# CLASS DEFINITION
# A class is a blueprint for creating objects.

# Example 1: Simple class
class Student:
    name = "Yeskendir"
    university = "KBTU"


student1 = Student()

print("Student name:", student1.name)
print("University:", student1.university)


# Example 2: Class with method
class Course:
    title = "Programming Principles 2"

    def show_title(self):
        print("Course title:", self.title)


course1 = Course()
course1.show_title()


# Example 3: Creating multiple objects
student2 = Student()
student3 = Student()

student2.name = "Ali"
student3.name = "Dana"

print("Student 2:", student2.name)
print("Student 3:", student3.name)


# Example 4: Object properties can be modified
student1.name = "Abdrakhman Yeskendir"

print("Updated student name:", student1.name)