# 1
N = int(input())
sq = (x * x for x in range(N))
for i in sq:
    print(i)

# 1.1
def sq(N):
    n = 0
    while n < N:
        yield n * n
        n += 1

    
lsq = sq(5)
for n in lsq:
    print(n)


# 2
def even_nums(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input())
en = even_nums(n)
for i in en:
    print(f"{i},", end = " ")


# 3

def div12(n):
    i = 0
    while i <= n:
        if i % 12 == 0:
            yield i
        i += 1
    

l = div12(100)
for i in l:
    print(f"{i},", end = " ")


# 4

a = int(input())
b = int(input())

squares = (x * x for x in range(a, b))

for i in squares:
    print(f"{i},", end = " ")


# 5

def nto0(n):
    i = n
    while i >= 0:
        yield i
        i -= 1

e = nto0(10)
for i in e:
    print(i)


