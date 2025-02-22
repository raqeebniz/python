#  5: Working with Lists and Tuples
# Introduction
# Python provides powerful sequence types: lists and tuples. These data structures help store and manage
# collections of data efficiently.



# 1. Lists in Python
# Ordered: Lists are ordered, meaning that the items in the list have a specific order and can be accessed by their index.
# Mutable: Lists are mutable, meaning that they can be modified after they are created.
# Indexed: Lists are indexed, meaning that each item in the list has a specific index that can be used to access it.
# Dynamic size: Lists can grow or shrink dynamically as elements are added or removed.
# Heterogeneous: Lists can contain elements of different data types, such as integers, strings, floats, and other lists.
# Supports duplicate values: Lists can contain duplicate values.



# Creating a List

# Creating lists with different data types
fruits: list  = ["apple", "banana", "cherry"]
numbers: list = [10, 20, 30, 40]
mixed: list   = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

#--------------------------
# Accessing List Elements
# You can access elements using indexing (starting from 0) and negative indexing (starting from -1).

fruits: list = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple, accessing element in reverse order
# -------------------------
# Modifying Lists
# Lists are mutable, meaning their elements can be changed.

fruits: list = ["apple", "banana", "cherry"]
fruits[-3] = "watermelon" # replacing "apple" with "watermelon"
print(fruits)  # Output: ['watermelon', 'banana', 'cherry']
# ----------------------------------------------------------------

# List Slicing

# Extract multiple elements using slicing.
print(fruits[0:2])  # Output: ['watermelon', 'banana'] 0 and 1

# -----------------------------------------

# 2. Common List Methods
# Lists provide built-in methods for efficient data manipulation.

# Appending and Extending Lists
fruits.append("mango")  # Adds a single element 'mango' to the end
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango']

fruits.extend(["grape", "kiwi"])  # Adds multiple elements
print(fruits)  # Output: ['watermelon', 'banana', 'cherry', 'mango', 'grape', 'kiwi']

# ------------------------------------------
# Removing Elements
# In Python, remove() and pop() are two distinct methods used to manipulate lists. While they may seem similar
# ,they have different purposes and behaviors.

# Remove() Method
# The remove() method is used to delete the first occurrence of a specified value from a list. If the value is
# not found in the list, a ValueError exception is raised.

# Key aspects of remove():

# 1 Value-based: remove() searches for a specific value in the list.

# 2 Returns None: The remove() method does not return any value.

# 3 Raises ValueError: If the value is not found in the list, a ValueError exception is raised.

fruits.remove("banana")  # Removes 'banana' # run multiple times to see error as "banana" is already removed
print(fruits)



# Pop() Method
# The pop() method is used to delete an item at a specified index from a list. If no index is provided
# ,it removes and returns the last item in the list.

# Key aspects of pop():

#  1 . Index-based: pop() searches for an item at a specific index in the list.
#  2 . Returns the removed item: The pop() method returns the item that was removed from the list.
#  3 . Raises IndexError: If the index is out of range, an IndexError exception is raised.

deleted = fruits.pop(1)  # Removes and returns the element at index 1 # run it multiple time to see error
print("deleted element = ", deleted)  # Output: 'cherry'
print(fruits) # Output: ['watermelon', 'mango', 'grape', 'kiwi', 'mango']


#------------------------------------------
# Sorting a List

numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# reverse sorting
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# -------------------------------------------------

# 3. Iterating Over Lists
# Use loops to process elements in a list.

# Using a for-loop

for fruit in fruits:
    print(fruit)

# -------------------------------------------------------\
# Using list comprehension

# List comprehension is a powerful feature in Python that allows you to create new lists in a concise and 
# readable way. It's a compact way to create lists from existing lists or other iterables by applying a
# transformation or filter to each element

# new_list = [expression for element in iterable if condition]

# expression is the operation you want to perform on each element.
# element is the variable that takes on the value of each element in the iterable.
# iterable is the list or other iterable that you want to process.
# condition is an optional filter that determines whether an element is included in the new list.

# Without if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] ] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]


# With if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] if x > 3] #  if x > 3 place this if condition and see
print(squared, " : ", type(squared))  # Output: [1, 4, 9, 16, 25]


# List comprehension is commonly used for:

   # Transforming data: List comprehension can be used to transform data from one format to another.
   # Filtering data: List comprehension can be used to filter out unwanted data.
   # Creating new data: List comprehension can be used to create new data by combining existing data.

#----------------------------------------------------------------------

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

#---------------------------------------------------
# Dictionaries in Python

# 1. Introduction to Dictionaries
# A dictionary is a collection of key-value pairs. It is:

 # Ordered (since Python 3.7): Items are stored in the order they were inserted.
 # Mutable: Items can be added, removed, or modified after the dictionary is created.
 # Un-indexed: Items are accessed using keys, not indices.
 # Without duplicates: Keys must be unique, but values can be duplicated.

# Before Python 3.7, dictionaries were unordered, meaning that items were not stored in a specific order.
# However, with the introduction of Python 3.7, dictionaries now maintain their insertion order. 

# -------------------------------------------------------------------

# 2. Creating a Dictionary

# Dictionaries are created using curly braces {} with key-value pairs separated by commas.

# The syntax is:
# dictionary = {key1: value1, key2: value2, ...}

# Example Code:

# prompt: genrate a List of 5 american cities

american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
american_cities


# A Person Example
# Create a dictionary to store a person's details
person: dict = {
    "name": "Alice",
    "age": 25,
    "city": american_cities
}
print(person)



thisdict: dict = dict(name = "John", age = 36, country = "Norway") # It is also possible to use the dict() constructor to make a dictionary.
print(type(thisdict)," - ", thisdict, )


# 3. Accessing Values

# You can access the value associated with a key using square brackets [] or the get() method.

# Example Code:

# Access values using keys
print(person["name"])  # Output: Alice
print(person.get("age", "99"))  # Output: 25, if not found it will return 99 (default value)

# Access a non-existent key
print(person.get("country", "my_default_vlaue"))  # Output: my_default_vlaue (default value)

#--------------------------------------------------------------------

# 4. Modifying a Dictionary

# You can add new key-value pairs or modify existing ones.

# Example Code:

# Add a new key-value pair
person["email"] = "alice@example.com"
print(person)

# Modify an existing value
person["age"] = 26
print(person)


# 5. Deleting Items

# You can remove a key-value pair using the del keyword or the pop() method.

# Note that pop() returns the value of the removed key-value pair, whereas del does not return anything.

# You can also use pop() with a default value, in case the key is not found in the dictionary:

# Example Code:

person: dict = {'name': 'Alice', 'age': 25, 'email': 'alice@example.com', 'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

# Remove a key-value pair using del
del person["city"]
print(person)

# Remove with key

# Remove a key-value pair using pop
age: int = person.pop("age", 0)
print("Removed age:", age)
print(person)

#Again remove a key which is already removed to check the default value
age: int = person.pop("age", 0)
print("key 'age' not found in dict so returning default value: ", age)


# 6. Dictionary Methods

# Python provides several useful methods for working with dictionaries.

# Method	Description	
#______________________________
# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.	


# Get all keys
print("person.keys()         = ", person.keys()  )  # Output: dict_keys(['name', 'email', 'city', 'age'])

# Get all values
print("person.values()       = ", person.values())  # Output: dict_values(['Alice', 'alice@example.com', 'Los Angeles', 27])

# Get all key-value pairs
print("person.items()        = ", person.items())  # Output: dict_items([('name', 'Alice'), ('email', 'alice@example.com'), ('city', 'Los Angeles'), ('age', 27)])

# Update the dictionary
person.update({"city": "Los Angeles", "age": 27})
print("After: person.update  = ", person)

# Clear the dictionary
person.clear()
print("After: person.clear() = ", person)  # Output: {}




# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
print(thisdict)

# ----------------------------------


# 7. Iterating Over a Dictionary

# You can loop through a dictionary using for loops.

# Example Code:

# only return key
for key in thisdict:
    print(key)


# return kay and value togather
for key, value in thisdict.items():
    print(key," : ", value)    

#------------------------------------------


# 8. Practical Examples
# Here are two practical examples to solidify these concepts.

# Example 1: Building a Phonebook

# Create a phonebook
phonebook: dict = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

# Add a new contact
phonebook["David"] = "111-222-3333"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")



#-------------------------------------------------------



# 9. Common Pitfalls
# Using a non-existent key without checking first for e.g. "

#print(my_dict.get("name_1")) # Output: None
#print(my_dict.get("name_1", "No name found")) # Output: No name found
#print(my_dict["name_1"])  # (raises a KeyError).

# Always use get() or check if the key exists with in to avoid error.

# Forgetting that dictionary keys must be immutable (e.g., strings, numbers, or tuples).

# Assuming dictionaries are ordered (in Python 3.6+, they retain insertion order, but this is not guaranteed in older versions).



# ------------------------------------------






# All Dict Functions

# prompt: generate a working example of all dictionary function

# Example Dictionary
my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# 1. Accessing Items
print("1. Accessing Items")
print("Name:", my_dict["name"])  # Accessing by key
print("Age:", my_dict.get("age"))  # Accessing using get()
print("City (using get):", my_dict.get("city"))

# 2. Adding Items
print("\n2. Adding Items")
my_dict["email"] = "john@example.com"
print("Dictionary after adding email:", my_dict)

# 3. Modifying Items
print("\n3. Modifying Items")
my_dict["age"] = 31
print("Dictionary after modifying age:", my_dict)

# 4. Removing Items
print("\n4. Removing Items")
my_dict.pop("city")
print("Dictionary after removing city (using pop):", my_dict)
del my_dict["email"]
print("Dictionary after removing email (using del):", my_dict)

# 5. Dictionary Methods
print("\n5. Dictionary Methods")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 6. Clearing the Dictionary
print("\n6. Clearing the Dictionary")
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Adding items back for further examples
my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# 7. Updating the Dictionary
print("\n7. Updating the Dictionary")
my_dict.update({"age": 32, "country": "USA"})
print("Dictionary after updating:", my_dict)

# 8. Iterating Through a Dictionary
print("\n8. Iterating Through a Dictionary")
print("Iterating through keys:")
for key in my_dict:
  print(key)

print("\nIterating through values:")
for value in my_dict.values():
  print(value)

print("\nIterating through items (key-value pairs):")
for key, value in my_dict.items():
  print(f"{key}: {value}")

#9 checking if a key exist
print("\n9. checking if a key exist")
if "name" in my_dict:
    print("Name exist")
else:
    print("Name do not exist")

# 10. Dictionary Length
print("\n10. Dictionary Length")
print("Length of the dictionary:", len(my_dict))

# 11. Creating a dictionary from iterable
print("\n11. Creating a dictionary from iterable")
iterable = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
new_dict = dict(iterable)
print("new dictionary:", new_dict)

# 12. Copying a dictionary
print("\n12. Copying a dictionary")
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# 13. Nested Dictionaries
print("\n13. Nested Dictionaries")
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested dictionary:", nested_dict)
print("Alice's age:", nested_dict["person1"]["age"])

