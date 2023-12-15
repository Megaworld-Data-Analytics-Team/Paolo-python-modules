# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Lists
#
# Lists are one of Python's data structures used to group/collect data into a single variable. Items in a list can be accessed and modified individually or as a group. Items can be accessed with their respective indices, similar to strings. You can also think of strings as a list of characters. Lists are defined with brackets `[ ]` with each item being separated by commas `,`.
#
# Again, indices start at 0, meaning the first item in the list has an index of 0 and the last item has an index of `len()-1'.

# %%
list_1 = ["one", "two", "three"]

print(list_1)
print(list_1[2])
print(len(list_1)) #number of items in the list

# %% [markdown]
# **Note**: Lists of only one item will still be interpreted by Python as a list. Access the individual item to use it as its intended data type.

# %%
list_2 = ["zero"]

print(type(list_2))
print(type(list_2[0]))

# %% [markdown]
# While not practical, items in a list do not have to be related nor do they need to share the same data type.

# %%
list_3 = ["Sufjan", 75, 5.11]
print(list_3)

# %% [markdown]
# ### List Operations
#
# Lists in Python are dynamic, meaning their length can change throughout the programs runtime as items are added or removed. Modifying items in a list is mostly the same as before. The item has to be accessed through its index before modification. You can search for an item's index through its value with `index()`. 
#
# Similar to strings, you can identify the number of items in a string with `len()` and access the last item with index `len() - 1`

# %%
list_1 = ["one", "two", "three", "one"]

list_1[1] = "seven"
print(list_1)

print(list_1.index("one"))
print(list_1[len(list_1) - 1])

# %% [markdown]
# ### Adding items
#
# `append()` adds a new item at the end of the list. Since lists are a dynamic data structure, you may declare an empty list at the beginning of the code and append items after.
# `insert()` lets you add a new item with a specified position/index in the list.

# %%
list_4 = []

list_4.append("String")
list_4.append("Int")
list_4.append("Float")
list_4.append("List")
list_4.append("Float")

print(list_4)

# 2 will be the index of the new value after insertion
list_4.insert(2, "Boolean") 

print(list_4)

# %% [markdown]
# ### Removing items
# `del()` can remove item given the item's index. Similarly, `remove()` achieves the same but requires the item's value. 
#
# **Note**: like `insert()` which identifies items by value rather than index, `remove()` only considers the *first* instance (i.e. lowest index) of the specified value. Succeeding instances are unnaffected.

# %%
del list_4[0]
print(list_4)

list_4.remove("Float")
print(list_4)

# %% [markdown]
# ### Sorting
# `sort()` rearranges the list alphabetically or least to greatest. You can set the function's `reverse` parameter to `True` to sort in reverse.

# %%
list_4.sort()
print(list_4)

list_4.sort(reverse=True)
print(list_4)

list_5 = [43.4, 43.1, 50.66, 78.1, 25.99, 99.2]
list_5.sort(reverse=True)
print(list_5)

# %% [markdown]
# ### 2-Dimensional Lists
# Lists can be used to represent tabular data. Tables in python are represented as a list of lists. Navigating the items in the list will require 2 index values, representing the columns and rows where the item resides. 

# %%
list_2d = [[1,2,3],[4,5,6],[7,8,9]]

#list will be printed in a line
print(list_2d)

print("\n")

#prints list in a grid for easier visualization
print('\n'.join(' '.join(str(x) for x in row) for row in list_2d))

print("\n")

#first index is the row, second index is the column
n = list_2d[0][2]
print(n)


# %% [markdown]
# # Conditional Statements
#
# Sometimes you'll only want blocks of code to execute only under certain conditions, which is where `if-else` statements come in. `if` statements test for a condition and if the condition results in `True`, the block of code under it (signified by an indent in the code) is executed. If the condition results in `False`, the code under `else` is executed instead. The following code demonstrates the use of `if-else` in the defined **function** `compare_20()`. This function takes a number and displays if that number is greater than 20 or not. 

# %%
def compare_20(num):
    if num > 20:
        print(str(num) + " is greater than 20")
    else: 
        print(str(num) + " is NOT greater than 20")

compare_20(14)
compare_20(37)


# %% [markdown]
# `elif` statements are used if you would like to test for than one condition. If the initial condition is not satisfied, it checks for the succeeding conditions until one is satisfied. Additionally, `else` statements are optional, if none of the conditions in your if-elif chain are met, no code is executed (notice the lack of an output for `compare_20(20)`). 

# %%
def compare_20(num):
    if num > 20:
        print(str(num) + " is greater than 20")
    elif num < 20: 
        print(str(num) + " is less than 20")
    elif num > 30: 
        print(str(num) + " is greater than 30")

compare_20(25)
compare_20(14)
compare_20(37)
compare_20(20)


# %% [markdown]
# > **Note**: Conditions are checked in the code from top to bottom. Once a condition is satisfied, it will no longer check or execute for the other conditions below it (see the output for `compare_20(37)`). If you insist on having both conditions checked, consider having them in a separate if-statement/if-elif chain or changing the order of the conditions.

# %%
def compare_20(num):
    if num > 20:
        print(str(num) + " is greater than 20")
    elif num < 20: 
        print(str(num) + " is less than 20")
        
    if num > 30: 
        print(str(num) + " is greater than 30")

compare_20(37)

# %% [markdown]
# `if` and `elif` are followed by **boolean statements**. These accept any variable that takes a `True` or `False` result. The following is a list of operators used to compare strings or numbers when writing conditionals in code.
#
#
# | Operator | Name                     | Syntax |
# |----------|--------------------------|--------|
# |    ==    | Equal                    | x == y |
# |    !=    | Not Equal                | x != y |
# |     >    | Greater than             | x > y  |
# |     <    | Less than                | x < y  |
# |    >=    | Greater than or equal to | x >= y |
# |    <=    | Less than or equal to    | x <= y |
#
# >**Note**: `=` and `==` are different operators. The latter is used to compare between two variables and the former is used to assign a value to a variable.
#

# %% [markdown]
# # Looping
# Looping is when a block of code is executed repeatedly, either to iterate through lists or until a condition is satisfied.
#
# ### While Loop
#
# `while` loops can be used to repeatedly execute a block of code until its succeeding condition is met. The following is a `while` loop that is fixed to repeat and print 5 times. `i` here acts as loop counter which increments after each iteration and stops at 5 due to the conditional.

# %%
i = 1

while i <= 5:
    print("Loop #" + str(i))
    i += 1 # i += 1 is equivalent to i = i + 1
    
print("end")

# %% [markdown]
# Infinite loops occur when there is no way to achieve the specified conditions within the block of code. In other words, the boolean statement is unable to result in `False`. The following `while` loops are examples that result in an infinite loop. 

# %%
# i = 1
# while i <= -1:
#     print("Loop #" + str(i))
#     i += 1
    
# i = 1
# while i <= 5:
#     print("Loop #" + str(i))
    
# while True:
#     print("Loop")

# %% [markdown]
# Aside from using a fixed number and an incrementing variable in each loop execution, you can also stop a while loop by using either a flag variable or a `break` statement. The following code will continue to prompt the user for a text input until the user inputs "exit".

# %%
active = True

# using flag variable 'active'
while active:
    msg = input("type 'exit' to close the program: ")
    
    if msg == "exit":
        active = False
        print("Closing program...")
    else:
        print(msg)
        
# alternatively: using 'break' keyword
# while True:
#     msg = input("type 'exit' to close the program: ")
    
#     if msg == "exit":
#         print("Closing program...")
#         break
#     else:
#         print(msg)

# %% [markdown]
# ### For Loop
# `for` loops are typically used to iterate through a list (or other iterable variables like strings). The code repeats for every item in the list, which is ideal for situations where you would like to modify all the items in a similar way.
#
# __Iterables__ - objects where each individual member/item can be accessed and iterated on. Variable types such as lists, strings, dictionaries, tuples, sets.

# %%
list_6 = [14,42,66,8,10,27]

"""
    this loop halves each item in the list
    i acts as the "iterator variable", which takes the value of an item in the list for one loop at a time
"""
for i in list_6:
    print(i/2)
    
print("\n")

for i in "Hello":
    print(i)

# %% [markdown]
# `for` loops don't require a condition to be satisfied for the loop to terminate. Rather, termination occurs once the items in an iterable is exhausted and there are no further items for the inner code block to execute. Where `while` loops can be programmed to run indefinitely, `for` loops depend on the size/length of the iterable it is given and the number of loops is typically known before the looping code executes.
#
# The following is a `while` loop alternative to the previous block of code which reqiures some extra logic to satisfy the condition of the loop. `for` loops are generally more convenient for navigating lists, otherwise `while` loops are more flexible. 

# %%
i = 0

"""
    using <= over < will cause an index out of range error since it lets `i` reach index 6, 
    the current list is only until index 5
"""

while i < len(list_6):
    print(list_6[i])
    i += 1
    

# %% [markdown]
# # Assignment
# Write a program that does the following in order:
# 1. declare an empty list
# 2. append 7 numerical values to the list 
# 3. print the list
# 4. using a while loop, reverse the order of the list (i.e. swap the values of the first and last index, 2nd and 2nd last, ...)
# 5. print the modified list

# %%
numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.append(7)

print(numbers)

ln = len(numbers)
i = 0

while i < len(numbers)/2:
    first = numbers[i]
    last = numbers[ln - (i + 1)]
    
    numbers[i] = last
    numbers[ln - (i + 1)] = first
    
    i += 1
    
print(numbers)
    

# %%
