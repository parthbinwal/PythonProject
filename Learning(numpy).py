import numpy as np
#array and basic
#creating array
arr=np.array([1,2,4,6,4,3])
print(arr,"1d array")
arr2d=np.array([[1,4,5,6],[3,5,9,0]])#dimension should be same else error
print(arr2d,"2d aarray")
#list vs array while multi;
list=[1,2,3,4,5,6]
print(list*2)
print(list)
print(arr*2)
#creating array from scratch
zeroes=np.zeros((3,4))
print(zeroes)
ones=np.ones((2,2))
print(ones)
#any value array
full=np.full((3,3),7)#1st argument size of matrix second value
print(full)
#random value array
ran=np.random.random((2,3))
print(ran)
#range
seq=np.arange(0,10,2)
print(seq)
#vector matrix,tensor
vector=np.array([1,3,5,7,9])
print(vector,"vector")
matrix=np.array([[1,2,3],[4,5,6]])
print(matrix,"matrix")
tensor=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(tensor)
#prop of array
array=np.array([[1,2,3],[4,5,6]])
print("shape",array.shape)
print("dimesnion",array.ndim)
print("size",array.size)
print("Dtype",array.dtype)


