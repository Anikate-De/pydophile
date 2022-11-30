import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print array
print('Array -', array)

# Print array dimensions
print('Dimensions -', array.ndim)

# Print array size
print('Size -', array.size)

# Print array shape
print('Shape -', array.shape)


print('-'*10)

# 2D Array operations
array = np.array([1,2,3,4,5,6,7])

print('2D Array -', array)

oneArray = np.ones(7, dtype=int)

print('array + oneArray -', array + oneArray)

print('array - oneArray -', array - oneArray)

print('array x 18 -', array * 18)

print('array ÷ 7 -', array / 18)

print('array + oneArray * 100 -', array + oneArray * 100)

print('array // 0.6 -', array // 0.6)



# 3D Array operations
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

print('3D Array -\n', array)

oneArray = np.ones((3,3), dtype=int)

print('array + oneArray -\n', array + oneArray)

print('array - oneArray -\n', array - oneArray)

print('array x 6 -\n', array * 6)

print('array ÷ 2 -\n', array / 2)

print('array + oneArray * 10 -\n', array + oneArray * 10)

print('array // 0.5 -\n', array // 0.5)


newArr = np.array([[3,245,323],[234,51,6],[0,82,9]])
print('New Array -\n', newArr)

print('array + newArray -\n', array + newArr)

print('array - newArray -\n', array - newArr)

print('array x newArray -\n', array * newArr)

print('array ÷ newArray -\n', array / newArr)

