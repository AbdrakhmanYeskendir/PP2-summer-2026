from functools import reduce

print("1. Use map() and filter() on lists")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prices = [100, 250, 330, 490, 580, 1150]

doubled_numbers = list(map(lambda number: number * 2, numbers))
high_prices = list(filter(lambda price: price > 500, prices))

print("doubled numbers:", doubled_numbers)
print("high prices:", high_prices)


print("\n2. Aggregate with reduce() (from functools)")

# Initial value is 10, so result will be 10 + sum(numbers)
total = reduce(lambda n, m: n + m, numbers, 10)
print("total:", total)


print("\n3. Use enumerate() and zip() for paired iteration")

products = ["Monster energy drink", "Marlboro Red", "Yamaha R6"]
prices = [900, 1150, 4000000]

for index, product in enumerate(products, start = 1):
    print(f"{index}.{product}")

catalog = []

for product, price in zip(products, prices):
    catalog.append({
        "product": product,
        "price": price
    })

print(catalog)


print("\n4. Demonstrate type checking and conversions")

n = 19
float_n = float(n)

print("int:", n)
print("float:", float_n)

print(type(n))
print(type(float_n))

print(isinstance(n, int))

str_n = str(n)
bool_n = bool(n)

print("string:", str_n)
print("bool:", bool_n)

print(type(str_n))
print(type(bool_n))
