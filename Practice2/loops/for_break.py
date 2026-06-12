# With the break statement we can stop the loop before it has looped through all the items

# Example 1: The break statement
# Exit the loop when x is "banana"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# Example 2: 
# Exit the loop when x is "banana", but this time the break comes before the print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# Example 3: Stop loop when number is 4
for i in range(1, 7):
    if i == 4:
        break
    print(i)
    

