# 1. Generator of squares from 1 to a
def squares(N):
    for i in range(N + 1):
        yield i * i

n = int(input())

for num in squares(n):
    print(num) 

# 2. Generator of even numbers from 0 to n-1
def g(n):
    for i in range(n):
        if i%2==0:
            yield i
a= int(input())
for j in g(a):
    print(j)
# 3. 
def f(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0: 
            yield i  # yield produces a generator value

a = int(input()) 
for j in f(a):  # Iterate through the generator
    print(j) 

# 4. 
def g(a,b):
    for i in range(a,b):
        yield i**2
a= int(input())
b=int(input())
for j in g(a,b):
    print(j)

# 5. 
def g(n):
    for i in range(n,0,-1):
        yield i
n=int(input())
for j in g(n):
    print(j)