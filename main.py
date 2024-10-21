# YOUR CODE HERE
updated_list=[]
def summation(a,b):
    for i in range(n):
        updated = a[i]+b[i]
        updated_list.append(updated) 
    return updated_list

def find_min_max(a):
    mi = min(a)
    ma = max(a)
    return mi, ma

n = int(input())
list1 = []
list2 = []
for i in range(n):
    z = int(input())
    list1.append(z)
for i in range(n):
    x = int(input())
    list2.append(x)

print(summation(list1,list2))
print(find_min_max(updated_list))
