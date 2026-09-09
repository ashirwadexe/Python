# # =================================================
# # ================= FILE HANDLING =================
# # =================================================

# # Some Theory
# # Types of data used for I/O:
# #   -> Text - '12345' as a sequence of unicode chars
# #   -> Binary - 12345 as a sequence of bytes of its binary equivalent
# # Hence there are 2 file types to deal with
# #   -> Text files - All program files are text files
# #   -> Binary Files - Images,music,video,exe files

# # How File I/O is done in most programming languages
# # 1. Open a file
# # 2. Read/Write data
# # 3. Close the file

# # WRITING IN A FILE
# # Case1: If the file is not present
# f = open('sample.txt', 'w') # This will open the file sample.txt and if mot exits it will create one
# f.write('Hello world')
# f.close()

# # write multiple strings
# f = open('sample.txt', 'w')
# f.write('Hello ashirwad')
# f.write('\nHello aditi')
# f.close()

# # Case2: If the file is already present
# f = open('sample2.txt', 'w')
# f.write('Mera bharat mahan')
# f.close()

# # how exactly open() work ?

# # Problem with 'w' mode
# # 'w' mode will erase the previous data and replace that with new data
# f = open('sample.txt', 'a') # append(a) mode dont replace but add the data at next step
# f.write('\nI am fine')
# f.write('\nhow are you ?')

# # Write lines 
# L = ['hello\n', 'hi\n', 'how are you?\n', 'i am fine\n']
# f = open('sample.txt', 'w')
# f.writelines(L)
# f.close()


# # READING FROM A FILE
# # using read() funtion of python
# f = open('sample.txt', 'r')
# s = f.read()
# print(s)
# f.close()

# # read upto n-chars
# f = open('sample.txt', 'r')
# s = f.read(10)
# print(s)
# f.close()

# # readline() - to read line by line
# f = open('sample.txt', 'r')
# print(f.readline(), end='')
# print(f.readline(), end='')
# f.close()

# # reading entire file using readline()
# f = open('sample.txt', 'r')
# while True:
#     data = f.readline()
#     if data == '':
#         break
#     else: 
#         print(data, end='')
# f.close()


# # Using Context Manager (With)
# #       It's a good idea to close a file after usage as it will free up the resources
# #       If we dont close it, garbage collector would close it
# #       'with' keyword closes the file as soon as the usage is over

# # with
# with open('sample.txt', 'a') as f:
#     f.write('\nselmon bhai')

# # try f.read() now
# with open('sample.txt', 'r') as f:
#     print(f.read())

# # moving within a file -> 10 char then 10 char
# with open('sample.txt', 'r') as f:
#     print(f.read(15))
#     print(f.read(10))

# # benefits? --> to load a big file in memory
# big_L = ['hello ashirwad\n' for i in range(1000)]

# with open('big.txt', 'w') as f:
#     f.writelines(big_L)
    
# with open('big.txt', 'r') as f:
#     chunk_size = 100

#     while len(f.read(chunk_size)) > 0:
#         print(f.read(chunk_size))
#         f.read(chunk_size)

# # seek and tell function
# # tell() --> ye fnt batayega ki abhi cursor kis psotion pr hai
# # seek() --> ye fnt se ham kisi bhi position pe move kr sakye hain
# with open('sample.txt','r') as f:
#   print(f.read(10))
#   print(f.tell())
#   f.seek(15)
  
#   print(f.read(10))
#   print(f.tell())

#   # seek during write
# with open('sample.txt','w') as f:
#   f.write('Hello')
#   f.seek(0)
#   f.write('Xa')

# Problems with working in text mode
# can't work with binary files like images
# not good for other data types like int/float/list/tuples

# # Working with binary files
# with open('image.png', 'r') as f:
#     f.read() # read() unicodes ko read krta hai binary ko nhi

# # creating a binary file
# # here reading a binary file and copying it to another file
# with open('image.png', 'rb') as f:
#     with open('image_copy.png', 'wb') as wf:
#         wf.write(f.read())

# # Working with another data types
# with open('sample.txt', 'a') as f:
#     # f.write(5) # 5 nhi write kr sakte since its not a unicode char only string is allowed
#     f.write('\n5') # ab ho jaega since '5' is a string

# # more complex data
# d = {
#     'name':'nitish',
#      'age':33,
#      'gender':'male'
# }

# with open('sample.txt','a') as f:
#   f.write(str(d))


# # =================================================
# # ======= Serialization and Deserialization =======
# # =================================================

# # Serialization - process of converting python data types to JSON format
# # Deserialization - process of converting JSON to python data types

# # Serialization using json module
# import json

# L = [1,2,3,4,5]

# with open('demo.json', 'w') as f:
#     json.dump(L,f)

# d = {
#     'name':'nitish',
#      'age':33,
#      'gender':'male'
# }

# with open('demo.json', 'w') as f:
#     json.dump(d, f, indent=4)

# # Deserialization
# with open('demo.json', 'r') as f:
#     ans = json.load(f)
#     print(ans)
#     print(type(ans))

# # Serialize and Deserialize tuple
# # tuple hamesha as list hi store hoga tuple me nhi
# import json
# t = (1,2,3,4,5,6)
# with open('demo.json', 'w') as f:
#     json.dump(t, f)

# # serialize and deserialize a nested dict
# d = {
#     'student':'nitish',
#      'marks':[23,14,34,45,56]
# }

# with open('demo.json','w') as f:
#   json.dump(d,f)


# # Serializing and Deserializing custom objects
# class Person:

#   def __init__(self,fname,lname,age,gender):
#     self.fname = fname
#     self.lname = lname
#     self.age = age
#     self.gender = gender

# # format to printed in
# # -> Nitish Singh age -> 33 gender -> male
# person = Person('Nitish','Singh',33,'male')

# # As a string
# # import json
# # with open('demo.json', 'w') as f:
# #   json.dump(person, f) # this will give error since python only serializes its own datatypes and not the one build by user

# # here we will serialize it
# # as a string
# import json
# def show_object(person):
#     if isinstance(person, Person):
#         return "{} {} age -> {} gender -> {}".format(person.fname, person.lname, person.age, person.gender)

# with open('demo.json', 'w') as f:
#     json.dump(person, f, default=show_object)

# # As a dict 
# import json
# def show_object(person):
#     if isinstance(person, Person):
#         return {'name':person.fname + ' ' + person.lname, 'age': person.age, 'gender': person.gender}

# with open('demo.json', 'w') as f:
#     json.dump(person, f, default=show_object, indent=4)


# # deserialization
# import json
# with open('demo.json', 'r') as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))

# # =========================================
# # =============== Pickling ================
# # =========================================

# # Pickling is the process whereby a Python object hierarchy is converted into a byte stream, and unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

# class Person:

#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def display_info(self):
#     print('Hi my name is',self.name,'and I am ',self.age,'years old')

# p = Person('ashirwad',23)

# # pickle dump
# import pickle
# with open('person.pkl','wb') as f:
#   pickle.dump(p,f)

# # pickle load
# import pickle
# with open('person.pkl','rb') as f:
#   p = pickle.load(f)

# p.display_info()

# Pickle Vs Json
# Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.