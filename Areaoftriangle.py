import math
a=int (input("Enter first side: "))
b=int (input("Enter second side: "))
c=int (input("Enter third side: "))
s=(a+b+c)/2
print("THe semi perimetter is", s)
Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of triangle with 3 sides is", Area)