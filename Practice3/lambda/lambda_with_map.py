# LAMBDA WITH MAP
# map() applies a function to every item in an iterable.

# Example 1: Double all numbers
numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda number: number * 2, numbers))

print("Original numbers:", numbers)
print("Doubled numbers:", doubled_numbers)


# Example 2: Convert words to uppercase
words = ["python", "sql", "fastapi", "git"]

uppercase_words = list(map(lambda word: word.upper(), words))

print("Uppercase words:", uppercase_words)


# Example 3: Get lengths of words
word_lengths = list(map(lambda word: len(word), words))

print("Word lengths:", word_lengths)


# Example 4: Add 10 points to each score
scores = [70, 82, 91, 65]

updated_scores = list(map(lambda score: score + 10, scores))

print("Updated scores:", updated_scores)


# Example 5: Convert prices to strings
prices = [1000, 2500, 3990]

formatted_prices = list(map(lambda price: f"{price} KZT", prices))

print("Formatted prices:", formatted_prices)