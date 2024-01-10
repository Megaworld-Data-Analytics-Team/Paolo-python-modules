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
# # Running your first Python script
# Your first python script is simple. This line of code runs the `print()` function which displays any text written inside. Select the code block below and run it.
#
# ![how to run code](https://i.imgur.com/z10no90.png)

# %%
print("hello!")

# %% [markdown]
# You can also write comments alongside your code. These can be used to help make your code more readable and will not affect how the code runs.

# %%
# this comment will produce no output
# print("hello")

# %% [markdown]
# ## Variables and data types
# Let's see that first script again but with a slight change. Select the cell of code below and try to run it.

# %% tags=["raises-exception"]
print(hello)

# %% [markdown]
# Notice the error: `name 'hello' is not defined`
#
# The previous line of code failed to execute and display the text "hello" because rather than being interpreted as text, due to the lack of quotations (`" "`) it's instead interpreted as the name of a **variable**. A variable is essentially a container for data that your program can manipulate and refer back to again within its lifetime. The error occurs because the variable `hello` has not been assigned a value and can not be displayed by `print()`. In other words, `hello` does not exist yet, so there is nothing to show.
#
# Here, we declare a variable named `message` and set its value to be `"hello"` using the `=` operator.

# %%
message = "hello"
print(message)

# %% [markdown]
# This displays a similar output to our first python script and acts as an alternative way to write it. How this method differs is that the `message` can be changed, overwritten and used multiple times throughout your program.
#
# Let's take the same variable and reassign its value to the string variable `"hi"`. The previous value of `message` has now been overwritten.

# %%
message = "hi"
print(message)

# %% [markdown]
# Aside from strings, there are other common basic data types. For now we'll mostly be dealing with **int** (numbers without decimals), **float** (numbers with decimals), and **boolean** (True or False)

# %%
#data type: int
test_var = 81
print(test_var)

print(test_var - 2) #the variable can be changed/manipulated while inside print()

#data type: float
test_var = 9.08
print(test_var)

#data type: boolean
test_var = True
print(test_var)

# %% [markdown]
# You can use `type()` to know the specfic data type of a variable

# %%
test_var = 82.4
print(type(test_var))

test_var = "sample string"
print(type(test_var))

# %% [markdown]
# ## Variable naming convention
#
# Note that variable names are case sensitive. `Message` and `message` will be treated as different variables. 
#
# Python enforces some limitations to variable names. Not adhering to these rules will cause errors:
# - names can not start with a number
# - names can only contain alphanumeric characters (0-9,A-z) and underscores
#
# Legal variable names: `msg`,`msg1`, `myMsg`, `my_msg`\
# Illegal names: `1msg`, `my msg`, `my-msg`
#
# ---
#
# Other than the rules that are inherent to Python, it's good practice to have a consistent naming convention throughout your codebase to make code easier to read and navigate. In our case, we'll be using the **snake case** naming convention where words are separated with an underscore (`_`).

# %%
#example
snake_case_var = "introduction to Python"
sample_variable = None

# %% [markdown]
# ## Obtaining user input
#
# So far, we've only asked `print()` to display data that is already made known to the program prior to code execution, but what if we want it to show data that isn't already found or written in the code. 
#
# `input()` similar to `print()` will display text as well as prompt the user for input. 

# %%
input("Enter string: ")

# %% [markdown]
# Store that input in a variable named `your_input` so our program can refer back to it and and display it through `print()`

# %%
your_input = input("Enter string: ")
print("You said: " + your_input)

# %% [markdown]
# Alternatively, if you know the input will not be used later in the program, you may shorten the code like this, eliminating the need for a variable

# %%
print("You said: " + input("Enter string: "))

# %% [markdown]
# Now lets try asking the user for a numerical input. In return, our script will display the entered number and add 2.

# %% tags=["raises-exception"]
message = "Enter number: "
your_input = input(message)
print(your_input + 2)

# %% [markdown]
# This error is an example of 2 different data types (in this case, a string and an int) attempting to interact. `input()` interprets all data that goes through it as a string, so when `your_input + 2` executes, it is attempting to add the value 2 to text which shouldn't be possible. To resolve this, we can do **data type conversion** to convert `your_input` to a usable int by putting the desired variable inside `int()`.

# %%
your_input = int(input(message))
print(your_input + 2)


#alternatively...
#print(int(input(message) + 2)

# %% [markdown]
# You can also do this in reverse with `str()`, converting a numerical value so it may be concatenated with a string

# %%
your_input = str(18.9)
print("Your number is " + your_input)

# %% [markdown]
# ## Arithmetic operations

# %%
x = 10
y = 3

print("Addition (+): " + str(x + y))
print("Subtraction (-): " + str(x - y))
print("Multiplication (*): " + str(x * y))
print("Division (/): " + str(x / y))

#division but removes decimal values
print("Division (//): " + str(x // y))

#returns remainder of x divided by y
print("Modulo (%): " + str(x % y))

# x raised to the power of y
print("Exponent (**): " + str(x**y))

# %% [markdown]
# ## String operations
#
# There's a variety of functions that allow us to modify existing strings and text data from variables. Many of the concepts applied here will be discussed more in-depth when we explore **lists**, but for now we'll demonstrate the syntax behind common string manipulation tasks.
#
# ### Concatenation
# Aside from arithmetic addition on numeric data types, the `+` operator can also be used to concatenate strings together.

# %%
message1 = "Hello "
message2 = "there!"
print(message1 + message2)
print(message1 + "World")

# %% [markdown]
# ### String Length
# `len()` takes a string and returns the number of characters. **Note**: `len()` can be applied outside of strings, those other use cases will be discussed later.

# %% tags=["raises-exception"]
print(len("computer"))
print(len("123456789"))
print(len("exit        "))

print(len(14)) #len() is not applicable to int, this will cause an error

# %% [markdown]
# ### String Indexes
# The index of a character refers to its position relative to the entire string. The first character in a string has an index of 0, second character has an index of 1, third has index of 2, and so on. The length of the string minus 1 or `len()-1` corresponds to the index of the last character. To access a character in your string, use `string_name[n]` where n is the index of your desired character. 
#
# There are no characters beyond 0 and `len()-1`, calling an index outside of those numbers will cause an error (See last line of code).

# %% tags=["raises-exception"]
message1 = "Hello World"

print(message1[0])
print(message1[1])
print(message1[len(message1)-1])

print(message1[20])

# %% [markdown]
# ### String Slicing
#
# You can get a substring of a string using `string_name[n:m]` where n is the starting index and m is the ending index *minus 1*, respectively. 

# %%
message1 = "Lorem ipsum dolor sit amet"
ln = len(message1)

print(message1[0:ln]) #take the whole string
print(message1[:])    #take the whole string; alternative

print(message1[0:1])  #take the first character
print(message1[4:9])  #take the 4th-9th characters

print(message1[:4])   #take the first 4 characters
print(message1[-4:])  #take the last 4 characters

print(message1[4:])   #take all EXCEPT the first 4 characters
print(message1[:-4])  #take all EXCEPT the last 4 characters


# %% [markdown]
# ### Splitting
# When called on a string, `split()` takes a character and separates the string into substrings and places them in a *list* based off the given character. In the list, each string can be accessed individually.

# %%
message1 = "Lorem ipsum dolor sit amet"
print(message1.split(' '))
print(message1.split('m'))
print(message1)

# %% [markdown]
# ### Replace Substring
#
# `replace()` can be used to modify specific sections of a string. This function requires 2 values, the first is the substring to be replaced out, second is the replacement substring. 
#
# **Note**: `replace()` and `split()` do not modify the original string. `print(message1)` remains unchanged even after applying string modification. The function's result must be assigned to a variable if you are to use it again.

# %%
message1 = "Lorem ipsum dolor sit amet"
print(message1.replace("or", "XX"))
print(message1.replace(" ", "..."))
print(message1)

# %% [markdown]
# # Assignment
# Write a program that prompts the user to input a word. After inputting a word, display the following:
# 1. the number of letters in the word divided by 2
# 2. the first and last letters of the word

# %%
word = input("Enter word:")
print(len(word)/2)
print(word[0] + "," + word[len(word)-1])

# %%
