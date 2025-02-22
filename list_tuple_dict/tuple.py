# 4. Tuples in Python

# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data
# collections.

# Creating a Tuple
tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)


# Even though tuples are immutable, Python may create new instances in memory when you define identical tuples
# in separate assignments. This is why id(tuple_1) and id(tuple_2) may differ.

tuple_1: tuple = (10, 20, 30) # tuple
tuple_2: tuple = (10, 20, 30) # tuple

print("id(tuple_1) = ", id(tuple_1)) # unique memory address
print("id(tuple_2) = ", id(tuple_2)) # unique memory address

print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2) # comparing by value

# Why are Tuples Immutable?

# There are several reasons why tuples are immutable:

# Memory Efficiency: Immutable tuples can be stored in a single block of memory, which makes them more
# memory-efficient than lists.

# Thread Safety: Immutable tuples are thread-safe, meaning that they can be safely accessed and shared 
# between multiple threads without fear of modification.

# Hashability: Immutable tuples are hashable, meaning that they can be used as keys in dictionaries.

# Summary:
# ✔ Tuples save memory 🧠
# ✔ Tuples are safe for multi-tasking 🔒
# ✔ Tuples can be used as dictionary keys 🔑

# That’s why Python keeps tuples unchangeable! 🚀 

# lets create an error.

# UnComment below line to chek Error
# tuple1[0] = "watermelon" # immutable


# Tuples in Python

# A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
# Tuples are useful for fixed data collections.

# Creating a Tuple
tuple1: tuple      = tuple(["apple", "banana", "cherry"])  # cast a list into tuple
tuple2: tuple      = (10, 20, 30)  # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True)  # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

# Accessing elements in a tuple
print("tuple1[0] =", tuple1[0])  # Accessing first element

# Tuple slicing
print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# Tuple length
print("Length of tuple1:", len(tuple1))

# Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
  print(item)

# Checking if an item exists in a tuple
print("Is 20 in tuple2?", 20 in tuple2)

# Concatenating tuples
tuple3: tuple = tuple1 + tuple2
print("tuple1 + tuple2 =", tuple3)

# Repeating tuples
tuple4: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple4)

# Nested tuples
nested_tuple = (tuple1, tuple2)
print("nested_tuple =", nested_tuple)

# Unpacking tuples
a, b, c = tuple1
print("Unpacking tuple1:", a, b, c)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)

#Trying to modify a tuple will result in a TypeError
# tuple1[0] = "watermelon" #immutable. This line will raise an error. Uncomment to test.


print(tuple1[0])   # Output: apple
print(tuple1[-3])  # Output: apple
print(tuple1.count("apple"))
print(tuple1.index("apple"))

#error
#tuple1.sort()
#tuple1.reverse()
#tuple1.append("mango")
#tuple1.extend(["grape", "kiwi"])
#tuple1.remove("banana")
#deleted = tuple1.pop(1)



# prompt: print the complete list of methods and attribute of tuple, dont include dunders

# Get a list of all attributes and methods of a tuple
tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]

# Print the list of methods (excluding dunder methods)
tuple_methods


# prompt: generate a example of ['count', 'index'] in tuple

tuple1: tuple = tuple(["apple", "banana", "cherry"])
print(tuple1.count("apple"))  # Output: 1
print(tuple1.index("apple"))  # Output: 0
example_tuple: tuple = ('count', 'index')
print(example_tuple) # Output: ('count', 'index')

# ---------------------------------------------------------------




# Python is Type Hint Language

a: int = input ("Enter your name: ")
print(a, type(a) )

# Type Hinting (a: int)
#  a: int is a type hint, which suggests that the variable a is expected to be an integer.

#  However, type hints are not enforced in Python. They are only for documentation and tools
#  like linters or type checkers.

# The actual value assigned to a will still be a string, because input() always returns a string.
