#If you have only one statement to execute, you can put it on the same line as the if statement.

#Example 1: One-line if statement
a = 5
b = 2
if a > b: print("a is greater than b")
# Note: You still need the colon : after the condition.


#Example 2: Shorthand if...else
a = 2
b = 330
print("A") if a > b else print("B")


#Example 3: Assign a value with if..else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Example 4: Multiple conditions on one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#PRACTICAL EXAMPLES

#Finding the maximum of two numbers
x = 15
y = 20
max_value = x if x > y else y
print("Max value:", max_value)


#Setting a default value:

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)