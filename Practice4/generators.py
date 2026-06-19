# An iterator is an object that has a countable number of values
# An iterator is an object that can be iterated upon, meaning that you can traverse through the all values
# Technically, in python, an iterator is an object which implements the iterator protocol, which consists the methods __iter__() and __next__()


# Example 1: Return an iterator from a tuple, and print each value
# Lists, tuples, dictionaries, and sets are all iterable objects.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Example 2: Strings are also iterable objects
mystr = "banana"
myIt = iter(mystr)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))


# LOOPING THROUGH AN ITERATOR

# Example 3: Iterate the values of tuple

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


#Example 4: Iterate the characters of a string

mystr = "banana"

for x in mystr:
    print(x)


#CREATE AN ITERATOR

# Example 5: Create an iterator that return numbers, 
# starting with 1, and each sequence will increase 
# by one(returning 1, 2, 3, 4, 5 etc.):

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# Example 6: StopIteration

class LimitedNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = LimitedNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


# GENERATORS IN PYTHON

# A generator function is a special type of function that returns an iterator object.
# Instead of using return to send back a single value, generator functions use YIELD to produce a series of results over time.
# The function pauses its execution after yield, maintaining its state between iterations.

# Example 1:
# This generator function fun yields numbers from 1 up to a specified max.
# Each call to next() on the generator object resumes execution right after the yield statement, where it last left off.


def fun(max):
   cnt = 1
   while cnt <= max:
      yield cnt
      cnt += 1

ctr = fun(5)
for n in ctr:
   print(n)


''' Why do we need generators?

--Memory efficient: Handle large or infinite data without loading everything into memory
--No List Overhead: Yield items one by one, avoiding full list creation
--Support Infinite Sequences: Ideal for generating unbounded data like Fibonacci seies
--Pipeline Processing: Chain generators to process data in stages efficiently

'''

# Example 2:

def fun1():
   yield 1
   yield 2
   yield 3

# Driver code to check above generator function
for val in fun1():
   print(val)


# Example 3:
def fun2():
  return 1 + 2 + 3

res = fun2()
print(res)


# Example 4: Generator Expression

sq = (x*x for x in range(1, 6))
for i in sq:
  print(i)


