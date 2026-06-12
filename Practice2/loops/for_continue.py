# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# Example 1: The continue statement
# Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


# Example 2: Skip number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)