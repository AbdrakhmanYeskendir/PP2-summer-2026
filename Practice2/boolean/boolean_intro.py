# BOOLEAN VALUES

# Example 1: Boolean results from comparison operators
print(10 > 9)
print(10 == 9)
print(10 < 9)


# Example 2: Using boolean expression in if/else statement
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# EVALUATING VALUES AND VARIABLES

# Example 3: bool() function with direct values
print(bool("Hello"))
print(bool(15))


# Example 4: bool() function with variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))


# TRUE VALUES
# Most non-empty values are True

# Example 5
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


# FALSE VALUES
# Empty values, zero, None and False are False

# Example 6
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Example 7: Object can be False if __len__ returns 0
class MyClass:
    def __len__(self):
        return 0


my_object = MyClass()
print(bool(my_object))

# FUNCTIONS CAN RETURN A BOOLEAN

# Example 8: A function can return True or False
def my_function():
    return True


print(my_function())


# Example 9: Using the boolean result of a function in if/else
def is_python_fun():
    return True


if is_python_fun():
    print("YES!")
else:
    print("NO!")


# Example 10: Built-in functions can also return Boolean values
x = 200

print(isinstance(x, int))
print(isinstance(x, str))