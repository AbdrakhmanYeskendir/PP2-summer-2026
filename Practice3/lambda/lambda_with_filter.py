# LAMBDA WITH FILTER
# filter() selects items that match a condition.

# Example 1: Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("Even numbers:", even_numbers)


# Example 2: Filter positive numbers
temperatures = [-5, 0, 10, 18, -2, 25]

positive_temperatures = list(filter(lambda temp: temp > 0, temperatures))

print("Positive temperatures:", positive_temperatures)


# Example 3: Filter words longer than 5 characters
words = ["python", "java", "backend", "sql", "developer"]

long_words = list(filter(lambda word: len(word) > 5, words))

print("Long words:", long_words)


# Example 4: Filter students who passed
students = [
    {"name": "Ali", "score": 45},
    {"name": "Dana", "score": 75},
    {"name": "Miras", "score": 60},
    {"name": "Aigerim", "score": 30}
]

passed_students = list(filter(lambda student: student["score"] >= 50, students))

print("Passed students:")
for student in passed_students:
    print(student["name"], student["score"])


# Example 5: Filter non-empty strings
names = ["Yeskendir", "", "Ali", "", "Dana"]

valid_names = list(filter(lambda name: name != "", names))

print("Valid names:", valid_names)