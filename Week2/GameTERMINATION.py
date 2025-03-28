import random
n=random.randint(1,100)
count=4
print(n)
while count >0 :
    x=int(input("Enter the number"))
    if x==n:
       print("Successful")
       break
    elif x>n:
       print("too high")
    else:
        print("too low")
    count = count - 1
print("YOU LOST,try again")
               
