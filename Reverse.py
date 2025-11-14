#with extra memory
def reverse(list):
    list2=[]
    for i in range(len(list)-1,-1,-1) :
        list2.append(list[i])
    return list2

def reverseOptimize(list) :
    i=0
    j=len(list)-1
    while i<j :
        list[i],list[j]=list[j],list[i]
        i=i+1
        j=j-1

    return list


print(reverse([1,2,3,4,5,6,7,8]))
print(reverseOptimize([1,5,7,8]))


