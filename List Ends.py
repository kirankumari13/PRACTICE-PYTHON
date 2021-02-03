
"""
a = [5, 10, 15, 20, 25]
x=[a[0],a[-1]]
print(x)

a = [5,10,15,20,30]
def list_ends(x):
    return [x[0],x[-1]]

print(list_ends(a))
"""
a = [5, 10, 15, 20, 25]
def list_ends(x):
    return [i for i in a[0::len(a)-1]]
print(list_ends(a))