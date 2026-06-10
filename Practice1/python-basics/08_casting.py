# Casting means converting one data type into another

x = int(5)
y = int(3.9)
z = int("12")

print(x)
print(y)
print(z)

a = float(10)
b = float(7.5)
c = float("4.25")

print(a)
print(b)
print(c)

name = str("Python")
age = str(19)
height = str(1.83)

print(name)
print(age)
print(height)

# Example with input-like values

number_as_text = "100"
number_as_int = int(number_as_text)

result = number_as_int + 50

print("Result:", result)

# Without casting, this would be string concatenation
first = "10"
second = "20"

print("As strings:", first + second)
print("As numbers:", int(first) + int(second))