# # -------------------------------------------
# # ---------------------STRINGS---------------
# # -------------------------------------------

# # Strings are sequence of Characters
# # In Python specifically, strings are a sequence of Unicode Characters

# # --------------Creating Strings---------------------
# s = 'hello'
# print(s)

# s = "hello"
# print(s)

# s = """Hello world""" # tripple inverted comma - for multi line strings
# print(s)

# s = str('hello')
# print(s)

# # --------------Accessing Strings---------------------
# # INDEXING +ve
# s = "hello world"
# print(s[0])
# print(s[9])
# print(s[4])

# # INDEXING -ve
# print(s[-3])
# print(s[-1])
# print(s[-2])
# print(s[::-1]) #it reverses the string

# # SLICING
# S = "HELLO WORLD"
# print(S[0:6])
# print(S[0:9])
# print(S[0:11:2]) #2 ka jump le ke print hoga

# --------------Adding Chars to Strings---------------------





# # --------------Editing Strings---------------------
# # String data type is immutable it can not be reassigned a new valu.
# s = "HELLO WORLD"
# # s[0] = 'L' #will give error
# ans = 'L' + s[1:]
# print(ans)

# # --------------Deleting Strings---------------------
# deleteing a portion of string is not allowed since string is immutable
# s = "HELLO WORLD"
# del s

# # --------------Operations on Strings---------------------
# s1 = "hello"
# s2 = "world"

# # ARITHEMATIC - add and multiplication allowed only
# print(s1+ ' '+s2) 
# print(s1*5)

# # RELATIONAL OPERATORS
# # logic - ham strings ko lexiographycally compare kr rhe hai means ASCII value ke basis pe comparison ho raha
# print(s1 == s2)
# print(s1 != s2)
# print(s1 >= s2)
# print(s1 > s2)
# print(s1 <= s2)
# print(s1 < s2)
# print('Pune' > 'pune') #FALSE -> since ASCII value of "P" is smaller tha "p"

# # LOGICAL OPERATORS
# print(s1 and s2) # output: world -> python ne dekha and hai to pura check kr ke true print krna hoga to last wala true world print kiya
# print(s1 or s2) # output: hello -> python ne dekha or hai to pahla wala true tha to pahle hello hi print kr diya
# print("" and "world") # output: "" since and false dega 
# print("" or "world") # since "" is falsy value to or ne world print kiya since its truthy value

# # LOOPS ON STRINGS
# s = "HELLO"
# for i in s:
#     print(i)

# for i in 'DELHI': #ye 5 baar PUNE print krega since delhi has 5 char
#     print('PUNE')

# # MEMBERSHIP OPERATORS
# print('D' in 'Delhi')
# print('A' in 'Delhi')
# print('e' not in 'Delhi')


# # --------------String Functions---------------------

# # Common Functions
# str = "HELLOWORLD"
# # ---------------len---------------
# print(len(str))
# # ---------------max---------------
# print(max(str))
# # ---------------min---------------
# print(min(str))
# # ---------------sorted---------------
# print(sorted(str, reverse=1))

# # THESE WORKS ONLY ON STRINGS
# # -----------------Capitalize-----------------
# print("hello".capitalize())
# # -----------------/Title-----------------
# print("hello world how are you".title())
# # -----------------/Upper-----------------
# print("hello".upper())
# # -----------------/Lower-----------------
# print("hello".lower())
# # -----------------/Swapcase-----------------
# print("HeLlO wOrld".swapcase())

# # --------------------Count--------------------
# print("my name is ashirwad chaurasia".count('i'))
# # --------------------/Find--------------------
# print("my name is ashirwad chaurasia".find('is'))
# # --------------------/Index--------------------
# print("my name is ashirwad chaurasia".index('h'))

# # -------------------endswith-------------------
# print("my name is ashirwad chaurasia".endswith('chaurasia'))
# # -------------------startswith-------------------
# print("my name is ashirwad chaurasia".startswith('my'))

# # ---------------format()----------------------
# name = 'Ashirwad'
# gender = 'male'

# print('Hi my name is {} and I am a {}'.format(name, gender))

# # ---------------------isalnum---------------------
# print("123ashirwad".isalnum()) #check string is alphanumeric or not
# # ---------------------isalpha---------------------
# print("ashirwad".isalpha()) #check string is alphabetic or not
# # ---------------------isdigit---------------------
# print("1234".isdigit()) #checks string is digit or not
# # ---------------------isidentifier---------------------
# print("first_name".isidentifier())
# print("first-name".isidentifier())

# # ---------------------Split---------------------
# print("my name is ashirwad".split())
# # ---------------------Join---------------------
# print(" ".join(['hi', 'my', 'name', 'is', 'ashirwad']))
# # -----------------replace-----------------
# print("hi my name is ashirwad".replace("ashirwad", "bappy"))
# # -----------------strip-----------------
# print("ashirwad            ".strip())