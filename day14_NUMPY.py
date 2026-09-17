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

