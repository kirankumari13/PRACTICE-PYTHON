a = [1,1,2,5,3,8,9,9,10,]
def remove_dup_v1(x):
    y=[]
    y=[i for i in x if i not in y]
    return y
def remove_dup_v2(x):
    return (list(set(a)))

print(remove_dup_v1(a))
print(remove_dup_v2(a))
