# BUILT-IN FUNCTIONS - ENUMERATE, ZIP, SORTED

"""
This file demonstrates:
- enumerate()
- zip()
- sorted()
- type conversions
"""

print("1. enumerate() example")

tasks = ["Learn Python", "Practice Git", "Read JSON"]

for index, task in enumerate(tasks):
    print(f"{index}.{task}")


print("\n2. zip() example")

names = ["Ali", "Dana", "Miras"]
scores = [80, 95, 70]

for name, score in zip(names, scores):
    print(f"{name} - {score}")


print("\n3. Create list of dictionaries using zip()")

students = []

for name, score in zip(names, scores):
    students.append({
        "name": name,
        "score": score
    })

print(students)


print("\n4. sorted() with numbers")

numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers)

print("Original numbers:", numbers)
print("Sorted numbers:", sorted_numbers)


print("\n5. sorted() with dictionaries")

students = [
    {"name": "Ali", "score": 80},
    {"name": "Dana", "score": 95},
    {"name": "Miras", "score": 70}
]

students_sorted_by_score = sorted(
    students, 
    key = lambda student: student["score"],
    reverse = True
)

print("Students sorted by score descending:")

for student in students_sorted_by_score:
    print(student["name"], "-", student["score"])


print("\n6. Type conversions")

number_text = "25"
float_text = "3.14"
number = 10

converted_int = int(number_text)
converted_float = float(float_text)
converted_string = str(number)
converted_bool = bool(number)

print("String to int:", converted_int)
print("String to float:", converted_float)
print("Int to string:", converted_string)
print("Int to bool:", converted_bool)


print("\n7. list(), tuple(), set() conversions")

numbers_tuple = (1, 2, 3)
numbers_list = [1, 2, 2, 3, 3]

converted_list = list(numbers_tuple)
converted_tuple = tuple(numbers_list)
converted_set = set(numbers_list)

print("Tuple to list:", converted_list)
print("List to tuple:", converted_tuple)
print("List to set:", converted_set)


print("\nenumerate_zip_examples.py completed successfully.")