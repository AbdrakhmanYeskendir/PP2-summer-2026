# CLASS VARIABLES VS INSTANCE VARIABLES
# Class variables are shared by all objects.
# Instance variables belong to each object separately.

# Example 1: Class variable
class Student:
    university = "KBTU"

    def __init__(self, name, major):
        self.name = name
        self.major = major

    def show_info(self):
        print(f"{self.name} studies {self.major} at {self.university}")


student1 = Student("Yeskendir", "Computer Science")
student2 = Student("Ali", "Information Systems")

student1.show_info()
student2.show_info()


# Example 2: Changing instance variable
student1.major = "Backend Development"

student1.show_info()
student2.show_info()


# Example 3: Changing class variable
Student.university = "Kazakh-British Technical University"

student1.show_info()
student2.show_info()


# Example 4: Counting created objects using class variable
class Course:
    total_courses = 0

    def __init__(self, title):
        self.title = title
        Course.total_courses += 1

    def show_course(self):
        print("Course:", self.title)


course1 = Course("PP2")
course2 = Course("Databases")
course3 = Course("OOP")

course1.show_course()
course2.show_course()
course3.show_course()

print("Total courses:", Course.total_courses)