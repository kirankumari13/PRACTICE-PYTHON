import random
a=random.sample(range(100),7)
b=random.sample(range(100),10)
print(a)
print(b)
c=[i for i in a if i in b]
print(c)