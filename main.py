# YOUR CODE HERE
updated_list=[]
def summation():
    for i in range(n):
        updated = list1[i]+list2[i]
        updated_list.append(updated) 
    return updated_list

def find_min_max():
    mi = min(updated_list)
    ma = max(updated_list)
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

print(summation())
print(find_min_max())
