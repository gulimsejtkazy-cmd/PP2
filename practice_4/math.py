# 1
import math
a=float(input("Input degree: "))
pi=math.pi
b=(a/180)*pi
print("Output radian:",round(b,6))

# 2
h=int(input("Height: "))
b=int(input("first value: "))
c=int(input("second value: "))
print("Expected Output:",((c+b)/2)*h)

# 3
import math
pi=math.pi
n=int(input("Input number of sides: "))
a=int(input("Input the length of a side: "))
tan=math.tan(pi/n)
x=(n*(a**2))/(4*tan)
print("The area of the polygon is: ",round(x))#round(b,6) — rounds a number to 6 decimal places.

# 4
a=float(input("Length of base: "))
b=float(input("Height of parallelogram: "))
print("Expected Output:",a*b)