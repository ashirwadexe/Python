# # =========================================================
# # ==============OBJECT ORIENTED PROGRAMMING================
# # =======================OOP CONCEPT=======================
# # =========================================================

# # NOTE: Everything in python is an object.
# # OOP gives the power to a programmer to create his own data types.
# # OOP is a programming pradigm that helps a programmer to create his own data types and use it more flexibly.

# # ===========> CLASS <===========
# # Python me jitne bhi data types hai eg. int, float, list, tupple -> all are built-in classes but when a variable of these classes are created python consider them as python objects
# #  L = [1,2,3,4]
# # Here => L is a class & [1,2,3,4] this variable is an object of that class L.


# # CLASS -> Class is a blueprint or a set of rules ki us class ka object behave kaise krega or class ke andar sare rules defined honge 

# # CLASS -> it has 2 things
# #           1. Data or Property
# #           2. Functions or Behavior
# #           eg. STRING has property -> Immutable, ordered, etc
# #               STRING has functions -> upper(), startswith(), find(), index(), etc

# # REMEMBER: Object is an instance of the Class.

# # eg:   Car --> Wagnor // wagnor = Car()
# #       Sports ---> Cricket // cricket = Sports()
# #       Animals --> Langoor // langoor = animals()

# # SYNTAX TO CREATE AN OBJECT
# # objectname = classname()
# # Object Literal -> L = [1,2,3,4]
# # we can create a list in object syntax also -> L = list()

# # SMALL BANKING APPLICATION - ATM Machine Code/Program

# # creating a class
# # We use pascal case to name a class -> HelloWord, MyAtm, etc

# class Atm: 
#     # constructor - is a function inside the class
#     # constructor is special function -> superpower -> to execute the functions inside it we dont need to call the constructor specifically
#     # CONSTRUCTOR SYNTAX
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#         self.menu() # calling the menu from inside constructor so that whenever object of atm is called this menu get executed 
#         # print("main to execute ho gya") #atm class ke object ko call krte hi ye constructor apne aap call ho gya

#     # creating ATM functionality
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
#             withdraw_amount = int(input("Enter amout: ")) #since input take string but converting into into int so that arth op can be performed line minus(-)
#             curr_balance = int(self.balance) #since balance is stored as a string but converting into into int so that arth op can be performed line minus(-)

#             if withdraw_amount <= curr_balance:
#                 new_balance = curr_balance - withdraw_amount
#                 self.balance = str(new_balance) #converting back to string so that error dont happen
#                 print(withdraw_amount," Rs. deducted from your account.")
#                 print("Current Balance: ", new_balance) 
#             else: 
#                 print("greeb sale itna paisa nhi h tere account me bas", self.balance, "Rs. hi hia chor")
#         else: 
#             print("Wrong pin saale chor")
#         self.menu()

# # class created -> but will not execute untill an object is created of that class
# obj = Atm()


# # =============> METHOD vs FUNCTION <=================
# # METHOD - function defined inside a class is called method
# # FUNCTION - a function independent of a class and defined outside it is called a fubction
# # eg.   len() -> is a function because it is independent os any class 
# #       List.append(4) --> is a Method because it is defined inside a list class


# # =============> CLASS DIAGRAM <=================
#             #         ┌──────────────────────────────┐
#             #         │             Atm              │
#             #         ├──────────────────────────────┤
#             #         │ - pin : str                  │
#             #         │ - balance : int              │
#             #         ├──────────────────────────────┤
#             #         │ + __init__() : None          │
#             #         │ + menu() : None              │
#             #         │ + create_pin() : None        │
#             #         │ + change_pin() : None        │
#             #         │ + check_balance() : None     │
#             #         │ + withdraw_balance() : None  │
#             #         └──────────────-───────────────┘
           


# # ==============> MAGIC METHOD aka DUNDER METHOD <====================
# # magic methods are specials methods and every one has a super power
# # SYNTAX --> __name__ 
# #           eg. __init__ => constructor
# # we can create our own data types using these magic methods --> python have 1500 magic methods
# #       **CONSTRUCTOR -> ye ek magic method hhota hai or iski superpower hai ki ye self call hota h object ko call krne pe 
# #       => constructor ke andar ham vo code likhte h jiska control h user ko nhi dena chahte
# #       => constructor is used to write configuration related code means the code used to connect the app with database/backend is written inside it
# #       => python me hamesha constructor ka naam "__init__()" hi rahega always

# #       GOLDEN RULE OF OPP
# #           -> All the methods and data can only be called by object of the class.
# # 
# #       **SELF -> 
# #               Self allow krta hia ki class ke ek method ko agar dusre method se baat krni hai ya uske andar se call krna h to ye allow "self"
# #               krega kyoki according to golden rule of OOP only the object of that class can access the data and method of that class
# #               
# #               NOTE: id(obj) and id(self) => both are same therefore both object and self are same.
# #               Therefore, self can access the class methods and properties kyoki self hi object hai or object hi self hai
# #               So -> jaise hi object ban raha hai {obj = Atm()} waise hi object as a "self" constructor{def __init__(self)} ke argument me pass ho
# #                     ja raha hai or ham jo bhi data ya method ko call krna chah rhe h uske andar se self.data ya self.method() usko call karwa de
# #                     raha hia
# #               Self ke jagah pr ham kuch bhi naam use kr sakte h jo bhi use krege vo hi point krega object of the class ko


# ===============================================================
# ========CREATING OUR OWN DATA TYPE USING OOPs CONCEPT==========
# ===============================================================

# ========FRACTION DATA TYPE=============

class Fraction:
    # Parameterized Constructor: It expecting parameters
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # 2nd Magic Method - to print the object
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    # 3rd Magic Method - to add to object
    def __add__(self, other):
        new_num = self.num*other.den + other.num*self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return '{}/{}'.format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return '{}/{}'.format(new_num, new_den)

# object of Fraction() class created
fr1 = Fraction(2,3) 
print(fr1)
fr2 = Fraction(2,3) 
print('add: ', fr2 + fr1)
print('sub: ', fr2 - fr1)
print('mult: ', fr2 * fr1)
print('div: ', fr2 / fr1)
