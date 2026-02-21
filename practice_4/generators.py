a=int(input())
g=(i**2 for i in range(1,a+1))
print(*g)
# 2

n = int(input())
g=(i for i in range(n) if i%2==0)

print(*g, sep=",")

# 3
def f(n):
    for i in range(n):
        if(i%3==0 and i%4==0):
            yield i

a=int(input())
for j in f(a):
    print(j)

# 4
a=int(input())
b=int(input())
g=(i**2 for i in range(a,b))
print(*g)
# 5
n=int(input())
g=(i for i in range(n,0,-1))
print(*g)