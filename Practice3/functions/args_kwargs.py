# *ARGS AND **KWARGS
# *args allows a function to accept many positional arguments.
# **kwargs allows a function to accept many keyword arguments.

# Example 1: Using *args
def sum_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Sum:", sum_numbers(1, 2, 3))
print("Sum:", sum_numbers(10, 20, 30, 40))


# Example 2: Using *args with strings
def show_languages(*languages):
    print("Programming languages:")

    for language in languages:
        print("-", language)


show_languages("Python", "Java", "C++")


# Example 3: Using **kwargs
def show_profile(**user):
    print("User profile:")

    for key, value in user.items():
        print(f"{key}: {value}")


show_profile(name="Yeskendir", age=19, university="KBTU")


# Example 4: Combining normal arguments, *args, and **kwargs
def create_report(title, *scores, **student_info):
    print("Report title:", title)

    print("Scores:")
    for score in scores:
        print("-", score)

    print("Student info:")
    for key, value in student_info.items():
        print(f"{key}: {value}")


create_report(
    "PP2 Practice Report",
    85,
    90,
    78,
    name="Yeskendir",
    group="Summer PP2"
)