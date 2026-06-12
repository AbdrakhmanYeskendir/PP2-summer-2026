#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

#Example 1: The elif keyword
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif b == a:
    print("a and b are equal")


#Example 2: Multiple elif statements
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")


#Example 3: Categorizing age groups
age = 25

if age  < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")


#Example 4: Day of the week checker
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")