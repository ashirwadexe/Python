# # ----------------------------------------------
# # ------------------FUNCTIONS-------------------
# # ----------------------------------------------

# # CREATING A FUNCTION

# # check no. is even or not
# def is_even(num):
#     """
#     This function returns if given number is odd or even
#     Input - any valid integer
#     Output - odd/even
#     Check it only takes integer as argument/input
#     """
#     if type(num) == int:
#         if num % 2 == 0:
#             print("Number is even")
#         else:
#             print("Number is odd")
#     else: 
#         print("pagal hia kya ? integer de input me")  

# is_even("a")
# for i in range(1,11):
#     is_even(i)

# # PARAMETER vs ARGUMENT
# # Parameter - function create ke time ham input jo pass hota hia usko parameter kahte hai
# # Argumnet - function call ke time jo input dete hai usko argument kahte hai
 
# # Types of Argument
# # 1. Default Argument  
# def power(a=1,b=1):
#     return a**b

# print(power(2,4))

# # 2. POsitional Argument
# # python me simple hai ki ye ek order follow krega pahla argument pahle parameter ko milega or dusra argument dusre parameter ko milega and so on

# # 3. Keyword Argument
# # ham argumnt ko parameter ko naam se pass kr sakte hai
# print(power(b=3, a=2)) # position kya h ye matter nhi krta functin me parameter ka jo position hoga argumnet wiase hi ja ke arrange ho jaega  -> power(a=2, b=3) => 8

# # *args AND **kwargs
# # *args and **kwargs are special python keywords that are used to pass the variable length of arguments to a function

# # *args
# # allows us to pass a variable of non-keyboard arguments to a function
# # *args hame allow kr rha hai n-numbers of parameter pass krne ke liye
# # *args sare inputs mo ek tupple me store kr raha hai
# # *args ke jagah pe ham kuch bhi likh sakte hai *bappy, *xyz, *lamda, *etc
# def multiply(*args):
#     product = 1
#     for i in args:
#         product = product * i

#     return product

# ans = multiply(1,2,4,5)
# print(ans)

# # **kwargs
# # It allows us to pass any no. of keyword arguments
# # keyword arguments mean that they contain key-value pair, like a python dictionary
# # python **kwargs ko ek dictionary me convert kr deta hai internally

# def display(**kwargs):
#     for (key, value) in kwargs.items():
#         print(key, '->', value)

# ans = display(India="Delhi", Nepal="Kathmandu", USA="WDC", Bangladesh="Dhaka")
# print(ans)

# How functions are executed in the memory ?
# function jab call hota hai tab se le ke return hone tak hi bas memory me function active rahta hia uske pahle or baad me function ka koi vajud nhi hota memory me

# Without return statement
# agar return statement nhi lagaya to ek default value print hogi -> NONE

# # Variable Scope
# # Global Variable - ye main program ke under aaega isko function ke andar or bahar kahi bhi use kiya ja sakte hai
# # Local Variable - ye bas function ke andar hota aata hai isko bas function ke andar hi usko use kiya ja sakta hai

# def g(y):
#     print(x)
#     print(x+1)
# x = 5
# g(x)
# print(x)

# # local or gloabl dono variable ka naam same ho sakta hai
# def f(y):
#     x = 1 #local variable
#     x+= 1
#     print(x)
# x = 5 #global variable
# f(x)
# print(x)

# # agar function ke andar local variable nhi hai to global ko use kr sakta hai pr global me change  nhi kr sakta function ke andar
# def h(y):
#     x += 1 #change not allow -> error
# x = 5
# h(x)
# print(x)

# # But options hai chnage krne ka
# def h(y):
#     global x #bad practice dont do it
#     x += 1
# x = 5
# h(x)
# print(x)

# # NESTED FUNCTION
# # nested function main program se hidden hota hai to ahme pahle outer function ko call krna hoga to call isnder function
# def f():
#     def g():
#         print('inside function g')
#     g()
#     print('inside function f')

# f()

# # FUNCTIONS ARE 1ST CLASS CITIZENS IN PYTHON

# # type and id
# def square(num):
#     return num**2

# print(type(square))
# print(id(square))

# # reassign
# x = square
# print(id(x))

# # deleting a function
# # del square
# # square(3)

# # storing a function
# L =[1,2,3,square]
# print(L)

# # functions are immutable since sets allow its storage in it.

# # returning a function
# def f():
#     def x(a,b):
#         return a+b
#     return x
# val = f()(2,3) # f() -> return kr raha hia "x" or ye hi x -> f() ki jagah aa ke val = x(2,3) bana de raha h or ye function call ho ja rhi hai or ans aa ja raha 5
# print(val)

# # function as argument
# def func_a():
#     print('inside func_a')
# def func_b(z):
#     print('inside func_b')
#     return z()
# print(func_b(func_a))

# 1st class citizens means functions have all the rights of datatypes

# Benefits of using a Function
# 1. Code modularty
# 2. Code readability
# 3. Code reusability

# # ---------LAMBDA FUNCTION----------
# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression.
# # Lambda function ka naam nhi hota.

# # square
# square = lambda x : x**2
# print(square(2))

# # sum
# sum = lambda x,y : x+y
# print(sum(5,3))

# # check if a string has a
# str = lambda str: 'a' in str
# print(str("Bppy"))

# # odd/even
# check = lambda a: 'even' if a%2 == 0 else "odd"
# print(check(11))

# # Difference bwt lambda and normal function
# # 1. No name -> anonymous
# # 2 lambda has no return value(infact, returns a function)
# # 3. lambda is written in one line
# # 4. mot reusable


# # ----------Higher Order Function------------
# # ek aisa function jo dusre function ko return kre ya fir dusre function ko argument me pass kre

# def square(x):
#     return x**2
# # HOF
# def transform(f, L):
#     output = []
#     for i in L:
#         output.append(f(i))
#     print(output)

# L = [1,2,3,4,5]
# print(transform(square,L))
# print(transform(lambda x:x**3,L))

# # ------------ MAP()----------------
# # square the items of a list using map()
# ans = list(map(lambda x:x**2, [1,2,3,4,5,6,7,8,9,10]))
# print(ans)

# # odd/even labelling of a list items
# L = [1,2,3,4,5]
# ans = list(map(lambda x: 'Even' if x%2==0 else 'Odd', L))
# print(ans)

# # ------------ FILTER()----------------
# # number greater taht 5
# L = [2,3,5,8,5,3,4,5,5,6,7,4,3,3,4,5,6,10]
# ans = list(filter(lambda x:x>5,L))
# print(ans)

# # fetch fruites starting with 'a'
# L = ['apple', 'graphes', 'cheery']
# ans = list(filter(lambda x: x.startswith('a'), L))
# print(ans)

# # ------------ REDUCE()----------------
# import functools
# L = [1,2,3,4,5,6,7,8]
# ans = functools.reduce(lambda x,y: x+y, L)
# print(ans)

# # min
# ans = functools.reduce(lambda x,y: x if x<y else y, [23,1,4,66,90,0])
# print(ans)

