import math
x1=float(input("enter x1 co-ordinatess"))
y1=float(input("enter y1 co-ordinates"))
x2=float(input("enter x2 co-ordinates"))
y2=float(input("enter y2 co-ordinates"))
b=x2-x1
h=y2-y1
d=math.sqrt((b**2)+(h**2))
print("distance =",d)
