'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

# Example 1: Execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Example 2: Looping through a string
for x in "banana":
    print(x)


# Example 3: Using the range() function
for x in range(6):
    print(x)


# Example 4: Using range with start and end values
for x in range(2, 6):
    print(x)


# Example 5: Using range with step
for x in range(2, 10, 2):
    print(x)