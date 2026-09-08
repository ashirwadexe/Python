# # =====================================================
# # ================== OOPs DAY-3 =======================
# # =========== INHERITANCE AND ABSTRACTIONS ============
# # =====================================================

# # ------------------ AGGREGATION ----------------------
# # Aggregation - one class has a relationship
# # meaning - one class owns the another class
# # eg. -> Here Customer class own kr raha hai Address class ko
# # NOTE: aggregation me ham ek private variables ko ham access nhi kr sakte hain but can do using getter
# class Customer: 
#     def __init__(self, name, gender, address):
#         self.name = name
#         self.gender = gender
#         self.address = address

#     def print_address(self):
#         print(self.address.get_city(), self.address.pin, self.address.state)

#     def edit_profile(self, new_name, new_city, new_pin, new_state):
#         self.name = new_name
#         self.address.edit_address(new_city, new_pin, new_state)


# class Address: 
#     def __init__(self, city, pin, state):
#         self.__city = city
#         self.pin = pin
#         self.state = state

#     def get_city(self):
#         return self.__city

#     def edit_address(self, new_city, new_pin, new_state):
#         self.__city = new_city
#         self.pin = new_pin
#         self.state = new_state
        

# add1 = Address('deoria', 274701, 'up')
# cust = Customer('ashirwad', 'male', add1)

# cust.print_address()
# cust.edit_profile('Bappy', 'GKP', 121212, 'Bihar')
# cust.print_address()


# # ------------------ INHERITANCE ----------------------

# # Inheritance allows the child class to access the variables and methods of the parent class.
# # It increases the code reusability.

# # eg. -> 

# # PARENT CLASS
# class User:
#     def __init__(self):
#         self.name = 'ashirwad'

#     def login(self):
#         print('login done')

# # CHILD CLASS
# class Student(User):

#     def enroll(self):
#         print('enrolled into the course')

# u = User()
# s = Student()

# print(s.name)
# s.login()
# s.enroll()

# # What gets inherited?
# # 1. Constructor
# # 2. Non Private Attributes
# # 3. Non Private Methods

# # 1. constructor example
# # CONCEPT: agar child class ke pass khud ka constructor nhi hai to parent class ka constructor class hoga

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000, "Apple", 13)
# s.buy()

# # constructor example 2
# # CONCEPT: Agar child ke pas constructor hai to parent ka contructor initialise hoga hi nhi or vo print nhi hoga
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor")

# s=SmartPhone("Android", 2)
# # This will not execute since child has its own constructor and parent class is not executing its own constructor
# print(s.brand)


# # 2. Child can't access private members of the class

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     #getter
#     def show(self):
#         print (self.__price)

# class SmartPhone(Phone):
#     def check(self):
#         print(self.__price)

# s=SmartPhone(20000, "Apple", 13)
# print(s.show())

# # FIND OUTPUT
# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def show(self):
#         print("This is in child class")
        
# son=Child(100)
# print(son.get_num())
# son.show()

# # FIND OUTPUT
# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,val,num):
#         self.__val=val

#     def get_val(self):
#         return self.__val
        
# son=Child(100,10)
# print("Parent: Num:",son.get_num())
# print("Child: Val:",son.get_val())

# # Method Overriding
# # NOTE: agar parent of child dono ke pas same name ka method ho to hamesha child ka method call hoga => Method Overriding
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")

# s=SmartPhone(20000, "Apple", 13)

# s.buy()

# # ----------- SUPER KEYWORD -----------------

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         # yaha child ka to buy() method to class hoga hi but using super() ham parent ka method bhi class kr sakte hain
#         # syntax to call parent ka buy method
#         super().buy()

# s=SmartPhone(20000, "Apple", 13)
# s.buy()

# # super -> constructor
# # yaha hamne child class se parent ke constructor ko call kiya hai or same variable ko inialise kiya hai child se
# class Phone: 
#     def __init__(self, price, brand, camera):
#         print('inside phone constructor')
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         print('inside smartphone constructor')
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print('inside smartphone constructor')

# s = SmartPhone(20000, 'apple', 12, 'mac', 8)
# print(s.os)
# print(s.brand)

# NOTE: super() keyword ko ham hamesha child class ke andar hi use kr sakte h outside me error aayega
# NOTE: super() keyword ko use kr ke ham bas methods ko call kr sakte hain variable ko nhi

# ------------- Inheritance in summary -----------------
# 1. A class can inherit from another class.
# 2. Inheritance improves code reuseability.
# 3. Constructor, attributes, methods get inherited to the child class
# 4. The parent has no access to the child class
# 5. Private properties of parent are not accessible directly in child class
# 6. Child class can override the attributes or methods. This is called method overriding
# 7. super() is an inbuilt function which is used to invoke the parent class methods and constructor

# --------------- Types of Inheritance -------------
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Hierarchical Inheritance
# 4. Multiple Inheritance(Diamond Problem)
# 5. Hybrid Inheritance

# # ------ 1. Single Inheritance -------
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()

# # ------ 2. Multilevel Inheritance -------

# class Product:
#     def review(self):
#         print ("Product customer review")

# class Phone(Product):
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000, "Apple", 12)
# s.buy()
# s.review()

# # ------ 3. Hierarchical Inheritance -------

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# class FeaturePhone(Phone):
#     pass

# SmartPhone(1000,"Apple","13px").buy()
# FeaturePhone(10,"Lava","1px").buy()

# # ------ 4. Multiple Inheritance -------

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class Product:
#     def review(self):
#         print ("Customer review")

# class SmartPhone(Phone, Product):
#     pass

# s=SmartPhone(20000, "Apple", 12)

# s.buy()
# s.review()

# # the diamond problem
# # https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class Product:
#     def buy(self):
#         print ("Product buy method")

# # Method resolution order - jiska naam pahle aaya vo execute hoga
# class SmartPhone(Phone,Product):
#     pass

# s=SmartPhone(20000, "Apple", 12)
# s.buy()


