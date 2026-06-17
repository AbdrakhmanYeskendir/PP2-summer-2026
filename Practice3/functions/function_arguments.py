# FUNCTION ARGUMENTS
# Arguments are values passed into a function.

# Example 1: Positional arguments
def introduce(name, age):
    print(f"My name is {name}. I am {age} years old.")


introduce("Yeskendir", 19)


# Example 2: Keyword arguments
def describe_car(brand, model, year):
    print(f"Car: {brand} {model}, year: {year}")


describe_car(brand="Mercedes", model="W124", year=1994)


# Example 3: Default argument
def greet_user(name="Guest"):
    print(f"Hello, {name}!")


greet_user("Ali")
greet_user()


# Example 4: Passing a list as an argument
def print_skills(skills):
    print("Skills:")
    for skill in skills:
        print("-", skill)


backend_skills = ["Python", "SQL", "FastAPI", "Git"]
print_skills(backend_skills)


# Example 5: Positional-only argument
def square_number(x, /):
    print("Square:", x * x)


square_number(5)


# Example 6: Keyword-only argument
def create_profile(*, username, role):
    print(f"Username: {username}")
    print(f"Role: {role}")


create_profile(username="yeskendir", role="student")