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

# # -----------Adding Items---------
# # not possible same reason as editing

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

# # --------------DIFFERENCE BW TUPPLE AND LISTS---------------
# # syntax diff'
# # mutability
# # speed - tupple fast since immutabe
# # memory - tupple takes less memory
# # built in functions - list have more fnt
# # error - list is more error prone
# # usability - jaha changes nhi chahiye use tupple

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


# # -------------------------------------
# # ------------Sets---------------------
# # -------------------------------------

# # A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# # However, a set itself is mutable. We can add or remove items from it.
# # Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# # ------------Characterstics:---------------
# # Unordered
# # Mutable - can be changed
# # No Duplicates
# # Can't contain mutable data types

# # --------Creating a Set-----------

# # empty
# s = {} # ye kabhi set nhi banega dicationary banega
# s = set() # this is an empty set
# print(s)
# print(type(s)) 

# # 1D and 2D
# s1 = {1,2,3}
# print(s1)
# # s2 = {1,2,3,{4,5}} # error cant make 2d set

# # home and hetro set
# s3 = {1,'hello', 4.5, True}
# print(s3) 
# # True output me nhi de raha - since true =1 and 1 is already there and set doesnt allow dplicates
# # sets are unordered therefore hashing is deciding positiosn of items

# # using type c0onversion
# s4 = set([1,2,3])
# print(s4)

# # duplicates note allowed
# s5 = {1,1,2,2,2,3,3,3,3,3}
# print(s5)

# # set cant have mutable items
# # s6 = { 1,2,[3,4]} # since it is mutable

# # ---------ACCESSING ITEM IN SETS---------
# # indexing and slicing i not allowed since it is unordered
# # can access items but whole set only

# # ---------EDITING ITEM IN SETS---------
# # not allowed same as accessing

# # ---------ADD ITEM IN SETS--------- 
# s7 = {1,2,3,4}
# s7.add(5) # this add position will be decided by hashing
# print(s7)

# # ---------UPDATE ITEM IN SETS--------- 
# s7.update([6,7,8]) # it will add multiple items at once

# # ---------DELETE ITEM IN SETS--------- 
# s8 = {1,2,3}
# del s8
# # print(s8)

# s9 = {1,2,3,4,5}
# s9.discard(3) # it deletes an item from set
# print(s9)

# s9.remove(5) # same as discard but it will throm error if item not found
# print(s9)

# s9.pop() # it will randomly delete an item
# print(s9)

# s9.clear() # it will clear the whole set
# print(s9)

# # -------------SET OPERATIONS---------------
# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7,8,9,10}
# # UNION (|)
# print(s1 | s2)

# # INTERSECTION (&)
# print(s1 & s2)

# # DIFFERENCE (-)
# print(s1 - s2) # s1 me s2 ka jo bhi nhi h vo sab print ho jaega
# print(s2 - s1)

# # SYMMETRIC DIFFERENCE (^) - common ko chod ke sab kuch print ho jaega
# print(s1 ^ s2)

# # MEMBERSHIP TEST
# print(6 not in s2)

# # ITERATION
# for i in s1:
#     print(i)


# # -------------SET Functions---------------

# # LEN/MIN/MAX/SUM/SORTED
# s1 = {1,2,3,4,5,6,7}
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sum(s1))
# print(sorted(s1, reverse=True))

# s1 = {1,2,3,4,5}
# s2 = {3,4,5,6,7,8,9,10}
# # UNION/UPDATE
# print(s1.union(s2)) #same as s1 | s2
# print(s1.update(s2)) #isme ham s2 ki value s1 me daal rhe hai but s2 same rahega but s1 me s2 merge ho jaega

# # INTERSECTION/INYERSECTION_UPDATE
# print(s1.intersection(s2))
# print(s1.intersection_update(s2))

# # DEFFERENCE/DIFFERENCE_UPDATE
# print(s1.difference(s2))
# print(s1.difference_update(s2))

# # SYMMETRIC_DIFFERENCE/SYMMENTRIC_DIFFERENCE_UPDATE
# print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference_update(s2))

# # ISDISJOINT/ISSUBSET/ISSUPERSET
# s3 = {1,2,3,4}
# s4 = {3,4}

# print(s3.isdisjoint(s4)) #disjoint set vo sets hote h jinme kuch bhi common na ho
# print(s3.issubset(s4)) #subset set vo hota hai jsime dusra set pahle ke andar aa jata ahi
# print(s4.issubset(s3)) #subset set vo hota hai jsime dusra set pahle ke andar aa jata ahi
# print(s3.issuperset(s4)) #superset me dusra set pahle ke andar pura aa jata hai

# # -------FROZEN SET--------------
# # Frozen set is just an immutable version of python set

# # creating frozen set
# fs = frozenset([1,2,3,4])
# print(fs)

# # What does work and what not ?
# # all functions of set will work 
# # doesnt work -> write operations(add, delete, update, edit)

# # SET COMPREHENSION
# fs = {i for i in range(1,11) if i%2==0}
# print(fs)



# # ======================================
# # ============DICTIONARY================
# # ======================================

# # Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.
# # In some languages it is known as map or assosiative arrays.

# # dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# # Characterstics:

# # Mutable
# # Indexing has no meaning
# # keys can't be duplicated
# # keys can't be mutable items

# # -------------CREATING A DICTIONARY---------------

# d = {} #empt
# print(d)

# d1 = {'name': 'Ashirwa','gender': 'Male'} #1d homo
# print(d1)

# d2 = {(1,2,3):1, 'hello':'world'} #1d hetro
# print(d2)

# # 2D - JSON follows dictionary
# d3 = {
#     'name':'Ashirwad',
#     'collage': 'IGNOU',
#     'sem': 2,
#     'subject': {
#         'dsa': 50,
#         'CN': 50,
#         'DA': 65
#     }
# }
# print(d3)

# # Using sequence and dict function
# d4 = dict([('name','bappy'),('age',23), (3,3)])
# print(d4)

# # duplicate keys
# d5 = {'name':'ashirwad', 'name':'bappy'} #duplicate keys are not allowed
# print(d5)

# # mutable items as keys
# # d6 = {'name':'ashirwad', [1,2,3]:3} # not allowed - error
# d6 = {'name':'ashirwad', (1,2,3):3} # tupple allowed - error
# print(d6)

# # -------------ACCESSING ITEMS DICTIONARY---------------

# # []
# d = {'name': 'Ashirwad','gender': 'Male'}
# print(d['name'])
# print(d['gender'])

# # get()
# print(d.get('name'))
# print(d.get('gender'))

# # 2D
# d['item1']['item2']

# # -------------ADDING KEY-VALUE PAIR TO DICTIONARY---------------
# d = {'name': 'Ashirwad','gender': 'Male'}
# d['age'] = 23
# d['weight'] = 80
# print(d)

# # -------------REMOVE KEY-VALUE PAIR FROM DICTIONARY---------------

# d = {'name': 'Ashirwad', 'gender': 'Male', 'age': 23, 'weight': 80}
# # pop
# d.pop('age')
# print(d)

# # popitem - last item ko delete krta hai
# d.popitem() 
# print(d)

# # delete() - pure us ek item ko delete kr dega
# del d['name']
# print(d)

# # clear() - pure dict ko delete kr dega - empty bana dega
# d.clear()
# print(d)

# # --------------EDIT KEY-VALUE PAIR----------------

# d = {'name': 'Ashirwad', 'gender': 'Male', 'age': 23, 'weight': 80}
# d['name'] = 'Bappy'
# print(d)

# # -------------------DICTIONARY OPERATIONS------------------

# # Membership
# d = {'name': 'Ashirwad', 'gender': 'Male', 'age': 23, 'weight': 80}
# print(d)
# print('Ashirwad' in d) # false since value ki baat  nhi krega keys ki krega - FALSE
# print('name' in d) # keys search kr rhe to TRUE dega

# # iteration
# for i in d:
#     print(i) #only keys print honge

# for i in d:
#     print(i, d[i]) # key-value print hoga

# # -------------------DICTIONARY FUNCTIONS------------------

# d = {'name': 'Ashirwad', 'gender': 'Male', 'age': 23, 'weight': 80}
# # len/sorted
# print(len(d))
# print(sorted(d, reverse=True))

# # items/keys/values
# print(d.items()) #tupple dega
# print(d.keys()) #kwys dega
# print(d.values()) #values dega

# # update()
# d1 = {1:2, 3:4, 5:6 }
# d2 = {4:7, 6:8}

# d1.update(d2)
# print(d1)
