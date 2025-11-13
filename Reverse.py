def reverse(list):
    list2=[]
    for i in range(len(list)-1,-1,-1) :
        list2.append(list[i])
    return list2


print(reverse([1,2,3,4,5,6,7,8]))


