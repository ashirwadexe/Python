# # --------------------------------------
# # --------------Tuples------------------
# # --------------------------------------

# # A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# # In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# # --------Characterstics---------
# # Ordered
# # Unchangeble
# # Allows duplicate

# # --------Plan of attack---------
# # Creating a Tuple
# # Accessing items
# # Editing items
# # Adding items
# # Deleting items
# # Operations on Tuples
# # Tuple Functions

# # CREATING A TUPPLE

# # empty
# t1 = ()
# print(t1)

# # how to create a tupple with single item
# t2 = (2) #ye tupple nhi banega balki int ban jaega
# print(t2)
# print(type(t2))
# # to create single item tupple  --> item ke baad comma laga denge
# t3 = (2,) 
# print(t3)
# print(type(t3))
# # htero
# t4 = (1,2,3,[2,4,5],True,"bappy")
# print(t4)
# # tuple
# t5 = (1,2,3,4,5,(6,7))
# print(t5)
# # using type conversion
# t6 = tuple("Hello")
# print(t6)


# # --------Accessing Tuple---------
# # indexing
# t7 = (1,2,3,4,5,6,7,8)
# print(t7)
# print(t7[0])
# print(t7[-1])
# print(t7[5])

# # slicing
# print(t7[0:3])
# print(t7[::-1])
# print(t7[4:7])

# # -----------Editing Items---------
# t8 = (1,2,3,4,5,6,7,8)
# t8[0] = 100 #it will give type error kyoki tupple me kuch edit kr nhi sakte ek baar assign ho jane ke baad

# -----------Adding Items---------
# not possible same reason as editing

# # ----------Deleteing Items-------
# # pure tupple ko delete kr sakte but ek item ko nhi
# t9 = (1,2,3,4)
# del t9
# print(t9)

# # ----------- Operations on Tupple-----------

# # + and *
# t10 = (1,2,3,4)
# t11 = (5,6,7)
# print(t10+t11)
# print(t10*3)

# # membership
# 1 in t10

# # iteration
# for i in t10:
#     print(i)

# # ----------- Functions on Tupple-----------
# t12 = (2,63,2,6,8,4,5,0,9,3)

# # len/sum/min/max/sorted
# print(len(t12))
# print(sum(t12))
# print(min(t12))
# print(max(t12))
# print(sorted(t12, reverse=True))

# # count
# print(t12.count(2))

# # index
# print(t12.index(8))

# --------------DIFFERENCE BW TUPPLE AND LISTS---------------
# syntax diff'
# mutability
# speed - tupple fast since immutabe
# memory - tupple takes less memory
# built in functions - list have more fnt
# error - list is more error prone
# usability - jaha changes nhi chahiye use tupple

# # ------ Tupple Unpacking----------
# a,b,c = (1,2,3) # both side must be equal for unpacking
# print(a,b,c)

# # swap using unpacking
# a = 1
# b = 2
# a,b = b,a
# print(a,b)

# # zipping tupple
# a = (1,2,3,4)
# b = (5,6,7,8)
# zip(a,b) # zip functon ek zip object bana dega
# print(zip(a,b))
# # unzipping
# list(zip(a,b))
# print(list(zip(a,b)))
