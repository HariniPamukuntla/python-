import random
n=random.randint(1,100)
print(n)
while True:
        x=int(input("Enter the number"))
        if x==n:
                print("Successful")
                break
        elif x>n:
                 print("too high")
        else:
                print("too low")
