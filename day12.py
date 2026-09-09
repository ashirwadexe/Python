# # =================================================
# # =========== DECORATORS AND NAMESPACE ============
# # =================================================

# # ----------- Namespaces -------------

# # A namespace is a space that holds names(identifiers).Programmatically speaking, namespaces are dictionary of identifiers(keys) and their objects(values)
# # There are 4 types of namespaces:
# #   --> Builtin Namespace
# #   --> Global Namespace
# #   --> Enclosing Namespace
# #   --> Local Namespace

# # ---------- Scope and LEGB Rule ------------------------

# # A scope is a textual region of a Python program where a namespace is directly accessible.
# # The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope. If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.

# # local and global
# # LEGB Rule - ke according local pahle (b) print hoga then global (a) print hoga
# a = 2
# def temp():
#     b = 3
#     print(b)

# temp()
# print(a)

# # local and global - same name
# # LEGB Rule will follow
# a = 2
# def temp():
#     a = 3
#     print(a)

# temp()
# print(a)

# # local and global -> local does not have but global has
# # agar python ke interpretor ko local me nhi mila to enclosing me ja ke doondhega waha bhi nhi mila to global me ja ke doodhega
# a = 2
# def temp():
#     print(a)

# temp()
# print(a)

# # local and global -> editing global
# a = 2
# def temp():
#     # local var: local me global ko access kr sakte h but usko edit/write/changes nhi kr sakte just read kr sakte hai
#     a += 1
#     print(a)

# temp()
# print(a)

# # but change kr payenge this way ->
# a = 2
# def temp():
#     global a # bata diya ki global a hai
#     a += 1
#     print(a)

# temp()
# print(a)

# # local and global -> global created inside local
# def temp():
#     # local var banega ye outside scope not availabe
#     global a # now availabe global
#     a = 1
#     print(a)

# temp()
# print(a)

# # local and global -> function parameter is local
# def temp(z):
#     # z is local var
#     print(z)

# a = 5
# temp(5)
# print(a)

# ========= BUILT-IN SCOPE ==========

# print('hello')

# # how to see all builtins
# import builtins
# print(dir(builtins))

# #  remaining builtins
# # builtin function ko agar global me use krte h to built-in override k=ho jaega or error aaega jaise yaha niche aa raha 
# L = [1,2,3]
# max(L)

# def max():
#     print('hello')

# max(L)

# =========== Enclosing Scope ==============
# ye hame dekhne ko milta hia inside nested functions

# def outer(): # ye outer wale ka scope hi enclosing scope hia also known as non-local scope
#     def inner():
#         print("inner function")
#     inner()
#     print('outer function')

# outer()
# print('main program')

# # LEGB Rule - se 4(local) 1st then 3(enclosing) then 1(global)
# def outer():
#     # a = 3
#     def inner():
#         # a = 4
#         print(a)
#     inner()
#     print('outer function')

# a = 1
# outer()
# print('main function')

# # =========== Non-Local keyword ==============
# def outer():
#     a = 3
#     def inner():
#         nonlocal a # yaha ham bata rhe hai ki local ke andar enclosing/nonlocal variable me changes kr rhe hai
#         a += 4
#         print(a)
#     inner()
#     print('outer function')

# a = 1
# outer()
# print('main function')