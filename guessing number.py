import random
print("Enter the range of numbers:0-")
n=int(input())
x=random.randint(0,n)
user=int(input("Guess the random number selected by the computer in the given range:"))
i=0
while(i<5):
    if(user>x):
        print("get lower")
        user=int(input())
    elif(user==x):
        print(x,"is the exact number selected")
        break
    else:
        print("get higher")
        user=int(input())
    i=i+1
