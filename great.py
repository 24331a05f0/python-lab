x,y,z=map(int,input("enter 3 numbers :").split())
choice  =input("enter choice min/max :")
if choice == "min":
    if x<y and x<z:
        print(f"{x}if smallest")
    elif y<z:
        print(f"{y}is smallest")
    else :
        print(f"{z}is smallest")
    
else:
    if x>y and x>z:
        print(f"{x}if greatest")
    elif y>z:
        print(f"{y}is greatest")
    else :
        print(f"{z}is geratest")