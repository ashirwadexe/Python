# OPERATORS IN PYTHON
#Arithmetic
print(5+6)
print(5-6)
print(12/6)
print(12%6)
print(12**6)
print(515//6)

# Relational
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4!=5)

# Logical
print(1 and 0)
print(1 or 0)
print(not 1)

#Bitwise Operators - works on bits 

#bitwise and 
print(2 & 3) 
                # 010
                # 110
                # ---
                # 010 -> 2 in decimal - result of above operation

# Bitwise or
print(2 | 3)
                # 010
                # 110
                # ---
                # 110 -> 3 in decimal - result of above operation

# Bitwise xor
print(2 ^ 3)
                # 01
                # 11
                # ---
                # 10 -> 1 in decimal - result of above operation

# Bitwise not - ye 0 ko 1 or 1 ko 0 kr dega
print(~3)

# Bitwise left
print(4 >> 2)

# Bitwise right
print(4 << 2)

# Assignment Operators
#  = 
#  a = 2; ----> here using = assignment opertor to assign a value 2

# Membership Operator
# in/ not in
# ye operator batata hai ki koi chij exist krta hai ki nhi
print('D' in 'Delhi') # true
print('D' not in 'Delhi') # false 

# PROGRAM - Find the sum of digits of a 3 digit number.
# num = int(input('Enter a 3 digit number: '))
# # num = 123
# a = num%10      # a = 3, num = 120
# num = num//10   # num = 12
# b = num%10      # b = 2, num = 10
# num = num//10   # num = 1

# print('Sum: ', a + b + num)



# ----------------------------------------
# ----------------If - Else---------------
# ----------------------------------------

# SYNTAX OF IF-ELSE
# if condition : 
#     code
# else : 
#     code

# Login program and identation
email = input('Enter email: ')
password = input('Enter password: ')

if email == 'ashirwad@gmail.com' and password == '12345': 
    print('Welcome Ashirwad')
elif email == 'ashirwad@gmail.com' and password != '12345':
    print('Incorrect password')
    password = input('Enter password again: ')
    if password == '12345': 
        print("Welcome Ashirwad")
    else : 
        print('Nikal sale')
else : 
    print('Access denied')
