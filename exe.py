def g(n):
    for i in range(n,0,-1):
        yield i
n=int(input())
for j in g(n):
    print(j)