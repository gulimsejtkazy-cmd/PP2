# 1. Generator of squares from 1 to a
a = int(input()) 
g = (i**2 for i in range(1, a+1)) 
print(*g)  

# 2. Generator of even numbers from 0 to n-1
n = int(input()) 
g = (i for i in range(n) if i % 2 == 0)  # Generator: all i from 0 to n-1 where i is even
print(*g, sep=",")  


# 3. 
def f(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0: 
            yield i  # yield produces a generator value

a = int(input()) 
for j in f(a):  # Iterate through the generator
    print(j) 

# 4. 
a = int(input()) 
b = int(input()) 
g = (i**2 for i in range(a, b))  # Generator expression: squares of numbers from a to b-1
print(*g) 

# 5. 
n = int(input())  
g = (i for i in range(n, 0, -1))  # Generator: numbers from n down to 1 (step -1)
print(*g) 