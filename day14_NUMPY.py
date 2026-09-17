# # ===============================================
# # ========= NUMPY ARRAY vs PYTHON LITS ==========
# # ===============================================
import numpy as np

# # NOTE: Numpy aaya hi isliye kyoki python ke datatype kafu slow the

# # SPEED --> Python list
# a = [i for i in range(100000000)]
# b = [i for i in range (100000000, 200000000)]

# c = []
# import time

# start = time.time()
# for i in range(len(a)):
#     c.append(a[i] + b[i])

# print(time.time() - start)

# # speed --> numpy array
# a = np.arange(100000000)
# b = np.arange(100000000, 200000000)

# start = time.time()
# c = a+b
# print(time.time()-start)


# # NOTE: Python list takes more memory to while numpy list takes less memory
# # Memory --> python 
# a = [i for i in range(10000000)]
# import sys
# print(sys.getsizeof(a))

# # Memory --> numpy list
# b = np.arange(10000000, dtype=np.int8)
# print(sys.getsizeof(b))

# convenience --> numpy is much better option when we are working in data science project since it takes much less memory and time

# # ===============================================
# # ============== ADVANCE INDEXING ===============
# # ===============================================

# a = np.arange(24).reshape(6,4)
# print(a)

# # Fancy Indexing  --> using this we can get desired row and column

# # row 0,2,3 print krao
# print(a[[0,2,3]])
# # row - 0,2,3,5
# print(a[[0,2,3,5]])
# # column - 0,2,3
# print(a[:, [0,2,3]])

# Boolian Indexing --> more interestiung than other indexing

# abhi tak ham index positions se nikal rhe the items ko
# but ab ham logic implement kr ke items nikalenge
a = np.random.randint(1,100,24).reshape(6,4) # every time we print it will give a new array
print(a)

# # find all numbers greater than 50 from a
# print(a[a > 50]) # only no greater than 50 in a will print others will not

# # find even no
# print(a[a%2==0])

# # find all no greater than 50 and are even
# print(a[(a>50) & (a%2==0)])

# find all numbers not divisble by 7
print(a[a%7!=0])