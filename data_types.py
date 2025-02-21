# 1. Numeric Types
# Python has three main numeric types:
# a. Integer (int)
# Whole numbers, positive or negative, without decimals.
num_int: int = 42

print(type(num_int)," num_int = ",num_int,)  # <class 'int'>

# b. Floating-Point (float)
# Numbers with decimal points.
num_float: float = 3.14
#num_float: float = .14

print(type(num_float), " num_float = ", num_float)  # <class 'float'>

# c. Complex (complex)
# Numbers with a real and imaginary part.
num_complex: complex = 2 + 3j

print(type(num_complex), " num_complex = ", num_complex)  # <class 'complex'>
#____________________________________________________________________________________________________________________________________________

# 2. Boolean (bool)
# Represents True or False.
is_python_fun: bool = True #False

print(type(is_python_fun), " is_python_fun = ", is_python_fun)  # <class 'bool'>
# ___________________________________________________________________________________________________________________________________________

# 3. Sequence Types
# These store multiple items in an ordered way.
# a. String (str)
# A sequence of characters enclosed in quotes.
text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    # <class 'str'>
print(type(text_single), " text_single   = ", text_single)    # <class 'str'>
print(type(text_multi), " text_multi    = ", text_multi)      # <class 'str'>
print(type(text_multi_1), " text_multi_1  = ", text_multi_1)  # <class 'str'>

# b. List (list)

# An ordered, mutable collection.
my_list_1: int = [1, 2, 3, "Java", 3.14, True] #Type hinting is not enforced in python, but you should mention appropriate data type in this case 'list'
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  # <class 'list'>
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead

# c. Tuple (tuple)
#An ordered, immutable collection.
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  # <class 'tuple'>


# d. Range (range)
# Represents a sequence of numbers.
num_range: range = range(1, 10, 2) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)  # <class 'range'>

for i in range(1, 10, 2): # we will study loops indepth in classes ahead
  print(i)

# ____________________________________________________________________________________________________________________________________________
# 4. Set Types  
#(We will cover this indepth in classes ahead)
# Unordered collections with unique elements.

# a. Set (set)
# Mutable, unordered, and contains unique values.
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)  # <class 'set'>
# out put: <class 'set'> my_set =  {1, 2, 33, 4, 5} it removes duplicates

# b. Frozen Set (frozenset)
# Immutable version of a set.
frozen_set = frozenset([11, 2, 3, 4, 4, 5])
#frozen_set = frozenset(my_set)
print(type(frozen_set), " frozen_set = ", frozen_set)  # <class 'frozenset'>
# Trying to add or remove will give an error ❌
# frozen_toys.add("train")  # ❌ This will cause an error
# frozen_toys.remove("car")  # ❌ This will also cause an error

# __________________________________________________________________________________________________________
# 5. Mapping Types
# Dictionary (dict) Stores key-value pairs.
# Key-value pairs.
my_dict: dict = {"name": "Alice", "age": 25, "language": "Python"}
print(type(my_dict)," my_dict = ", my_dict )  # <class 'dict'>
# ___________________________________________________________________________________________________________
# 6. Binary Types
# Python has binary types to work with such data:
# 1️⃣ bytes – Like a locked notebook (cannot change).
# 2️⃣ bytearray – Like a normal notebook (can change).
# 3️⃣ memoryview – Like a magnifying glass to see inside bytes.

# bytes (Cannot Change)
data = bytes([65, 66, 67])  # A = 65, B = 66, C = 67
print(data)  # Output: b'ABC'

byte_data: bytes = b"Hello"
print(type(byte_data), " byte_data = ", byte_data)  # <class 'bytes'>

# B. Bytearray (bytearray)
byte_array: bytearray = bytearray([65, 66, 67, 69]) #65=A, 66=B ....decimal
print(type(byte_array), " byte_array = ", byte_array)  # <class 'bytearray'>
print(byte_array[0])
print("Empty bytearray(): ",bytearray())


# Creating a bytearray object
ba: bytearray = bytearray(b"hello")
print("Before: ba = ", ba)

# Modifying the bytearray
ba[0] = 72  # ASCII value of 'H'

print("After: ba = ",ba)  # Output: bytearray(b'Hello')


# C. Memoryview (memoryview)
mem_view: memoryview = memoryview(b"Operation Badar")
print(type(mem_view), " mem_view = ", mem_view)  # <class 'memoryview'>
print(bytes(mem_view[0:5]))
print( mem_view[6:11] ) #cast it to byte otherwise it will show memory address

# ___________________________________________________________________________________________________________
# None Data Type in Python
# In Python, None is a special data type that represents the absence of a value or a null object reference. It is a singleton object, meaning that there is only one instance of None in the entire Python environment.

# No value: None represents the absence of a value or a null object reference.

x: str = None
y: str = None
z: str = x

#display the data type of x:
print(type(x))
print("value of x = " + str(x) )
print("x == y = ", x == y)
print("id(x) = ", id(x))
print("id(y) = ", id(y))
print("id(z) = ", id(z))
print("x is y = ", x is y)
print("x is z = ", x is z)
print("id(x) is id(z) = ", id(x) is id(z)) # False :( why? you will get the answer in topic 'Integer Literals in Python'
print("id(x) == id(z) = ", id(x) == id(z)) # True
'''
In Python, `==` is the equality operator, which checks if the values of two objects are equal.
On the other hand, `is` is the identity operator, which checks if two objects are the same object in memory.
'''


print("None is None            = ", None is None) # True
print("None == None            = ", None == None) # True
print("None == x               = ", None == x)
print("None is x               = ", None is x)
print("id(None) is id(None)    = ", id(None) is id(None)) # 'is' check memory space sharing
#If number is out of integer literal range -5 to 256 then even the same number are considered as seprate object 
# ___________________________________________________________________________________________________________

#**id() Function in Python**
# The id() function in Python returns the unique identifier for an object. This identifier is a small integer that is unique among all objects
# currently in existence of your python environment.


print("""Variable x, y & z have 'None' value, as we know that 'None' is a singleton object,
meaning that there is only one instance of `None` in the entire Python environment.
So the id(x), id(y) & id(z) represents the same object id in memory.\n""")

x: str = None
y: str = None
z: str = x

print("ID of variable x  = " + str(id(x)))
print("ID of variable y  = " + str(id(y)))
print("ID of variable z  = " + str(id(z)))

print("\nIs variable x & y shares the same memory space? \nThe answer is: " + str(id(x) == id(y)))

# False in a boolean context: None is considered False in a boolean context, meaning that it can be used in conditional statements.

if(None):
  print("if block: This line of code will not execute because in Python 'None' is considered False")
else:
  print("else block: As None is considered False, so this line of code will execute")

# ___________________________________________________________________________________________________________
# Integer Literals in Python
# In Python, an integer literal is a sequence of characters that represents an integer value. Integer literals are used to define integer constants in Python code.
# Memory Space Sharing
# In Python, integer literals can share the same memory space under certain conditions. This is due to a process called interning, where Python
# stores a pool of interned objects that can be reused when the same value is needed again.

x: int = 1
y: int = 1
z: int = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x))) # when you need to concatinate any thing with string you need to first cast it to str()
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(y) = " + str(id(z)))
print("id(x) == id(y) = ", id(x) == id(y) )
print("id(x) is id(y) = ", id(x) is id(y) ) # ;)

# Integer Interning in Python

# In Python, integers in the range -5 to 256 are interned, meaning that they are stored in a pool of interned objects. This means that when you
# create an integer literal within this range, Python returns a reference to the existing object in the pool.

x = -6
y = -6
z = x

print("Value of x = " + str(x) + ", and id(x) = " + str(id(x)))
print("Value of y = " + str(y) + ", and id(y) = " + str(id(y)))
print("Value of z = " + str(z) + ", and id(y) = " + str(id(z)))

print("\n ===================== \n")

a = 257
b = 257
c = a

print("Value of x = " + str(a) + ", and id(a) = " + str(id(a)))
print("Value of y = " + str(b) + ", and id(b) = " + str(id(b)))
print("Value of z = " + str(c) + ", and id(c) = " + str(id(c)))


# Greenland Shark. Living in the waters of—you guessed it—Greenland, this shark lives for 300 to 500 years. It has the longest known lifespan
# of any vertebrate species
shark1_age = 300
shark2_age = 300

print("Value of shark1_age = " + str(shark1_age) + ", and id(shark1_age) = " + str(id(shark1_age)))
print("Value of shark2_age = " + str(shark2_age) + ", and id(shark2_age) = " + str(id(shark2_age)))

if(shark1_age == shark2_age): #comparison by value
  print("shark1_age & shark2_age have same age")
else:
  print("shark1_age & shark2_age have different age")

print(" ===================== ")

if id(shark1_age) == id(shark2_age):#comparison by id()
  print("shark1_age & shark2_age have same id")
else:
  print("shark1_age & shark2_age have different id")
# ___________________________________________________________________________________________________________
# Type Casting
# Type casting is the process of converting a value of one data type to another data type. Python supports several types of type casting,
# including:

# Type casting is the process of converting a value of one data type to another data type. Python supports several types of type casting, including:

# Implicit Type Casting: Python automatically converts a value of one data type to another data type when necessary. For example, when you add 
# an integer and a float, Python converts the integer to a float.
# Explicit Type Casting: You can use functions like int(), float(), str(), and bool() to explicitly convert a value of one data type to another
# data type.

i: int = 10
print("Value of i = " + str(i) + ",     Type of i = " + str(type(i)))

j: float = 20.6

f: float = i + j #Implicit Type Casting
print("Value of f = " + str(f) + ",   Type of f = " + str(type(f)))

f1: float = 66.89
print("Value of f1 = " + str(f1) + ", Type of i = " + str(type(f1)))

i1: int = int(f1) #When ever you type cast a float value into an integer it truncate
             #the decimal part and only keeps the whole number
print("Value of i1 = " + str(i1) + ",    Type of i = " + str(type(i1)))

s: str = "25.8"
f2: float = float(s)
print("Value of f2 = " + str(f2) + ",  Type of i = " + str(type(f2)))

#uncomment the below line of code to see error
#i2 = int(s) #correct this error by casting with float()
#print("Value of i2 = " + str(i2) + ", Type of i = " + str(type(i2)))

# ___________________________________________________________________________________________________________
# isinstance() Function in Python
# The isinstance() function in Python is used to check if an object (first argument) is an instance of a class (second argument). It returns
# True if the object is an instance of the class, and False otherwise.

# Syntax

# The syntax of the isinstance() function is as follows:

# Where:
#      . object is the object to be checked.
#      . classinfo is the class or a tuple of classes to check against.

age: int = 20
weight: float = 66.89
print("check: isinstance(age, int)      = ", isinstance(age, int))
print("check: isinstance(weight, int)   = ", isinstance(weight, int))
print("check: isinstance(weight, float) = ", isinstance(weight, float))
