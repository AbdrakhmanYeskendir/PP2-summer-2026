# Exercise 1
import math

degree = int(input())

radian = math.radians(degree)

print(radian)


# Exercise 2

def area_trapezoid(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

print(area_trapezoid(5, 5, 6))


# Exercise 3

def area_reg_polygon(num_sides, len_side):
    area = (num_sides * math.pow(len_side, 2)) / (4 * math.tan(math.radians(180/num_sides)))

    return area

print(area_reg_polygon(4, 25))

# Exercise 4

def area_parallelogram(length_of_base, height):
    area = length_of_base * height

    return area

print(area_parallelogram(5, 6))

