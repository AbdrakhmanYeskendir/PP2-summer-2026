# LAMBDA WITH SORTED
# sorted() can use lambda as a custom sorting key.

# Example 1: Sort numbers
numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers)

print("Sorted numbers:", sorted_numbers)


# Example 2: Sort words by length
words = ["Python", "SQL", "FastAPI", "Git", "PostgreSQL"]

sorted_words = sorted(words, key=lambda word: len(word))

print("Words sorted by length:", sorted_words)


# Example 3: Sort students by score
students = [
    {"name": "Ali", "score": 75},
    {"name": "Dana", "score": 92},
    {"name": "Miras", "score": 60}
]

students_by_score = sorted(students, key=lambda student: student["score"])

print("Students sorted by score:")
for student in students_by_score:
    print(student["name"], student["score"])


# Example 4: Sort students by score descending
students_by_score_desc = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

print("Students sorted by score descending:")
for student in students_by_score_desc:
    print(student["name"], student["score"])


# Example 5: Sort products by price
products = [
    {"name": "Laptop", "price": 450000},
    {"name": "Mouse", "price": 7000},
    {"name": "Keyboard", "price": 25000}
]

products_by_price = sorted(products, key=lambda product: product["price"])

print("Products sorted by price:")
for product in products_by_price:
    print(product["name"], product["price"])