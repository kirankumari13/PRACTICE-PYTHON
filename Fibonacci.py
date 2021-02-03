n=int(input("give a number:"))
'''
a=1
b=0
x=[]
for i in range(n):
    c=a+b
    x.append(c)
    a=b
    b=c
print(x)
'''
def fib(a,b):
    k=[]
    for i in range(n):
        c=a+b
        k.append(c)
        a=b
        b=c
    print(k)
fib(1,0)