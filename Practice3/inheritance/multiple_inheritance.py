# MULTIPLE INHERITANCE
# A class can inherit from more than one parent class.

# Example 1: First parent class
class Swimmer:
    def swim(self):
        print("This object can swim.")


# Example 2: Second parent class
class Runner:
    def run(self):
        print("This object can run.")


# Example 3: Child class with multiple inheritance
class Athlete(Swimmer, Runner):
    def compete(self):
        print("Athlete is competing.")


athlete1 = Athlete()
athlete1.swim()
athlete1.run()
athlete1.compete()


# Example 4: Multiple inheritance with different skills
class BackendDeveloper:
    def write_api(self):
        print("Writing a backend API.")


class DatabaseDeveloper:
    def design_database(self):
        print("Designing a database schema.")


class FullStackBackendEngineer(BackendDeveloper, DatabaseDeveloper):
    def build_project(self):
        print("Building a full backend project.")


engineer = FullStackBackendEngineer()
engineer.write_api()
engineer.design_database()
engineer.build_project()


# Example 5: Checking method resolution order
print("Method Resolution Order:")
for class_name in FullStackBackendEngineer.__mro__:
    print(class_name)