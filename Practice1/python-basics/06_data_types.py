# Python has different built-in data types

text_value = "Python"
integer_value = 19
float_value = 3.14
complex_value = 2 + 3j
boolean_value = True

list_value = ["Python", "Java", "C++"]
tuple_value = ("backend", "database", "API")
range_value = range(5)

dict_value = {
    "name": "Yeskendir",
    "age": 19,
    "major": "Computer Science"
}

set_value = {"Python", "SQL", "Git"}
frozenset_value = frozenset({"Django", "FastAPI", "PostgreSQL"})

none_value = None

print(type(text_value))
print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(boolean_value))

print(type(list_value))
print(type(tuple_value))
print(type(range_value))
print(type(dict_value))
print(type(set_value))
print(type(frozenset_value))
print(type(none_value))

print("List example:", list_value)
print("Dictionary example:", dict_value)
print("Set example:", set_value)