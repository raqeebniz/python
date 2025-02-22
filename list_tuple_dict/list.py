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
