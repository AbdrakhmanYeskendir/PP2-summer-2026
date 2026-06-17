# RETURN VALUES
# A function can return a result using the return keyword.

# Example 1: Returning a simple value
def get_university():
    return "KBTU"


university = get_university()
print("University:", university)


# Example 2: Returning calculation result
def add_numbers(a, b):
    return a + b


result = add_numbers(10, 5)
print("Sum:", result)


# Example 3: Returning boolean value
def is_adult(age):
    return age >= 18


print("Is adult:", is_adult(19))
print("Is adult:", is_adult(16))


# Example 4: Returning multiple values
def calculate_rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


rectangle_area, rectangle_perimeter = calculate_rectangle(5, 3)

print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)


# Example 5: Returning a list
def get_even_numbers(numbers):
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers_list = [1, 2, 3, 4, 5, 6]
print("Even numbers:", get_even_numbers(numbers_list))