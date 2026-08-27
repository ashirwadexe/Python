# # # ============HOW OBJECTS ACCCESS ATTRIBUTES================

# class Person:
#     def __init__(self, name_input, country_input):
#         self.name = name_input
#         self.country = country_input
#         self.greet()

#     def greet(self):
#         if self.country == "India" or "india":
#             print('Namaste,', self.name)
#         else:
#             print('Hello,', self.name)

# p = Person('Ashirwad', 'India')

# # how to access attributes
# print(p.name)

# # how to access methods()
# print(p.greet())

# # what if I try to access non-existential attributes
# # ERROR AAEGA

# # Attribute creation from outside of the class
# ans = p.gender = 'male'
# print(ans)

# # =================== REFERENCE VARIABLE ==================

# #    ==> Reference variables hold the objects
# #    ==> We can create objects without reference variable as well
# #    ==> An object can have multiple reference variables
# #    ==> Assigning a new reference variable to an existing object does not create a new object

# # Object without a reference
# class Man:
#     def __init__(self):
#         self.name = 'Ashirwad'
#         self.age = 23

# # Man() ko call krne pe Man ka object ban raha hia memory me isko kahi pe store krne ki jrurt nhi hai
# Man()
# # yaha Man() ko call krne pe man ka object ban raha hai or uska address 'm' me ja ke store ho raha hai bas
# # m -> is not the object it is the reference variable that holds the address of the object Man
# m = Man()
# print(m)


# # ================ PASS BY REFERENCE ===============
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# # outside the class => function
# def greet(person):
#     print('Hi my name is', person.name, 'and I am a ', person.gender)
#     p1 = Person('Aditi', 'female')
#     return p1

# # ham kisi function me ek Class ke object jo bhi pass kr sakte hai jaise yaha kiya hai
# p = Person('Ashirwad', 'male')
# x = greet(p)
# print(x.name)
# print(x.gender)

# # yaha pe ham function ko object ka address bhej rhe hai isko hi pass by reference kahte h 
# # yaha sidhe object na bhej kr ke uska reference(address) bhejte hai
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# def greet(person):
#     print(id(person))
#     person.name = 'Bappy'
#     print(person.name)

# p = Person('Ashirwad', 'male')
# print(id(p))
# greet(p)
# print(p.name)

# # ============= OBJECT KI MUTABILITY ===============
# # Python me sare object mutable hote hai but ham inko immutable bana sakte hai
# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# def greet(person):
#     person.name = 'bappy'
#     return person

# p = Person('Ashirwad','male')
# print(id(p))
# p1 = greet(p)
# print(id(p1))

# # instance var -> python tutor
# # Instance variable ek aisa variable hota h jiski value alag alag objects ke liye alag alag hoti hia
# # Instance variable ki value object pe dependent hoti hai
# class Person:

#   def __init__(self,name_input,country_input):
#     self.name = name_input
#     self.country = country_input

# p1 = Person('Ashirwad','India')
# p2 = Person('Steve','Australia')
# print(p1.name)
# print(p2.name)

# # ===============================================
# # ============ ENCAPSULATION ====================
# # ===============================================

# # We can make any attribute/variable of a class private using 'double underscore => __' 
# # eg. __name, __balance
# # This __name will store in memory as -> _ClassName__AttributeName 
# # eg. __name = _Atm__name, __balance = _Atm__balance

# # to allow access of our attributes from the outside of class we use getter() and setter()
# # we can write inside the setter function to allow which type of value can be set or which is not

# class Atm: 
#     def __init__(self):
#         self.pin = ''
#         self.__balance = 0
#         self.menu()

#     # getter - getter is used to access the private variables outside the class
#     def get_balance(self):
#         return self.__balance

#     # setter - setter is used to set the values of private variables from outside the class
#     # is function me ham logic likh ke control kr sakte h ki koun sa type of value set hoga or koun sa nhi
#     def set_balance(self,new_value):
#         if type(new_value) == int:
#             __balance = new_value
#         else: 
#             print('beta bahut marenge')
#         return self.__balance

#     def menu(self):
#         user_input = input("""
#             Hi how can i help you ?
#             1. Press 1 to create pin.
#             2. Press 2 to change pin.
#             3. Press 3 to check balance.
#             4. Press 4 to withdraw.
#             5. Press anything else to exit.
#         """)
#         if user_input == "1":
#             # create pin
#             self.create_pin()
#         elif user_input == "2":
#             # change pin
#             self.change_pin()
#         elif user_input == "3":
#             # check balance
#             self.check_balance()
#         elif user_input == "4":
#             # withdraw
#             self.withdraw_balance()
#         else:
#             exit()

#     # create pin function()
#     def create_pin(self):
#         user_pin = input("Enter pin:")
#         self.pin = user_pin

#         user_balance = input("enter balance:")
#         self.balance = user_balance

#         print("Pin created successfully")
#         self.menu()

#     # change pin function()
#     def change_pin(self):
#         old_pin = input("enter old pin: ")
#         if old_pin == self.pin:
#             # let him change pin
#             new_pin = input("enter new pin:")
#             self.pin = new_pin
#             print("pin change successfull")
#             self.menu()
#         else:
#             print("wrong pin")
#             self.menu()

#     # check balance function()
#     def check_balance(self):
#         user_pin = input("enetr your pin to check balance: ")
#         if user_pin == self.pin: 
#             user_balance = self.balance
#             print("Your balance: ", user_balance)
#             self.menu()
#         else: 
#             print("Pin is wrong")
#             self.menu()       

#     # withrwa balance function()
#     def withdraw_balance(self):
#         user_pin = input("enetr your pin to withdraw balance: ")

#         if user_pin == self.pin:
#             withdraw_amount = int(input("Enter amout: ")) 
#             curr_balance = int(self.balance)

#             if withdraw_amount <= curr_balance:
#                 new_balance = curr_balance - withdraw_amount
#                 self.balance = str(new_balance) 
#                 print(withdraw_amount," Rs. deducted from your account.")
#                 print("Current Balance: ", new_balance) 
#             else: 
#                 print("greeb sale itna paisa nhi h tere account me bas", self.balance, "Rs. hi hia chor")
#         else: 
#             print("Wrong pin saale chor")
#         self.menu()

# obj = Atm()


# # ==================== COLLECTION OF OBJECTS ==================
# # we can store multiple objects inside a set, dictionary, etc

# # list of objects
# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('Ashirwad','male')
# p2 = Person('Bappy','male')
# p3 = Person('Aditi','female')

# L = [p1,p2,p3]

# for i in L:
#   print(i.name,i.gender)

# # dict of objects
# # list of objects
# class Person:

#   def __init__(self,name,gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('Ashirwad','male')
# p2 = Person('Bappy','male')
# p3 = Person('Aditi','female')

# d = {'p1':p1,'p2':p2,'p3':p3}

# for i in d:
#     print(d[i].name)

# ==================== STATIC VARIABLES ==================

# Static variable object ke liye hota hai or ye har object ke liye same hona chahiye
# syntax ---> ClassName.VariableName
# eg.   school ka saam 

# Instance variable class ka hota hia or ye har object ke liye alag hota hai
# syntax ---> self.VariableName or objName.VariableName
# eg.  Student ka cgpa
#      Customer ka naam  
#      studnet ka naam