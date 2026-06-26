# BUILT-IN FUNCTIONS - MAP, FILTER, REDUCE

"""
This file demonstrates:
- len()
- sum()
- min()
- max()
- map()
- filter()
- reduce()
"""

from functools import reduce

print("1. Basic built_in functions")

numbers = [10, 25, 7, 30, 14]

print("Numbers:", numbers)
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Average:", sum(numbers)/len(numbers))

print("\n2. map() example")

# map() applies a function to every item in a list

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print("Original numbers:", numbers)
print("Squares:", squares)


print("\n3. filter() example")

# filter() keeps only items that match a condition

ages = [12, 17, 18, 22, 15, 30]

adults = list(filter(lambda age: age >= 18, ages))

print("All ages:", ages)
print("Adults:", adults)


print("\n4. reduce() example")

# reduce() combines all items into one final result

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a, b: a * b, numbers)

print("Numbers:", numbers)
print("Product:", product)


print("\n5. map() with strings")

names = ["dana", "ali", "miras"]

capitalized_names = list(map(lambda name: name.capitalize(), names))

print("Original names:", names)
print("Capitalized names:", capitalized_names)


print("\n6. filter() with strings")

words = ["Python", "SQL", "FastAPI", "Git", "PostgreSQL"]

long_words = list(filter(lambda word: len(word) > 5, words))

print("Words:", words)
print("Words longer than 5 characters:", long_words)


print("\nmap_filter_reduce.py completed successfully.")
