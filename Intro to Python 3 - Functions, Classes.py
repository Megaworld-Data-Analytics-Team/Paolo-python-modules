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
# # Functions
# Functions provide a way for developers to bundle their code for repeated use. Rather than rewritting the same blocks of code for similar tasks, you can instead define a function that handles that task and call that function. `print()` is one of the built-in functions we have already been using, but we can also create our own.
#
# Consider this task: for each item in a list of words, print the word. Without functions you could approach the task like this..

# %%
words = ["one", "two", "three", "four"]
words_2 = ["eleven", "twelve", "thirteen"]
words_3 = ["seven", "eight", "nine"]

for i in words:
    print(i)
    
for i in words_2:
    print(i)
    
for i in words_3:
    print(i)


# %% [markdown]
# This, however, makes for repetitive code, and for longer and more complex tasks, writting code in this manner is tedious. Instead, let's define a function named `print_list()` that takes a list as a **parameter** and prints each word.

# %%
def print_list(words):
    for i in words:
        print(i)


# %% [markdown]
# Functions are independent sections of code that do not execute on their own. They're typically defined prior to the actual start of the program and do not affect how the code runs until they are called. To use a function, we have to call them similar to how we use `print()`. 

# %%
print_list(words)
print_list(words_2)
print_list(words_3)

# %% [markdown]
# The `words` list in the function definition is reffered to as a **parameter** (sometimes also called an argument). These are variables that the function requires when it is called and is how we pass information to functions. Calling a function without sending all necessary variables will cause an error.

# %% tags=["raises-exception"]
print_list()

# %% [markdown]
# Alternatively, passing more paramters than what the function accepts will also result in an error.

# %%
print_list(words, words_2)


# %% [markdown]
# Note that when defining a function with multiple paramters, the order they are defined in is important when calling the function. Alternatively, you can specify which value corresponds to which parameter to disregard order.

# %%
def subtract(num1, num2):
    print(num1 - num2)
    
subtract(5,2)
subtract(2,5)
subtract(num2 = 3, num1 = 7)


# %% [markdown]
# You can also define **default values** to your parameters. When passing values to a function, passing for parameters with default values is optional. These optional parameters will instead take a pre-defined value for its process. 

# %%
def subtract(num1, num2=10):
    print(num1 - num2)
    
subtract(2)   #num1 = 2, num2 = 10
subtract(2,4) #num1 = 2, num2 = 4


# %% [markdown]
# Parameters is how functions *recieve* information but they are also capable of sending back data through `return`. Here, `subtract()` returns the resulf of `num1 - num2` and is displayed by `print()`.

# %%
def subtract(num1, num2):
    return num1 - num2

print(subtract(5,2) + 7)


# %% [markdown]
# As a recap, here is some of the syntax for defining your functions.

# %%
def function_x():
    print("...")

def function_y(param1):
    print("...")
    return None

def function_z(param1, param2=True):
    print("...")
    return None

function_z(None)


# %% [markdown]
# # Classes
#
# Rather than defining a process, classes instead define a set of properties for a variable (which can include functions). You can use classes to represent objects. For example, let's say we want to develop an application that displays available room listings to the user. Each room would have properties like the price, location and size/area. 
#
# Here we define an empty class with the `class` keyword

# %%
class Room:
    pass


# %% [markdown]
# Now lets give the `Room` class some attributes and functions. The `init()` function is used to create an instance of the object class and assign variable values upon instantiation.

# %%
class Room:
    def __init__(self, price, room_open):
        self.price = price
        self.room_open = room_open
    
    def close_room(self):
        self.room_open = False
    
    def open_room(self):
        self.room_open = True
        
    def get_status(self):
        if self.room_open:
            print("open")
        else:
            print("closed")
            
#instantiating Room class objects, this calls the __init__() function            
room_1 = Room(3400, True)
room_2 = Room(200, False)

# accessing instance variables through <object name>.<attribute name>
print(room_1.price)
print(room_2.price)

print(room_1.room_open)
print(room_2.room_open)


# %% [markdown]
# The `self` parameter refers to the object instance that calls its respective function. Each instance of an object will have their own values for their attributes `price` and 
#
# >`room_open`. `room_1.get_status()` is equivalent to writing `Room.get_status(room_1)` where `room_1` is passed as `self`. <br>
# In other words: \<instance\>.function() is equivalent to \<Object\>.function(\<instance\>)
#

# %%
room_1.get_status()
room_1.close_room()
room_1.get_status()
room_2.get_status()
Room.open_room(room_2)
Room.get_status(room_2)

# %% [markdown]
# ## Storing Classes and Functions in modules
# To organize and shorten your code for easier reading, classes and functions can be stored into separate files as modules and then imported into the main code. Code from the modules can be slotted into any other program with `import`. `functions.py` contain some of the functions and classes that have been shown here with an addition. Try importing these modules into another/previous notebooks and calling the `concatenate()` function. Documentation for the new function is written in the file. 

# %%
import functions as fn

words = ["This","is","a","sentence."]
print(fn.concatenate(words))

# %% [markdown]
# # Understanding Documentation
# In succeeding modules, we'll be importing functions from other libraries to assist in our tasks rather than writing the code for it ourselves. Here's an example of using the square root function `sqrt()` from the [numpy](https://numpy.org/doc/stable/index.html) library.

# %%
import numpy as np

print(np.sqrt(36))


# %% [markdown]
# `sqrt()` is a fairly straightforward function, pass a number and the function returns the root value. Some functions, however, are more complex. Their usage may not be as clear and may have more specifications for their parameters. To understand these functions better, most commonly used libraries have available documentation that details all its stored functions and classes. 
#
# See the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html) for the `sqrt()` function we just used. The page describes all the functions parameters and return value. Here we can see that the function actually has a bit more it can do that the initial description written earlier. It has a few optional parameters that can be used if necessary and the function can also take a lists of numbers rather than only individual values. The documentation may also sometimes show syntax and example code to assist you. Here's an example of [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) for another function we'll be using in the future.
#
# In larger scale projects, writing documentation for the code you write is essential both so you and other collaborators can understand and remember how to use your code. The code inside `functions.py` shows an example on how to write documentation for a function.

# %%
def concatenate(words):
    """ <description of function> 
        This function takes a list of words and combines them into one string

    Arguments: 
        <variable name {data type} -- description> 
        words {List} -- strings to be concatenated

    Returns:
        <data type -- descriptions> 
        String -- concatenated string, words separated by space
    """

    full_string = ""

    for i in words:
        full_string = full_string + i + " "
    
    return full_string


# %% [markdown]
# ## Lambda functions
#
# These are single-line compressed versions of regular functions that dont require defining. Useful for creating short, one-time use functions that make up less code. Also used to write for other functions that require another function as a parameter. The syntax is as follows:
#     
#     lambda <parameters> : <code>
#
# __NOTE__: Unlike regular functions, lambda will always have a return value.

# %%
#function that prints text "Hello"
hello = lambda : print("Hello")
hello()

#function that takes a string 'x' and returns a string with all characters in uppercase
uppercase = lambda x : x.upper()
print(uppercase("Title"))

#function that takes value 'x' and returns x^2
square = lambda x : x*x
print(square(5))

# %% [markdown]
# The next few functions provide a way for us to quickly operate on iterables with just a few lines of code, potentially bypassing the need for extended `for` loops. These will be useful for applying similar operations on larger datasets for the following module.
#
# ## map()
#
#     map(func, *iterables)
#
# This function takes 2 parameters, `func` is the function that is to be applied on each item on `iterables`. Notice the asterisk `*`, this means that there can be any number of iterable variables depending on the requirements of `func`. 
#
# Consider the following task: Write a program that takes a list of website names and concatenates the string ".com" at the end. Here's how we would write that with what we know so far.

# %%
words = ["twitter", "youtube", "reddit", "google", "discord"]
new_words = []

for x in words:
    word = x + ".com"
    new_words.append(word)
    
print(new_words)

# %% [markdown]
# The `map` function provides an alternative, compressed and more flexible way to write this with the same output. __NOTE__: `map` returns a map object so it has to manually be transformed back into its desired data type.

# %%
words = ["twitter", "youtube", "reddit", "google", "discord"]

"""
    CODE BREAKDOWN:
    words - list of strings to be concatenated
    lambda w:w+".com" - lambda function where 'w' is the given list of words
    map() - 'func' is passed as the lambda function and `iterable` is `words`, `func` is then applied to each individual item
    list() - transforms the return value of map() into a list
"""

new_words = list(map(lambda w:w+".com", words))
print(new_words)


# %%
# Regular functions can also be used in place of 'func'
def add_com(word):
    return word+".com"

new_words = list(map(add_com, words))
print(new_words)

# %% [markdown]
# `map` can take multiple iterables depending on the requirements of `func`. If `func` requires 2 iterables for its parameters then both those iterables will also be passed to `map`. When dealing with two iterables, `func` will be applied to the first item on the first iterable with the first item on the second iterable. Then it will use the second item on both iterables, then the third, and so on.
#
# Here's more complex version of the task from earlier: Write a program that takes a list of website names. Before each name, number it depending on its position in the list. After each name, concatenate ".com".

# %%
words = ["twitter", "youtube", "reddit", "google", "discord"]

def add_com(word, num):
    return str(num)+". "+word+".com"

"""
    CODE BREAKDOWN:
    words - list of strings to be modified
    range(1,6) - generates a sequence of numbers from 1 to 5, used for numbering, output = [1,2,3,4,5]
    add_com() - function where 'word' is the string to be modified, 'num' as the number to be added for numbering 
    
    map() - add_com passed as 'func','words' list passed as the first iterable for 'word', range() passed as second iterable for 'num'
          - execution of the function is as follows:
              > add_com("twitter",1)
              > add_com("youtube",2)
                  ...
              > add_com("discord",5)
    
    list() - transforms the return value of map() into a list
"""

# order of the iterables depends on the order of the parameters defined in the function
new_words = list(map(add_com, words, range(1,6)))
print(new_words)

# %% [markdown]
# > __NOTE__: In the case that the two iterables are not of equal length, `map` simply stops computing for values once either list is exhausted of items to iterate. 

# %%
#second iterable is shorter than first
words = ["twitter", "youtube", "reddit", "google", "discord"]
nums = range(1,4)

new_words = list(map(add_com, words, nums))
print(new_words)

#first iterable is shorter than second
words = ["twitter", "youtube", "reddit", "google", "discord"]
nums = range(1,8)

new_words = list(map(add_com, words, nums))
print(new_words)

# %% [markdown]
# ## filter()
#     filter(func, iterable)
#     
# Like `map`, `filter` takes a function and applies it on every item on `iterable`. Unlike the previous function however, `func` is required to return a boolean (True/False) value. `filter` passes each item through `func` and returns the list of items that resulted in `func` returning True. In other words, `filter` checks a condition on each item of `iterable`. `filter` then returns the list of items that met the condition.
#
# The following code takes a list of grades and returns the list of passing grades (>= 70).

# %%
grades = [69, 78, 74, 89, 92, 90, 65, 82]

passed = list(filter(lambda x: x >= 70, grades))
print(passed)

# %% [markdown]
# ## reduce()
#     reduce(func, iterable, initial)
#     
# Rather than returning a list like our previous functions, `reduce` returns a singular value. `func` here is restricted to accepting 2 parameters. These parameters are not restricted to taking iterables, however. `reduce` takes the first and second items in the iterable and "combines" them into a new value created by `func`, this new value is then use with the next item in the iterable and applies `func` for another value. This continues until all items have been exhausted and the whole iterable has been combined into one value. `initial` is an optional paramter that, if set, will take the place of the first item and move all other items one position forward. 
#
# Let's take our `concatenate` function from earlier and rewrite it with `reduce`.

# %%
# import reduce function from functools library
from functools import reduce

words = ["This","is","a","sentence."]

"""
    CODE BREAKDOWN:
    words - list of strings to be combined into one
    lambda w1,w2 - lambda function, concatenates w2 to w1
    
    reduce() - passes lambda function as `func` and words as `iterable`
             - execution of lambda w1,w2 is as follows:
                  > "This"+" "+"is"
                  > "This is"+" "+"a"
                  > "This is a"+" "+"sentence"
"""

full_string = reduce(lambda w1,w2: w1+" "+w2, words)
print(full_string)

# %% [markdown]
# # Assignment
# Complete the code, replace "None" with the appropriate variables/values. Use the following functions to accomplish their respective tasks.
# 1. map: convert list of numbers (String) to list of numbers (int)
# 2. filter: define a function that returns True if a string has an even number of characters, return False otherwise. Given a list of strings, filter out words from the list that dont fit the condition.
# 3. reduce: Given a list of strings, reduce to a single string containing all consonants used, letters should not be repeated in the final output.

# %%
import re
from functools import reduce

# map
numbers = ["1", "2", "3", "4", "5", "6"]
numbers = list(map(lambda n:int(n), numbers))
print(numbers)

# filter
words = ["even", "odd", "Unlike", "other", "edit", ".", "too ", "features"]

def is_even(word):
    if len(word) % 2 == 0:
        return True
    else: return False

even = list(filter(is_even, words))
print(even)

# reduce 
words = ["bulk", "rusty", "frags", "erase", "features"]

def remove_vowels(word):
    word = re.sub("[aeiouAEIOU]","", word)
    return word

def get_consonants(w1, w2):
    word = remove_vowels(w1) + remove_vowels(w2)
    word = "".join(sorted(set(word)))
    return word

consonants = reduce(get_consonants, words)
print(consonants)

# %%
import re
from functools import reduce

# map
numbers = ["1", "2", "3", "4", "5", "6"]
numbers = None
print(numbers)

# filter
words = ["even", "odd", "Unlike", "other", "edit", ".", "too ", "features"]

def is_even(word):
    if None:
        return None
    else: return None

even = None
print(even)

# reduce 
words = ["bulk", "rusty", "frags", "erase", "features"]

def remove_vowels(word):
    word = re.sub("[aeiouAEIOU]","", word)
    return word

def get_consonants(w1, w2):
    word = None
    word = "".join(sorted(set(word)))
    return word

consonants = None
print(consonants)

# %%
