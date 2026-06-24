"""
Practice 5: Python Regular Expressions

This file demonstrates Python RegEx basics using the re module.

Topics covered:
- RegEx introduction
- re.search()
- re.findall()
- re.split()
- re.sub()
- re.match()
- Metacharacters
- Special sequences
- Sets / character classes
- Quantifiers
- Groups
- Flags
- 10 common regex exercises
"""

import re


def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ----------------------------------------------------------------------
# 1. REGEX INTRODUCTION
# ----------------------------------------------------------------------

print_section("1. RegEx Introduction")

text = "Python is powerful. Python is popular."

# RegEx is used to search for patterns in text.
# Example: find the word "Python" in a sentence.

pattern = r"Python"

result = re.search(pattern, text)

if result:
    print("Pattern found:", result.group())
    print("Start index:", result.start())
    print("End index:", result.end())
else:
    print("Pattern not found")


# ----------------------------------------------------------------------
# 2. re.search()
# ----------------------------------------------------------------------

print_section("2. re.search()")

# re.search() finds the first match anywhere in the string.

text = "My phone number is 87011234567"
pattern = r"\d+"

match = re.search(pattern, text)

if match:
    print("First number found:", match.group())
else:
    print("No number found")


# ----------------------------------------------------------------------
# 3. re.match()
# ----------------------------------------------------------------------

print_section("3. re.match()")

# re.match() checks only the beginning of the string.

text1 = "Python is easy"
text2 = "I like Python"

pattern = r"Python"

match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)

print("Text 1 starts with Python:", bool(match1))
print("Text 2 starts with Python:", bool(match2))


# ----------------------------------------------------------------------
# 4. re.findall()
# ----------------------------------------------------------------------

print_section("4. re.findall()")

# re.findall() returns all matches as a list.

text = "Prices: 1200, 450, 9990, 75"
pattern = r"\d+"

numbers = re.findall(pattern, text)

print("All numbers:", numbers)


# ----------------------------------------------------------------------
# 5. re.split()
# ----------------------------------------------------------------------

print_section("5. re.split()")

# re.split() splits a string by a pattern.

text = "apple,banana;cherry orange"
pattern = r"[,;\s]+"

items = re.split(pattern, text)

print("Split result:", items)


# ----------------------------------------------------------------------
# 6. re.sub()
# ----------------------------------------------------------------------

print_section("6. re.sub()")

# re.sub() replaces pattern matches with another string.

text = "Hello, world. Python is cool!"
pattern = r"[,.!]"
replacement = ":"

new_text = re.sub(pattern, replacement, text)

print("Original text:", text)
print("Modified text:", new_text)


# ----------------------------------------------------------------------
# 7. METACHARACTERS
# ----------------------------------------------------------------------

print_section("7. Metacharacters")

sample_text = "cat cot cut cute coat cbt"

# . means any character except newline.
print("Dot . example:")
print(re.findall(r"c.t", sample_text))

# ^ means starts with.
print("Starts with ^ example:")
print(bool(re.search(r"^cat", sample_text)))

# $ means ends with.
print("Ends with $ example:")
print(bool(re.search(r"cbt$", sample_text)))

# * means zero or more repetitions.
print("Star * example:")
print(re.findall(r"cu*t", sample_text))

# + means one or more repetitions.
print("Plus + example:")
print(re.findall(r"cu+t", sample_text))

# ? means zero or one repetition.
print("Question mark ? example:")
print(re.findall(r"cu?t", sample_text))

# | means OR.
print("OR | example:")
print(re.findall(r"cat|coat", sample_text))

# [] means character set.
print("Set [] example:")
print(re.findall(r"c[ao]t", sample_text))

# () creates a group.
print("Group () example:")
date_text = "Date: 18.04.2019"
date_match = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", date_text)

if date_match:
    print("Full date:", date_match.group())
    print("Day:", date_match.group(1))
    print("Month:", date_match.group(2))
    print("Year:", date_match.group(3))


# ----------------------------------------------------------------------
# 8. SPECIAL SEQUENCES
# ----------------------------------------------------------------------

print_section("8. Special Sequences")

text = "User: yeskendir_19, Email: test@example.com, Price: 1200, City: Almaty"

# \d - digit
print(r"\d digits:", re.findall(r"\d", text))

# \D - not digit
print(r"\D non-digits first 20:", re.findall(r"\D", text)[:20])

# \w - word character: letters, digits, underscore
print(r"\w word characters first 20:", re.findall(r"\w", text)[:20])

# \W - not word character
print(r"\W non-word characters:", re.findall(r"\W", text))

# \s - whitespace
print(r"\s spaces:", re.findall(r"\s", text))

# \S - not whitespace
print(r"\S non-spaces first 20:", re.findall(r"\S", text)[:20])

# \A - beginning of string
print(r"\A beginning:", bool(re.search(r"\AUser", text)))

# \Z - end of string
print(r"\Z end:", bool(re.search(r"Almaty\Z", text)))


# ----------------------------------------------------------------------
# 9. SETS AND CHARACTER CLASSES
# ----------------------------------------------------------------------

print_section("9. Sets and Character Classes")

text = "abc ABC 123 _ - @"

# [abc] means a or b or c
print("[abc]:", re.findall(r"[abc]", text))

# [a-z] means lowercase letters
print("[a-z]:", re.findall(r"[a-z]", text))

# [A-Z] means uppercase letters
print("[A-Z]:", re.findall(r"[A-Z]", text))

# [0-9] means digits
print("[0-9]:", re.findall(r"[0-9]", text))

# [^abc] means not a, not b, not c
print("[^abc] first 20:", re.findall(r"[^abc]", text)[:20])


# ----------------------------------------------------------------------
# 10. QUANTIFIERS
# ----------------------------------------------------------------------

print_section("10. Quantifiers")

text = "a ab abb abbb abbbb"

# {n} exactly n repetitions
print("a followed by exactly 2 b:", re.findall(r"ab{2}", text))

# {n,} n or more repetitions
print("a followed by 2 or more b:", re.findall(r"ab{2,}", text))

# {n,m} from n to m repetitions
print("a followed by 2 to 3 b:", re.findall(r"ab{2,3}", text))


# ----------------------------------------------------------------------
# 11. FLAGS
# ----------------------------------------------------------------------

print_section("11. Flags")

text = """Python is great.
python is popular.
PYTHON is everywhere."""

# re.IGNORECASE ignores letter case.
print("IGNORECASE:")
print(re.findall(r"python", text, flags=re.IGNORECASE))

# re.MULTILINE makes ^ and $ work line by line.
print("MULTILINE:")
print(re.findall(r"^python", text, flags=re.IGNORECASE | re.MULTILINE))


# ----------------------------------------------------------------------
# 12. RAW STRINGS
# ----------------------------------------------------------------------

print_section("12. Raw Strings")

# In regex, use r"..." because backslashes are common.
# Example: r"\d+" is cleaner than "\\d+"

text = "Order number: 12345"

pattern = r"\d+"
print("Digits found:", re.findall(pattern, text))


# ----------------------------------------------------------------------
# 13. COMMON REGEX EXERCISES
# ----------------------------------------------------------------------

print_section("13. Common RegEx Exercises")


# Exercise 1:
# Match a string that has 'a' followed by zero or more 'b's.
def match_a_followed_by_zero_or_more_b(text):
    return bool(re.fullmatch(r"ab*", text))


print("Exercise 1:")
print("a:", match_a_followed_by_zero_or_more_b("a"))
print("abbb:", match_a_followed_by_zero_or_more_b("abbb"))
print("ac:", match_a_followed_by_zero_or_more_b("ac"))


# Exercise 2:
# Match a string that has 'a' followed by two to three 'b's.
def match_a_followed_by_two_to_three_b(text):
    return bool(re.fullmatch(r"ab{2,3}", text))


print("\nExercise 2:")
print("abb:", match_a_followed_by_two_to_three_b("abb"))
print("abbb:", match_a_followed_by_two_to_three_b("abbb"))
print("ab:", match_a_followed_by_two_to_three_b("ab"))


# Exercise 3:
# Find sequences of lowercase letters joined with underscore.
def find_lowercase_with_underscore(text):
    return re.findall(r"[a-z]+_[a-z]+", text)


print("\nExercise 3:")
print(find_lowercase_with_underscore("hello_world Test_case user_name wrong-Case"))


# Exercise 4:
# Find sequences of one uppercase letter followed by lowercase letters.
def find_uppercase_followed_by_lowercase(text):
    return re.findall(r"[A-Z][a-z]+", text)


print("\nExercise 4:")
print(find_uppercase_followed_by_lowercase("Hello World PYTHON TestCase Almaty"))


# Exercise 5:
# Match a string that has 'a' followed by anything, ending in 'b'.
def match_a_anything_ending_b(text):
    return bool(re.fullmatch(r"a.*b", text))


print("\nExercise 5:")
print("axxxb:", match_a_anything_ending_b("axxxb"))
print("ab:", match_a_anything_ending_b("ab"))
print("accc:", match_a_anything_ending_b("accc"))


# Exercise 6:
# Replace all occurrences of space, comma, or dot with a colon.
def replace_space_comma_dot(text):
    return re.sub(r"[ ,\.]", ":", text)


print("\nExercise 6:")
print(replace_space_comma_dot("Hello, world. Python is cool"))


# Exercise 7:
# Convert snake_case string to camelCase string.
def snake_to_camel(text):
    parts = text.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


print("\nExercise 7:")
print(snake_to_camel("hello_world_python"))


# Exercise 8:
# Split a string at uppercase letters.
def split_at_uppercase(text):
    return re.findall(r"[A-Z][a-z]*", text)


print("\nExercise 8:")
print(split_at_uppercase("HelloWorldPythonRegex"))


# Exercise 9:
# Insert spaces between words starting with capital letters.
def insert_spaces_before_capitals(text):
    return re.sub(r"(?<!^)([A-Z])", r" \1", text)


print("\nExercise 9:")
print(insert_spaces_before_capitals("HelloWorldPythonRegex"))


# Exercise 10:
# Convert camelCase string to snake_case.
def camel_to_snake(text):
    snake = re.sub(r"(?<!^)([A-Z])", r"_\1", text)
    return snake.lower()


print("\nExercise 10:")
print(camel_to_snake("helloWorldPythonRegex"))


# ----------------------------------------------------------------------
# 14. PRACTICAL MINI EXAMPLES
# ----------------------------------------------------------------------

print_section("14. Practical Mini Examples")

receipt_text = """
1. Product A 2,000 x 154,00 308,00 Стоимость 308,00
2. Product B 1,000 x 51,00 51,00 Стоимость 51,00
ИТОГО: 359,00
Время: 18.04.2019 11:13:58
Банковская карта: 359,00
"""

# Find all prices like 154,00 or 1 200,00
prices = re.findall(r"\d[\d\s]*,\d{2}", receipt_text)
print("Prices:", prices)

# Find date and time
date_time_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}", receipt_text)
if date_time_match:
    print("Date and time:", date_time_match.group())

# Find total
total_match = re.search(r"ИТОГО:\s*([\d\s]+,\d{2})", receipt_text)
if total_match:
    print("Total:", total_match.group(1))

# Find payment method
payment_match = re.search(r"Банковская карта", receipt_text)
if payment_match:
    print("Payment method:", payment_match.group())


print("\nregex.py completed successfully.")