# # # ===============================================
# # # ========= NUMPY ARRAY vs PYTHON LITS ==========
# # # ===============================================
# import numpy as np

# # # NOTE: Numpy aaya hi isliye kyoki python ke datatype kafu slow the

# # # SPEED --> Python list
# # a = [i for i in range(100000000)]
# # b = [i for i in range (100000000, 200000000)]

# # c = []
# # import time

# # start = time.time()
# # for i in range(len(a)):
# #     c.append(a[i] + b[i])

# # print(time.time() - start)

# # # speed --> numpy array
# # a = np.arange(100000000)
# # b = np.arange(100000000, 200000000)

# # start = time.time()
# # c = a+b
# # print(time.time()-start)


# # # NOTE: Python list takes more memory to while numpy list takes less memory
# # # Memory --> python 
# # a = [i for i in range(10000000)]
# # import sys
# # print(sys.getsizeof(a))

# # # Memory --> numpy list
# # b = np.arange(10000000, dtype=np.int8)
# # print(sys.getsizeof(b))

# # convenience --> numpy is much better option when we are working in data science project since it takes much less memory and time

# # # ===============================================
# # # ============== ADVANCE INDEXING ===============
# # # ===============================================

# # a = np.arange(24).reshape(6,4)
# # print(a)

# # # Fancy Indexing  --> using this we can get desired row and column

# # # row 0,2,3 print krao
# # print(a[[0,2,3]])
# # # row - 0,2,3,5
# # print(a[[0,2,3,5]])
# # # column - 0,2,3
# # print(a[:, [0,2,3]])

# # # Boolian Indexing --> more interestiung than other indexing

# # # abhi tak ham index positions se nikal rhe the items ko
# # # but ab ham logic implement kr ke items nikalenge
# # a = np.random.randint(1,100,24).reshape(6,4) # every time we print it will give a new array
# # print(a)

# # # find all numbers greater than 50 from a
# # print(a[a > 50]) # only no greater than 50 in a will print others will not

# # # find even no
# # print(a[a%2==0])

# # # find all no greater than 50 and are even
# # print(a[(a>50) & (a%2==0)])

# # # ==================================================
# # # =============== BRAODCASTING =====================
# # # ==================================================

# # # The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.
# # # The smaller array is “broadcast” across the larger array so that they have compatible shapes.
# # # NOTE: broadcasting tab use hota hia jab do arrays pe arithmetic op ho or dono ka shape different ho --> normally ye op error dega but numpy me broadcasting isko kr dega

# # # same shape
# # a = np.arange(6).reshape(2,3)
# # b = np.arange(6,12).reshape(2,3)
# # print("a -", a)
# # print("b -", b)
# # print(a+b)

# # # different shape
# # a = np.arange(6).reshape(2,3)
# # b = np.arange(3).reshape(1,3)
# # print("a -", a)
# # print("b -", b)
# # print(a+b)

# # Broadcasting Rules
# # 1. Make the two arrays have the same number of dimensions.
# #   --> If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.
# #   --> 1D + 1D, 2D + 2D, 3D + 3D

# # 2. Make each dimension of the two arrays the same size.
# #   --> If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# #   --> If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.

# # # More examples - 1

# # a = np.arange(12).reshape(4,3)
# # b = np.arange(3)
# # print(a)
# # print(b)

# # print(a+b)

# # # ex - 2
# # a = np.arange(12).reshape(3,4)
# # b = np.arange(3)

# # print(a)
# # print(b)
# # # print(a+b)   # this will not broadcast with this shape

# # # ex - 3
# # a = np.arange(3).reshape(1,3)
# # b = np.arange(3).reshape(3,1)

# # print(a)
# # print(b)
# # print(a+b)

# # # ex - 4
# # a = np.arange(3).reshape(1,3)
# # b = np.arange(4).reshape(4,1)

# # print(a)
# # print(b)

# # print(a + b)

# # # ex - 5
# # a = np.array([1])
# # # shape -> (1,1)
# # b = np.arange(4).reshape(2,2)
# # # shape -> (2,2)

# # print(a)
# # print(b)

# # print(a+b)

# # # ex - 6
# # a = np.arange(12).reshape(3,4)
# # b = np.arange(12).reshape(4,3)

# # print(a)
# # print(b)

# # print(a+b)



# # # ==================================================
# # # ====== Working with Mathematical Formulas ========
# # # ==================================================

# # # numpy has built-in mathematical formulas
# # a = np.arange(10)
# # print(np.sum(a))

# # # how to calculate a mathematical function which is not in numpy

# # # ==> SIGMOID
# # def sigmoid(array):
# #     return 1/(1 + np.exp(-(array)))

# # a = np.arange(10)
# # print(sigmoid(a))

# # # ==> mean squared error -- Mean Squared Error (MSE) measures the average squared difference between a model's predicted values and the actual observed values.

# # actual = np.random.randint(1,50,25)
# # predicted = np.random.randint(1,50,25)

# # def mse(actual, predicted):
# #     return np.mean((actual - predicted)**2)

# # ans = mse(actual, predicted)
# # print("MSE: ", ans)

# # Binary cross entropy


# # # ==================================================
# # # ========= Working with misiing values ============
# # # ==================================================

# # # np.nan() --> here we are using np.nan() -> to detect empty no and remove then using not(~)
# # a = np.array([1,2,3,4,np.nan,6])
# # print(a[~np.isnan(a)])

# # # ========================================
# # # ========= Plotting Graphgs =============
# # # ========================================

# # # matplotlib -- libarary will use to plot graphs
# # # NOTE: matplotlib is library in python which is used to plot or create graph using there formulas or functions

# # # Plotting a 2D graph
# # # x = y --> line from origin 

# # import matplotlib.pyplot as plt
# # x = np.linspace(-10,10, 100)
# # y = x

# # plt.plot(x,y)
# # plt.show()  # --> to show the graph using matplotlib

# # # y = x**2
# # x = np.linspace(-10,10,100)
# # y = x**2
# # plt.plot(x,y)
# # plt.show()

# # # y = sin(x)
# # x = np.linspace(-10,10,100)
# # y = np.sin(x)
# # plt.plot(x,y)
# # plt.show()

# # # y = xlog(x)
# # x = np.linspace(-10,10,100)
# # y = x * np.log(x)
# # plt.plot(x,y)
# # plt.show()

# # # sigmoid
# # x = np.linspace(-10,10,100)
# # y = 1 / (1 + np.exp(-x))
# # plt.plot(x,y)
# # plt.show()



