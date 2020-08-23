import numpy as np

arr = np.arange(50).reshape((10,5))


print(arr)
print()

print(arr.T)
print()

print(np.dot(arr.T,arr))
print()

arr3d = np.arange(50).reshape((5,5,2))
print(arr3d)

print()
print(arr3d.transpose(1,0,2))

arr1 = np.array([[1,2,3]])
print(arr1)
print()
print(arr1.swapaxes(0,1))
