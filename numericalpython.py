import numpy as np
"""a=np.array([1,2,3])
b=np.array([[1,2],[3,4]])
print(np.zeros((2,3)))
print(np.ones((3,2)))
print(np.eye(3))
print(np.full((2,2),7))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
#Array atributes
arr=np.array([[1,2],[3,4]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)
#indexing and slicing
arr=np.array([[1,2],[3,4]])
print(arr[0,1])
print(arr[:,1])
print(arr[1,:])
#mathematical operations
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)
print(np.dot(a,b))
print(np.mean(a))
print(np.std(b))
print(np.sum(a))
print(np.max(b))
#reshaping and flattening
arr=np.array([[1,2],[3,4]])
print(arr.reshape(4,1))"""
# broadcasting 
a=np.array([[1],[2],[3]])
b=np.array([10,20,30])
print(a+b)

