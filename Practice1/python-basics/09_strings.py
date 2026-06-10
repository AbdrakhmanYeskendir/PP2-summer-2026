# Strings are text values

message = "Hello, Python!"

print(message)

# Accessing characters
print("First character:", message[0])
print("Second character:", message[1])

# String length
print("Length:", len(message))

# Slicing strings
print("First five characters:", message[0:5])
print("From position 7:", message[7:])
print("Before position 5:", message[:5])

# Negative indexing
print("Last character:", message[-1])
print("Second last character:", message[-2])

# String methods
text = "   backend development with python   "

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Without spaces:", text.strip())
print("Title format:", text.title())

# Replacing text
language = "I like Java"
new_language = language.replace("Java", "Python")

print(language)
print(new_language)

# Checking text
course = "Python basics"

print("Python" in course)
print("Java" in course)

# String concatenation
first_name = "Yeskendir"
last_name = "Developer"

full_name = first_name + " " + last_name

print(full_name)

# f-string formatting
age = 19
major = "Computer Science"

info = f"My name is {first_name}, I am {age} years old, and I study {major}."

print(info)