p = int(input("enter the principle amount:"))
r = int(input("enter the rate of interest:"))
n = int(input("enter number of times interest is compounded:"))
t = int(input("enter number of years:"))
a = p * (1 + r / (100 * n)) ** (n * t)
CI = a - p
print(round(CI,2))
