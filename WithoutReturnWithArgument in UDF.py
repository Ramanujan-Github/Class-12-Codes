#without_return_with_arg

import math
from math import pi
def area(a):
    s=a**2
    print(s)
def volumeofcube(d):
    t=d**3
    print(t)
def TSA(y,z,h):
    b=2*((y*z)+(h*z)+(y*h))
    print(b)
def volumeofcone(r,height):
    w=(1/3)*pi*r*height
    print(w)
print("Write a program implementing user defined functions of four different types with menu as \n1. Area of square\n2. Volume of a cube\n3. Total surface area of cuboid\n4. Volume of a cone\n5. Exit")
x=True
while x==True:
    ch=int(input())
    if ch==1:
        a=int(input())
        area(a)
        s=True
    elif ch==2:
        d=int(input())
        volumeofcube(d)
        s=True
    elif ch==3:
        y=int(input())
        z=int(input())
        h=int(input())
        TSA(y,z,h)
        s=True
    elif ch==4:
        r=int(input())
        height=int(input())
        volumeofcone(r,height)
        s=True
    else:
        s=False
        break