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
