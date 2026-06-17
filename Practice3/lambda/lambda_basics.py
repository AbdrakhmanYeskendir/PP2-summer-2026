# LAMBDA BASICS
# A lambda function is a small anonymous function.

# Example 1: Simple lambda
double = lambda x: x * 2

print("Double:", double(5))


# Example 2: Lambda with two arguments
add = lambda a, b: a + b

print("Sum:", add(10, 7))


# Example 3: Lambda for checking even number
is_even = lambda number: number % 2 == 0

print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))


# Example 4: Regular function vs lambda function
def square_regular(x):
    return x * x


square_lambda = lambda x: x * x

print("Regular function square:", square_regular(6))
print("Lambda function square:", square_lambda(6))


# Example 5: Lambda inside another function
def create_multiplier(n):
    return lambda x: x * n


double_number = create_multiplier(2)
triple_number = create_multiplier(3)

print("Double 8:", double_number(8))
print("Triple 8:", triple_number(8))