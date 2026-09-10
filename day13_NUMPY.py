# # ===============================================
# # ==================== NUMPY ====================
# # ===============================================
import numpy as np

# # --------- What is numpy? --------------
 
# # NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

# # At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types

# # --------- Numpy Arrays Vs Python Sequences ------------------
# #   --> NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.
# #   --> The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.
# #   --> NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.
# #   --> A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays.


# # CREATING NUMPY ARRAYS
# a = np.array([1,2,3,4])
# print(a)
# print(type(a))

# # 2D array
# b = np.array([[1,2],[3,4],[5,6]])
# print(b)

# # 3D array
# c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(c)

# # dtype
# d = np.array([1,2,3],dtype=complex)
# print(d)
# print(type(d))

# # np.arange --> it will create an array with range 1 to 10
# e = np.arange(1,11)
# print(e)

# # with reshape(rows, columns) --> it will convert the 1D array into 2D and 3D array 
# f = np.arange(1,11).reshape(5,2)
# print(f)
# f1 = np.arange(1,11).reshape(2,5)
# print(f1)

# # np.ones(length) and np.ones((rows,columns)) --> isko use kr ke ham ek np.array bana sakte hai on the go jiske sare items 1 honge
# g = np.ones(10)
# print(g)
# g1 = np.ones((3,4))
# print(g1)

# # np.zeros(length) and np.zeros((rows,columns)) --> isko use kr ke ham on th go me ek np.array bana sakte h jiske sare items zero honge
# h = np.zeros(10)
# print(h)
# h1 = np.zeros((3,4))
# print(h1)

# # np.random(length) and np.random((rows,colums))
# i = np.random.random(10)
# print(i)
# i1 = np.random.random((4,4))
# print(i1)

# # NOTE: np.ones, np.zeros, np.random.random --> iska use ham krte hia array ko initialize krne ke liye

# # np.linspace - lineraly spaces --> np.linespace(lower range, higher range, number of items want to generate)
# # ye jo array generate krega uske 2 items ka distance equal hoga
# j = np.linspace(-10,10,10)
# print(j)

# # np.identity --> we can create identity matrix using it
# k = np.identity(7)
# print(k)



# # ============ ARRAY ATTRIBUTES ================
# a1 = np.arange(10)
# a2 = np.arange(12, dtype=float).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# # ndim --> no. of dimentions
# print(a1.ndim)
# print(a2.ndim)
# print(a3.ndim)

# # shape --> it will tell the shape of array and give the  number of rows and colums or axis of 3d
# print(a1.shape)
# print(a2.shape)
# print(a3.shape)

# # size --> no of items kitne hian
# print(a1.size)
# print(a2.size)
# print(a3.size)

# # itemsize --> ye batata hai ki har item memory me kitna size occupy kr raha hai 
# print(a1.itemsize)
# print(a2.itemsize)
# print(a3.itemsize)

# # dtype --> items ka datatype kya hai ?
# print(a1.dtype)
# print(a2.dtype)
# print(a3.dtype)


# # ================ CHANGING DATATYPE =====================

# # astype --> 
# print(a3.astype(np.int32))

# # ================ ARRAY OPERATIONS =====================
# a4 = np.arange(12).reshape(3,4)
# a5 = np.arange(12,24).reshape(3,4)

# # SCALAR OPERATION
# # arithmetic
# print(a4 * 2)
# print(a4 + 2)
# print(a4 - 2)
# print(a4 / 2)

# # realtional
# print(a2 > 5)
# print(a2 < 5)
# print(a2 == 5)

# # VECTOR OPERATIONS
# # arithmetic
# print(a4 + a5)
# print(a4 - a5)
# print(a4 * a5)
# print(a4 / a5)

# # MATHEMATICAL OPERATIONS

# a6 = np.random.random((3,3))
# a6 = np.round(a6*100)

# # min/max/sum/prod
# print(np.max(a1))
# print(np.min(a1))
# print(np.sum(a1))
# print(np.prod(a1))

# # to find min/max/sum/prod of each row and column --> 0 - col and 1 - row
# print(np.max(a6, axis=0))
# print(np.max(a6, axis=1))

# # STATISTICAL OPERATIONS
# # mean/median/std/var
# print(np.mean(a6)) 
# print(np.median(a6)) 
# print(np.std(a6)) 
# print(np.var(a6)) 

# # TRIGNOMETRIX FUNCTIONS
# print(np.sin(a6))
# print(np.cos(a6))
# print(np.tan(a6))

# # DOT PRODUCT
# # 1st matrix ka col or 2nd ka row match hona chahiye
# # resultant matrix ka shape 1st ke row or 2nd ke col ke size ka hoga
# a7 = np.arange(12).reshape(3,4)
# a8 = np.arange(12,24).reshape(4,3)

# print(np.dot(a7,a8))

# # LOG AND EXPONENT
# print(np.log(a6))
# print(np.exp(a6))

# # round/floor/ceil
# print(np.round(np.random.random((2,3))*100)) # nearest int
# print(np.floor(np.random.random((2,3))*100)) # piche wale int pe daal dega
# print(np.ceil(np.random.random((2,3))*100)) # aage wale int pe daal dega


# # INDEXING AND SLICING

# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# # indexing
# print(a1)
# print(a1[-1]) # last item
# print(a1[0]) #item at index 0

# # indexing in 2D array
# print(a2)
# print(a2[1,2]) # 6
# print(a2[2,0]) # 4

# # indexing in 3D array
# print(a3)
# print(a3[1,0,1]) # 5 --> a3[which array, row, col]
# print(a3[0,1,1]) # 3
# print(a3[0,0,0]) # 0

# # SLICING

# print(a1[0:5])
# print(a1[2:5])
# print(a1[::-1])

# # slicing in 2D array
# print(a2[0,:]) # row 0
# print(a2[1,:]) # row 1
# print(a2[2,:]) # row 2
# print(a2[:,0]) # col 0
# print(a2[1:,1:3])
# print(a2[::2,::3])

# # slicing in 3D array
# a3 = np.arange(27).reshape(3,3,3)
# print(a3)
# print(a3[1])
# print(a3[::2])

# # ITERATING
# for i in a1:
#     print(i)

# for i in np.nditer(a2):
#     print(i)

# for i in np.nditer(a3):
#     print(i)

# # ============ RESHAPING ===============

# # reshape
# # transpose --> row to col and col to row
# print(np.transpose(a2))
# print(a2.T)

# # ravel --> converts n-dimention array into 1D array
# print(a3.ravel())

# # =========== STACKING ============
# ab1 = np.arange(12).reshape(3,4)
# ab2 = np.arange(12,24).reshape(3,4)

# # horizontal stacking
# print(np.hstack((ab1,ab2)))

# # vertical stacking
# print(np.vstack((ab1,ab2)))

# # ============= SPLITTING ===============
# ab1 = np.arange(12).reshape(3,4)
# ab2 = np.arange(12,24).reshape(3,4)

# # horizontal splitting
# print(np.hsplit(ab2,4))
# # vertical splitting
# print(np.vsplit(ab1, 3))
# # NOTE: stacking or splitting ke liye dono arrays ka shape same hona chahiye

