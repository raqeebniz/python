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

