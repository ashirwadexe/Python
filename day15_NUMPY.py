# # ============================================================
# # ================ NUMPY IMPORTANT FUNCTIONS =================
# # ============================================================

import numpy as np
a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
# print(a)
# print(b)

# # np.sort() --> used to sort an unsorted array and return s sorted aray of an arrray
# # https://numpy.org/doc/stable/reference/generated/numpy.sort.html
# print(np.sort(a))
# print(np.sort(b)) # 2D row-ise sorting
# print(np.sort(b, axis=0)) # 2D column-ise sorting

# # np.append --> The numpy.append() appends values along the mentioned axis at the end of the array
# # https://numpy.org/doc/stable/reference/generated/numpy.append.html
# print(np.append(a, 1000))
# print(np.append(b, np.ones((b.shape[0],1)), axis=1)) # adding a extra colum in 2D array with all items 1

# # np.concatenate --> numpy.concatenate() function concatenate a sequence of arrays along an existing axis.
# # https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html
# c = np.arange(6).reshape(2,3)
# d = np.arange(6,12).reshape(2,3)
# print(c)
# print(d)
# print(np.concatenate((c,d)))


# # np.unique --> With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.
# # https://numpy.org/doc/stable/reference/generated/numpy.unique.html/
# e = np.array([1,2,2,2,3,3,4,4,5,6,7,7,7,8,8,9,0])
# print(np.unique(e))

# # np.expand_dims --> With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array
# # https://numpy.org/doc/stable/reference/generated/numpy.expand_dims.html
# ans = np.expand_dims(a,axis=0).shape  # expandend in row
# print(ans)
# ans = np.expand_dims(a,axis=1) # expanded in colum
# print(ans)


# # np.where ---> The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
# # https://numpy.org/doc/stable/reference/generated/numpy.where.html
# # print(a)
# # print(np.where(a>50))
# # replace all the items > 50 with 0
# # --> np.where(condition, true, false)
# # --> if condition true --> show truthy values and is false show falsy values
# print(np.where(a>50, 0, a))
# # replace all even with zero
# print(np.where(a%2==0, 0, a))


# # np.argmax --> The numpy.argmax() function returns indices of the max element of the array in a particular axis.
# # https://numpy.org/doc/stable/reference/generated/numpy.argmax.html
# print("Larget no is at index: ", np.argmax(a))
# print(b)
# print("Largets no is at index: ", np.argmax(b, axis=1), "in each row")
# print("Largets no is at index: ", np.argmax(b, axis=0), "in each column")


# # np.argmin() --> gives the index of smalletst item in a particular axis
# print(np.argmin(a))
# print(b)
# print("Smallest item is at index: ", np.argmin(b, axis=1), "in each row")
# print("Smallest item is at index: ", np.argmin(b, axis=0), "in each column")


# # np.cumsum ---> numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.
# # https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html
# # cumulative sum --> A cumulative sum is a sequence of partial sums where each value adds up all previous values in a data set up to that point. It is also known as a running total.
# print(a)
# print("Cummulative sum: ", np.cumsum(a))
# # 2D array
# print("Cummulative sum on each row: \n", np.cumsum(b, axis=1))
# print("Cummulative sum on each column: \n", np.cumsum(b, axis=0))

# # np.cumprod() --> A cumulative product is a sequence of running multiplications where each element in an output array or series represents the product of all previous elements up to that point
# print("Cummulative product: ", np.cumprod(a))
# # 2D array
# print("Cummulative product on each row: \n", np.cumprod(b, axis=1))
# print("Cummulative product on each column: \n", np.cumprod(b, axis=0))


# # np.percentile ---> numpy.percentile()function used to compute the nth percentile of the given data (array elements) along the specified axis.
# # https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
# print(a)
# print(np.percentile(a,100))
# print(np.percentile(a,50))
# print(np.median(a))


# # np.histogram ---> Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.
# # https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
# print(np.histogram(a, bins=[0,10,20,30,40,50,60,70,80,90,100]))


# # np.corrcoef ---> Return Pearson product-moment correlation coefficients.
# # https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html
# salary = np.array([20000,40000,25000,35000,60000])
# experience = np.array([1,3,2,4,2])
# print(np.corrcoef(salary, experience))


# # np.isin ---> With the help of numpy.isin() method, we can see that one array having values are checked in a different numpy array having different elements with different sizes.
# # https://numpy.org/doc/stable/reference/generated/numpy.isin.html
# # np.isin() --> ye multiple items ko array me search kr kre batata hia vo hia ya nhi hai
# print(a)
# item = [10,20,30,4,50,60,70,80,90,100]
# print(np.isin(a, item))
# print(a[np.isin(a, item)])


# # np.flip ---> The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.
# # https://numpy.org/doc/stable/reference/generated/numpy.flip.html
# print(a)
# print(np.flip(a))
# print(b)
# print(np.flip(b))


# # np.put ---> The numpy.put() function replaces specific elements of an array with given values of p_array. Array indexed works on flattened array.
# # https://numpy.org/doc/stable/reference/generated/numpy.put.html
# # changes in original anrray and its permanent
# print(a)
# np.put(a, [0,1,2,3,4], [111,222,333,444,555])
# print(a)


# # np.delete ---> The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.
# # https://numpy.org/doc/stable/reference/generated/numpy.delete.html
# print(a)
# print(np.delete(a,[0,1,2,3,4,5,6,7]))
# # delete in 2D also by passing axis=0 for colum or axis=1 for row
# print(b)
# print(np.delete(b, [0], axis=1)) # row 1 deleted


# =========== Set functions ==============

# np.union1d
# np.intersect1d
# np.setdiff1d
# np.setxor1d
# np.in1d


# # np.clip ---> numpy.clip() function is used to Clip (limit) the values in an array.
# # https://numpy.org/doc/stable/reference/generated/numpy.clip.html
# # it will limit the items in array like here values will only vary between min-25 to max-75
# print(a)
# print(np.clip(a,a_min=25,a_max=75))


