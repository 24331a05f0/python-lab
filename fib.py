n=int(input("enter a number:"))
f=0
s=1
print("fibonacci series: ")
for i in range(n):
    print(f, end='')
    next = f+s
    f=s
    s=next