import random
a= random.randint(1,10)
print(a)
c=0
while True:

    user=int(input("please give a number between (1,9): "))
    c=c+1
    if a==user:
        print("guess is right")
        break
    else:
        if user<a:
            print("the guess is too low ")
        
        elif user>a:
            print("the guess is too high")
            
        x=input("Do you want to continue? (Y/N):").upper()
        if x=="N":
            break
        
print(c) 
