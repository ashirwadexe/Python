# hot to print something in Py

# python output 
# print() function me hame string ke sath inverted commas dene hi honge but not with number or booleans
print("Hello World!!!")
print(123)
print(True)
print("Ashirwad", 1,2,3,4.6, True)
# output ke time pe char ke bich space aa ja raha apne aap- ye ho raha (sep='') property ki wajah se
# output: Ashirwad 1 2 3 4.6 True
print("Ashirwad", 1,2,3,4.6, True, sep='/')
# now output: Ashirwad/1/2/3/4.6/True
print("Ashirwad", 1,2,3,4.6, True, sep='&')
# now output: Ashirwad&1&2&3&4.6&True

# har output new line pe ho raha hai due to end='\ln'
# is default behaviour ko change krte h
print("hello", end='-')
print("hello", end='-')
print("hello", end='-')
print("hello", end='-')
# new output: hello-hello-hello-hello-
print("hello")


# ---------------------------------------
# -----------DATA TYPES------------------
# ---------------------------------------

# 1.Integers
# Python can handle this big 1*10^308 integer
print(8)
print(1e308)
print(1e309)
# output:   8
#           1e+308
#           inf - it cant handle 1*10^309 but till 308

# 2. Decimals
# Py can handle decimals/float till 1.7e309

# 3. Boolean
# Boolean is true or false

# 4.Text/String
print("hello Wolrd");

# 5. Complex Data
# real + imaginary
print(5+4j)

# 6. List -> Array in CPP
print([1,2,3,4,5]);

#7. Tuple
print((1,2,3,4,5));

#8. Sets
print({1,2,3,4,5});

# 9. Dictionary
print({'name': 'Ashirwad', 'Age': 23, 'Weight': 80});


# type() Function
print(type('Hello'))
print(type(1))
print(
    type(1+7j),
    type(True)
)

# ---------------------------------------
# -----------VARIABLES-------------------
# ---------------------------------------

# variables are containers used to store data for future use
# declaration of variable in python

name = "Ashirwad"
print('name is: ', name)

a = 3
b = 5
print('add: ', a+b)

# DYNAMIC TYPING - yaha ham variable ka type nhi define krte direct variable likh denge py ka interpreter khud find kr lega ki inte hai ya float ya string
result = "string"

# STATIC TYPING - yaha datatype define krna hoga
# int a = 5;

# DYNAMIC BINDING - isme varibale ka data type fix nhi hoti aage ja ke change ho sakti hai
name = "Bappy"
print(name)
name = 33.55
print(name)

# Smart way to define multiple variables
a=2
b='name'
c=777.987
print(a,b,c)

a,b,c, = 2, 'name', 777.987
print(a,b,c)


# ------------------------------------------------------
# -----------KEYWORDS & IDENTIFIERS-------------------
# ------------------------------------------------------

# KEYWORDS - These are reserved words for python, dont use them as variables (33 keywords in Py)
# Compilation - converting the english code into machine language(0/1)
# Compilor - converts the whole code in one go - FAST 
# Interpretor - converts the code line by line - SLOW 

# Identifiers - a name created by the programmer
# Rules to create a identifier
# 1. not start with digit
# 2. only underscore(_) special character can be used in naming
# 3. identifiers cannot be keywords


# ------------------------------------------------------
# -----------USER INPUT---------------------------------
# ------------------------------------------------------

name = input('Enter name: ')
print('Your Name is : ',name)

# IMPORTANT: input by default input string data type me leta hai kyoki ye ek unversal data form h isme baki sare types store ho sakte hai 
# add 2 numbers
fnum = input("enter 1st no: ");
snum = input("enter 2nd no: ");

sum = int(fnum)+ int(snum);
print('sum is: ', sum)


# ------------------------------------------------------
# -----------TYPE CONVERSION----------------------------
# ------------------------------------------------------

# Implicit - interpretor khud kr deta hai programmer ko kuch nhi krna
# Explicit - programmer type conversion krega 
# str to int (comples cant be changed to integer)
# type(int('4'))
# type(int(4.5))

# # int to str
# print(str(5))
# print(str(5.7665))

# ------------------------------------------------------
# -----------LITERALS----------------------------
# ------------------------------------------------------

# It is the raw value stored in a variable
a = 0b1010 #Binary Literal - 0b - bata raha h ki aage ki value binary me hia
b = 100 #Decimal Literal
c = 0o310 #Octal Literal
d = 0x12c # hexadecimal Literal

# Float Loteral
float_1 = 10.5
float_2 = 1.5e3 #1.5*10^3 - very big number
float_3 = .5e-3 #1.5*1^-3 - very small number

# Complex Literal
x = 3.14j
print(x.imag, x.real)

# String Literal
string = "This is Python."
strings = 'This is Python.'
char = "C"
multiline_string = """This is a multiline string with a more than one line code."""
unicode = u"\U0001F600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_string)
print(unicode)
print(raw_str)

# None Literal
ab = None
print(ab)