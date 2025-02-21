# Operators in Python

# Operators in Python are symbols used to perform operations on variables and values. Python supports several types of operators:


# 1. Arithmetic Operators
# Used for basic mathematical operations.

# Example:
a: int = 10
b: int = 3
print("a + b  = ", a + b)   # 13 Addition
print("a - b  = ", a - b)   # 7 Subtraction
print("a * b  = ", a * b)   # 30 Multiplication
print("a / b  = ", a / b)   # 3.3333333333333335
print("a // b = ", a // b)  # 3 Floor Division
print("a % b  = ", a % b)   # 1 Modulus (remainder)
print("a % b  = ", a ** b)  # 1000 Exponentiation (10 * 10 * 10)

#___________________________________________________________________
# 2. Comparison (Relational) Operators
# 2. Comparison (Relational) Operators

# Example
x: int = 10
y: int = 5

print("x == y = ", x == y)  # False, Equal
print("x != y = ", x != y)  # True, Not equal
print("x > y  = ", x > y)   # True, Greater than
print("x < y  = ", x < y)   # False, Less than
print("x >= y = ", x >= y)  # True, Greater than or equal
print("x <= y = ", x <= y)  # False, Less than or equal


#___________________________________________________________________
# 3. Logical Operators
# Used to combine conditional statements.

# Example

x: bool = True
y: bool = False

print("x and y = ", x and y)  # False
print("x or y  = ", x or y)   # True
print("not x   = ", not x)    # False

#___________________________________________________________________
# 4. Assignment Operators
# Used to assign values to variables.

x = 5
print("Assignment: x = 5                    ",x)  # Output: 5

x += 3  # Equivalent to x = x + 3
print("Addition Assignment: x += 3          ",x)  # Output: 8

x -= 3  # Equivalent to x = x - 3
print("Subtraction Assignment: x -= 3       ",x)  # Output: 5

x *= 3  # Equivalent to x = x * 3
print("Multiplication Assignment: x *= 3    ",x)  # Output: 15

x /= 3  # Equivalent to x = x / 3
print("Division Assignment: x /= 3          ",x)  # Output: 5.0

x //= 3  # Equivalent to x = x // 3
print("Floor Division Assignment: x //= 3   ",x)  # Output: 1.0


# Why Use Shorthand Operators?
# Readability: Makes the code more concise and easier to read.
# Efficiency: Reduces the need to repeat the variable name.
# Common Practice: Widely used in Python and other programming languages.

#___________________________________________________________________
# 5. Identity Operators
# Used to compare memory locations.
a: list = [1, 2, 3]
b: list = [1, 2, 3]
c: list = a

print("a is c     =  ",a is c)       # True  (same object, sharing same memmory space)
print("a is b     =  ",a is b)       # False (different objects, seperate memmory space)
print("a == b     =  ", a == b)      # True  (same values, different memmory space but having same vlaues)
print("a is not b =  ", a is not b)  # True  (True because of different memmory space, although having same memmory space)

print('\n-----\n') # seperator for better output readability

print("id(a) = ", id(a))
print("id(b) = ", id(b))
print("id(c) = ", id(c))


#___________________________________________________________________
# 6. Membership Operators
# Used to check if a value exists in a sequence (list, tuple, string, etc.).

# Example

my_list: list = [1, 2, 3, 4, 5]

print("my_list           = ", my_list)            # [1, 2, 3, 4, 5]
print("3 in my_list      = ", 3 in my_list)       # True
print("10 not in my_list = ", 10 not in my_list)  # True

print("\n-----\n")

my_string: str = "Operation Badar"

print("my_string                 = ", my_string)                # Operation Badar
print("'O' in my_string          = ", 'O' in my_string)         # True
print("'Hello' not in my_string  = ", 'Hello' not in my_string) # True

#___________________________________________________________________
# Python Keywords
# Keywords in Python are reserved words that have special meanings and serve specific purposes in the language syntax. Python keywords cannot
# be used as the names of variables, functions, and classes or any other identifier.
import keyword

# Line continuation (`\`) allows printing a statement over multiple lines, improving code readability without breaking the string.
print("The list of \
keywords is : ")

# printing all keywords at once using "kwlist()"
print(keyword.kwlist)

# You cant use keywords/ reserved words as variable name. 
# Uncomment below line to see error

#and: bool = True

#___________________________________________________________________
# Python Variables

# In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name
# that is assigned to a value. Unlike many other programming languages, Python variables do not require explicit declaration of type. 
# The type of the variable is inferred based on the value assigned.

# (inferred meaning deduce or conclude (something) from evidence and reasoning rather than from explicit statements.)

# Variables act as placeholders for data. They allow us to store and reuse values in our program.

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive (myVar and myvar are different).
# Avoid using Python keywords (e.g., if, else, for) as variable names.

# Valid variable names
# name = "Alice"
# _age = 25
# salary2024 = 50000
# my_variable = "Python"

# Invalid variable names
# 2name = "Bob"          # ❌ Starts with a digit
# my-variable = "Error"  # ❌ Contains a hyphen
# class = "CS101"        # ❌ Uses a reserved keyword


# Here are the naming conventions in Python with their respective names:

# CapWords or PascalCase: Class names
# snake_case: Variable names, function names, method names, module names, package names
# UPPER_CASE: Constant names
# dunder (double underscore): Special method names (e.g. __init__, __str__)

# It's worth noting that the official Python style guide, PEP 8, recommends using CapWords for class names and snake_case for variable names,
# function names, and other identifiers.

# Assigning Different Values
# We can assign different values to multiple variables simultaneously, making the code concise and easier to read.

x, y, z = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

print(x, y, z)

# Uncomment below line to see error
# x: int, y: float, z: str = 1, 2.5, "Python" # Using type hints while assigning mutiple variables simultaneously cause and error invalid syntax

# print(x, y, z)


# Delete a Variable Using del Keyword
# We can remove a variable from the namespace using the del keyword. This effectively deletes the variable and frees up the memory it was using.

# Assigning value to variable
x: int = 10
print(x)

# Removing the variable from memory using del keyword
del x

# Trying to print x after deletion will raise an error
# print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
print(x) # NameError: name 'x' is not defined, because we already delete variable x (del x)

# Explanation:
# del x removes the variable x from memory. After deletion, trying to access the variable x results in a NameError, indicating that the variable no longer exists.





















