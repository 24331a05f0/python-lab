print("Area of the triangle using Heron's formula calculation")
a = float(input("enter side a of the triangle:"))
b = float(input("enter side b of the triangle:"))
c = float(input("enter side c of the triangle:"))
s = (a+b+c)/2
area_heron =(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle using Heron's formula is:",area_heron)