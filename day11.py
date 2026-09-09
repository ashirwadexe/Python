# # ==========================================
# # ========== EXCEPTION HANDLING ============
# # ==========================================

# # there are 2 stages where error may happen in a program
# #   1. During compilation - Syntax Error
# #   2. During execution - Exceptions

# # Syntax Error
# #   -> Something in the prgram is not written according to the program grammer
# #   -> Error is raised by the compiler/interpretor
# #   -> You can solve it by rectifying the program

# # eg of syntax error --> print "hello world"

# # Other examples of syntax error
# #   --> Leaving symbols like colon,brackets
# #   --> Misspelling a keyword
# #   --> Incorrect indentation
# #   --> empty if/else/loops/class/functions

# # IndexError
# # The IndexError is thrown when trying to access an item at an invalid index.
# L = [1,2,3]
# L[100]

# # ModuleNotFoundError
# # The ModuleNotFoundError is thrown when a module could not be found.
# import mathi #spelling of math module wrong
# math.floor(5.3)

# # KeyError
# # The KeyError is thrown when a key is not found
# d = {'name':'nitish'}
# d['age']

# # TypeError
# # The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
# 1 + 'a'

# # ValueError
# # The ValueError is thrown when a function's argument is of an inappropriate type.
# int('a')

# # NameError
# # The NameError is thrown when an object could not be found.
# print(k)

# # AttributeError
# L = [1,2,3]
# L.upper()

# # Stacktrace -- it is the error message given by python to tell where the error is to help solve it

# # ================ Exceptions ====================
# # If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.
# #   --> Exceptions are raised by python runtime
# #   --> You have to takle is on the fly
# # Examples
# #   --> Memory overflow
# #   --> Divide by 0 -> logical error
# #   --> Database error

# # Why is impotant to handle exceptions ?
# #   --> the error reduces the user experience 
# #   --> security, can't show this much technical data to the user

# # How to handle exceptions ?
# #   --> Try Except block

# # Let's create a file
# with open('sample.txt', 'w') as f:
#     f.write('Hello world')

# # try except demo
# try:
#     with open('sample11.txt', 'r') as f:
#         print(f.read())
# except: 
#     print('sorry file not found')

# # How to catching specific exceptions 
# try:
#     m = 5
#     f = open('sample.txt', 'r')
#     print(f.read())
#     print(m)
#     print(5/0)
# except FileNotFoundError:
#     print('file not found')
# except NameError:
#     print('variable not defined')
# except ZeroDivisionError:
#     print('cant divide by 0')
# except Exception as e:
#     print(e.with_traceback)

# # Else block
# try:
#     f = open('sample.txt', 'r')
# except FileNotFoundError:
#     print('file nhi mili')
# except Exception:
#     print('kuch to lafda hai')
# else:
#     print(f.read()) # agar try sahi se run hua to except bypass ho jaega or else trigger ho jaega

# # finally block
# try:
#     f = open('sample.txt', 'r')
# except FileNotFoundError:
#     print('file nhi mili')
# except Exception:
#     print('kuch to lafda hai')
# else:
#     print(f.read()) # agar try sahi se run hua to except bypass ho jaega or else trigger ho jaega
# finally: 
#     print('ye to print hoga hi hoga')

# # =========== raise Exception =================
# # In Python programming, exceptions are raised when errors occur at runtime. 
# # We can also manually raise exceptions using the raise keyword.

# # We can optionally pass values to the exception to clarify why that exception was raised
# #   --> raise NameError('aise hi try kr raha hu')
# #   --> raise FileNotFoundError('aise hi try kr raha hu')

# class Bank:

#   def __init__(self,balance):
#     self.balance = balance

#   def withdraw(self,amount):
#     if amount < 0:
#       raise Exception('amount cannot be -ve')
#     if self.balance < amount:
#       raise Exception('paise nai hai tere paas')
#     self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#   obj.withdraw(-5000)
# except Exception as e:
#   print(e)
# else:
#   print(obj.balance)

# =============== creating custom exceptions ==================
# exception hierarchy in python

# class MyException(Exception):
#   def __init__(self,message):
#     print(message)

# class Bank:

#   def __init__(self,balance):
#     self.balance = balance

#   def withdraw(self,amount):
#     if amount < 0:
#       raise MyException('amount cannot be -ve')
#     if self.balance < amount:
#       raise MyException('paise nai hai tere paas')
#     self.balance = self.balance - amount

# obj = Bank(10000)
# try:
#   obj.withdraw(5000)
# except MyException as e:
#   pass
# else:
#   print(obj.balance)