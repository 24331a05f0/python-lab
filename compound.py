princ_amt=float(input("enter principal amout:"))
rate=float(input("enter rate of interest:"))
time=float(input("enter time in year:"))
compd_interest=princ_amt*((1+rate/100)**time)-princ_amt
print("compound interest is:",compd_interest)