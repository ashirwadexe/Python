# # ------------------------------------------
# # ------------------LIST--------------------
# # ------------------------------------------

# # List is a datatype where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.

# L = [20, 'Jessa', 35.43]

# # ARRAYS Vs LIST
# # 1. Fixed size-array vs dynamic size-array
# # 2. Conviniance in list because can add multiple data type in a single list but cant do the same in a    array -> so list is hetrogenious.
# # 3. Speed of execution is slow as compared to array.
# # 4. List occupies more space in memory as compared to array.

# # HOW LIST STORED IN MEMORY ?
# # stored in a referencial aaray or like pointers in C.
# # id() prints the memory address of data
# L = [1,2,3]
# print(id(L[0]))
# print(id(L[1]))
# print(id(L[2]))

# # CHARACTERISTICS OF LIST
# # Ordered
# # Changable/mutable
# # hetrogenous
# # can gave duplicates
# # are dynamic
# # items can be accessed
# # can contain any kind of objects in python

# # CREATING A LIST
# print([]) #empty list
# print([1,2,3,4,5]) #1D list
# print([1,2,3, [4,5]]) #2D list
# print([1,2,[3,4,[5,6,7]]]) #3D list
# print([1,2,4.55,(4+3j), "Bappy"]) #hetrogenous list
# print(list('Hello')) #type conversion

# # ACCESSING ITEMS FORM LIST
# # Indexing
# A = [1,2,3,4,5,6]
# print(A[0]) #positive indexing
# print(A[-1]) #negative indexing - ye right se access krna start krta hai

# B = [1,2,3,[4,5]] 
# print(B[3])
# print(B[3][0])
# print(B[3][1])

# C = [[[1,2],[3,4],[[5,6],[7,8]]]]
# print(C[0][0][1])
# print(C[0][0][0])

# # SLICING - jab ek sath multiple item nikalne ho list se
# print(A[2:5])
# print(A[::-1]) #to reverse the list

# # ADDING ITEMS TO A LIST
# # 1. Append Function - it adds only 1 item
# A.append(7)
# print(A)

# # 2. Extend Function - it adds multiple items
# A.extend([8,9,10])
# print(A)

# A.extend('Delhi')
# print(A)

# # 3. Insert Function - add item at desired location
# A.insert(2, 100) #2-index, 100-item to be added at index 2
# print(A)

# # EDITING EXISTING ITEMS IN A LIST

# A = [1,2,3,4,5]
# A[2] = 500
# print(A)

# A[1:3] = ['A','B','C']
# print(A)

# DELETING ITEMS FROM A LIST
# del
B = [1,2,3,4,5,6,7,8]
# del B
# print(B)
# del B[0]
# print(B)

# remove - delete the data from its value and not index
# B.remove(5)
# print(B)

# pop - iska default behaviour hai last item ko delete krna if idex not pass in parameter
# B.pop()
# print(B)

# clear - list ko empty kr deta hai
B.clear()
print(B)