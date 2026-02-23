# 1
a=float(input("Input degree: "))
b=(a/180)*3.141592654
print("Output radian:",round(b,6))

# 2
h=int(input("Height: "))
b=int(input("first value: "))
c=int(input("second value: "))
print("Expected Output:",((c+b)/2)*h)

# 3
pi=3.141592654
def tan(x):
    return x + (x**3)/3
h=int(input("Input number of sides: "))
b=float(input("Input the length of a side "))

area = (h * b**2) / (4 * tan(pi / h))
print("The area of the polygon is:", round(area, 4))

# 4
a=float(input())
b=float(input())
print(a*b)