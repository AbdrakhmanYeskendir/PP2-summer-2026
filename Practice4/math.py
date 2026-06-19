# Example 1:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# Example 2:

z = abs(-7.25)

print(z)


# Example 3:

a = pow(4, 3)

print(a)


#Example 4:

b = round(3.27)
c = round(3.5)
d = round(3.6)

e = round(3.123456, 2)

print(b)
print(c)
print(d)
print(e)


# Example 5:

import math

f = math.sqrt(64)

print(f)


# Example 6
 
g = math.ceil(1.4)
h = math.floor(1.4)

print(g, h)


# Example 7

i = math.pi

print(i)


#Example 8

j = math.sin(math.radians(60))
k = math.cos(math.radians(60))

print(j)
print(k)


# Example 9

l = math.e

print(l)

# (random, randint, choice, shuffle)
# Example 10
# The random() method returns a random floating number between 0 and 1.

import random

print(random.random())


# Example 11
# The randint() method returns an integer number selected element from the specified range.
# Note: This method is an alias for randrange(start, stop+1).

import random

print(random.randint(3, 9))


# Example 12
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

import random

myList = ["apple", "banana", "cherry"]

print(random.choice(myList))

#Example 13
# The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
# Note: This method changes the original list, it does not return a new list.

import random

random.shuffle(myList)

print(myList)