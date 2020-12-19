import numpy as np

#########################################################
# # BASICS
# a = np.array([1, 3, 6, 9], dtype='int16')
# print(a)
#
# b = np.array([[6, 9, 9], [9, 6, 8]])
# print(b)
#
# # get dimension
# print("Dimension of a is " + str(a.ndim))
# print("Dimension of b is " + str(b.ndim))
#
# # get shape it will show vector
# print(a.shape)
# print(b.shape)
#
# # to get type
# print(a.dtype)
# print(b.dtype)
#
# # get size
# print(a.itemsize)
# print(b.itemsize)
#
# # get number of elements
# print(a.size)
# print(b.size)
#
# # get total size
# print(a.nbytes)         #or
# print(b.size*b.itemsize)
#########################################################################

# Accessing/changing specific ELEMENTS, ROWS, COLUMN,etc
# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a, a.ndim, a.itemsize, a.dtype, a.size, a.shape, a.nbytes)
#
# # get specific elements [r, c] and also python number starts from 0
# print(a[1, 5])
#
# # get a specific row
# print(a[0, :])              # : means all column
#
# # get a specific column
# print(a[:, 2])              # : means all row
#
# # getting little more fancy [row, start index : end index : step size]
# print(a[0, 1:6:2])
#
# # to change elements
# a[1, 5] = 20
# a[:, 2] = [1, 2]
# print(a)
#######################################################################

# # 3-d example
#
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)
#
# # get specific element
# print(b[1, 0, 0])
#
# # replace
# b[:, 1, :] = [[9, 9], [8, 8]]
# print(b)
############################################################

# initializing different types of array
# # all zeros matrix
# a = np.zeros((2, 3))
# print(a)
#
# # all ones matrix
# b = np.ones((4, 2, 2), dtype='int32')
# print(b)
#
# # any other number
# c = np.full((2, 2), 99)
# print(c)
#
# # any other number (full like)
# d = np.full_like(a, 4)              # d = np.full(a.shape, 4)
# print(d)
#
# # Random decimal number
# e = np.random.rand(4, 2)
# print(e)
#
# # Random integer number
# f = np.random.randint(5, 7, size=(3, 3))
# print(f)
#
# # Identity matrix
# g = np.identity(4)
# print(g)
#
# # repeat array
# arr = np.array([[2, 3, 4]])
# r = np.repeat(arr, 3, axis=0)
# print(r)
############################################################

# # questions
# o = np.ones((5, 5))
# # print(o)
#
# z = np.zeros((3, 3))
# # print(z)
# z[1, 1] = 9
# # print(z)
#
# o[1:4, 1:4] = z
# print(o)
########################################################################

# Mathematics
# a = np.array([1, 2, 3])
# b = np.array([2, 4, 7])
# print(a, a+2, a-2, a*2, a/2, a**2, a+b)
#
# # take trigonometry function
# print(np.sin(b), "      ", np.cos(b), "    ", np.tan(b))
#
# # Linear Algebra
# c = np.ones((2, 3))
# d = np.full((3, 2), 2)
# print(np.matmul(c, d))
#
# # find determinant
# e = np.identity(3)
# print(np.linalg.det(e))
#
# # statistics
# stats = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.min(stats))
# print(np.max(stats, axis=1))
# print(np.sum(stats, axis=0))
########################################################################

# # Reorganizing arrays
# before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(before)
#
# after = before.reshape((4, 2))
# print(after)
#
# # Vertically stacking vectors
# v1 = np.array([1, 2, 3, 4])
# v2 = np.array([5, 6, 7, 8])
# print(np.vstack([v1, v2, v1, v2]))
#
# # Horizontal  stack
# h1 = np.ones((2, 4))
# h2 = np.zeros((2, 2))
# print(np.hstack((h1, h2)))
#############################################################################

# Miscellaneous
# Load data from file
filedata = np.genfromtxt('Resources/data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean Masking and Advanced Indexing
print(filedata > 50)
print(filedata[filedata > 50])
print(np.any(filedata > 50, axis=0))
print(((filedata > 50) & (filedata < 100)))
print((~((filedata > 50) & (filedata < 100))))
##############################################################################