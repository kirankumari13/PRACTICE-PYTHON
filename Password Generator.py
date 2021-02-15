import random
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*"
#password_length=int(input("how strong password do you want?"))
#password="".join(random.sample(s,password_length))
#print(password)
c=0
while True:
    password_length=int(input("how strong password do you want?"))
    password="".join(random.sample(s,password_length))
    print(password)
    c+=1
    if len(password)>= 8:
        print("the password is strong.")
        break
    else:
        if len(password)<8:
         print("the password is weak.please, give a new password.")
        user=input("Do you want to continue? (Y/N):").upper()
        if user=="N":
             break
print(c)