# Loops and Iteration in Python

# 1. Introduction to Loops
# Loops are used to repeat a block of code multiple times. Python supports two types of loops:

# for loops: Used to iterate over a sequence (e.g., lists, strings, or ranges).
# while loops: Used to repeat a block of code as long as a condition is True.
# When to use scenario:

# A. For Loop:

# Grading a class of students: You have a list of 30 students and you want to calculate the average score for each student. You use a for loop to iterate over the list of students and calculate the average score for each one.

# Washing Machine(number spins), Microwave Oven e.t.c.

# B. While Loop:

# Filling up a gas tank: You want to fill up your gas tank until it's full. You don't know how many times you'll need to fill up the tank, but you'll keep filling it up until it's full. You use a while loop to fill up the tank until it's full.

# Air Conditioner, Refigrator, Heater, Washing Machine(filling water) e.t.c.


# 2. The for Loop
# The for loop iterates over a sequence (like a list, string, or range) and executes a block of code for each
# item for a specified or fixed number of times.

# Example Code:
# Iterate over a list
fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Note: Membership Operators in Python in, not in

# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)

# In Lesson 01 we learned about range()

# Print numbers from 0 to 4
for i in range(5):
    print(i)    

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)


for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    # Code to be executed 100,000 times
    print(f"Hello, World! Iteration { _ }")


# 3. The while Loop

# The while loop repeats a block of code as long as a condition is True.

# Example Code:

# Print numbers from 1 to 5
count: int = 1
while count <= 5:
    print(count)
    count += 1



# 4. Controlling Loops    

# Python provides two keywords (break & continue) to control loops:

# break: Exits the loop immediately.
# continue: Skips the rest of the code in the current iteration and moves to the next iteration.

# Example Code:

# Break example
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4


# Continue example
for i in range(5):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4


# 5. Nested Loops        

# What are nested loops?
# Nested loops also known as inner loops or nested iterations, refer to the process of placing one loop inside
# another loop. The inner loop will iterate through its entire cycle for each iteration of the outer loop.

# Example Code:
# Multiplication table
for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row


# Use Cases for Nested Loops

# Nested loops are useful in various scenarios, such as:

# 1. Matrix operations: When working with matrices, you often need to iterate over each element in a 
#    two-dimensional array. Nested loops can help you achieve this.

# 2. Iterating over multiple lists: If you have multiple lists and want to perform operations on each 
#    combination of elements, nested loops can be used.

# 3. Games and simulations: Nested loops can be used to create game boards, simulate complex systems, or 
#    iterate over multiple levels of data.

# 4. Data processing: When dealing with large datasets, nested loops can help you process and analyze the data
#    by iterating over each element and performing operations.

# Best Practices for Using Nested Loops

# While nested loops can be powerful, it's essential to use them wisely to avoid performance issues and
#  improve readability:

# 1. Minimize nesting: Try to limit the number of nested loops to three levels or less, as excessive nesting
#    can lead to performance degradation and decreased readability.

# 2. Use meaningful variable names: Use clear and descriptive variable names to help distinguish between the 
#    outer and inner loops.

# 3. optimize loop conditions: Ensure that the loop conditions are optimized to minimize unnecessary 
#    iterations.

# ___________________________________________________________________

# 6. Practical Examples

# Here are two practical examples to solidify these concepts.


# Example 1: Sum of Numbers
# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)


# Example 2: Finding Factors of a Number
# Find factors of a number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")