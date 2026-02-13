def primeR(num, div=2):
    if num<2:
        return False
    if div >num**0.5:
        return True
    if num % div == 0:
        return False
    return primeR(num,div+1)
n=int(input("enter a number: "))
if primeR(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")