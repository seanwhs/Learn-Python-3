# Python from scratch course
# First hand-on class: Python Basics
# Nicolas Gutierrez 2023

# The code in this script in separated in cells by concepts.

# %% Spyder IDE description and introduction
# -- Three main windows: Editor, Variable explorer, IPython console.
# -- Options in the menus.
# -- Configuration of different interpreters.
# -- blocks of code in Spyder.
# -- Comment and Uncommenting in spyder
# -- Running a line or a block

# %% Indentation in Python

# Code starts in column 0 as follows
print("Hello")
print("Python students!")

# Lines belonging to a block
# Indentation (Normally 4 spaces or a tabulation) are used in Python to group
# lines into a block of code.
# Unlike Matlab, Python does not use a keyword to close a block of code, but
# just the indentation, what makes cleaner code.
# Indentation markings can be activated in all IDE, so the number of spaces...
# can be clearly checked and/or modified.
a = ## Complete here
if a:
    print("It seems a is True")

# NOTE: You can display the indentation character in your IDE. If you are using spyder
# you can go to Tools->Prefernces->Editor and click show "Show blank spaces". PEP8
# recommends 4 spaces as a standard indentation mechanism.

# NOTE 2: Spaces can be annoying, but you can activate indent guides to guide you in
# intricated if-else trees.

# %% PEP 8 and styling in Python
# https://peps.python.org/pep-0008/
# PEP 8 is the standard code styling guide in Python. I recommend you read it and try
# to stick to the standars so your code is more understandable and more pythonic in
# general terms.

# "Code is read much more often that it is written" by Guido Van Rossum

# Good naming is important in all languages, Python included. 

# %% Built in Data Types (Python Native data types)
# 1) Numeric
# 2) Strings
# 3) Lists
# 4) Tuples
# 5) Dictionaries
# 6) Set

# 1) Numeric Data Types
# Integers.
a = ## Complete here
print("The variable", a, " is of type ", type(a))

# Floats.
b = ## Complete here
print("The variable ", b, " is of type", type(b))

# Complex.
c = ## Complete here
print("The variable ", c, " is of type", type(c))

# 2) String Data Types
d = ## Complete here
print("The variable ", d, " is of type", type(d))

# 3) Lists - Collection of elements
# List initialization
e_1 = []
e_2 = list()
# Collection of numbers
e = ## Complete here
print("The variable ", e, " is of type", type(e))
# Collection of strings
f =## Complete here
print("The variable ", f, " is of type", type(f))
# Collection of objects
g = ## Complete here
print("The variable ", g, " is of type", type(g))
# Interesting methods inside lists
e.append(4)
e.append([5])
e.extend(6)
e.extend([7])
e.sort()
e.pop(0)
e.insert(0, 1)
e.reverse()

# 4) Tuple - Collection of elements too
# Collection of numbers
h = ## Complete here
print("The variable ", h, " is of type", type(h))
# Collection of strings
i = ## Complete here
print("The variable ", i, " is of type", type(i))
# Collection of objects
j = ## Complete here
print("The variable ", j, " is of type", type(j))
# Interesting methods inside tuples
h.append(2)

# 5) Dictionaries - Collection of elements, but indexed by strings/ints
# Dictionary initialization
k_1 = {}
k_1 = dict()
# Indexed by strings
k = ## Complete here
print("The variable ", k, " is of type", type(k))
# Indexed by int
l = ## Complete here
print("The variable ", l, " is of type", type(l))
# Interesting methods inside dictionaries
k.keys()
k.values()
k.pop()

# 6) Set - Collection of elements unindexed and unordered
# Set is useful to find the unique values in a list-tuple and to compare groups
# Set initilization
m_1 = set()
# Set of strings
m = ## Complete here
print("The variable ", m, " is of type", type(m))
# Set of ints
n = ## Complete here
print("The variable ", n, " is of type", type(n))
# Interesting methods inside dictionaries
n.add(5)
n.pop() # This removes an arbitrary element

# Set requires immutable elements!

# Mutability, which ones of these data types are mutable and not mutable?
# Mutable -> List, Dictionary, set
# Immutable -> Tuple, int, float, complex, string

# %% Indexing in basic Python

list_to_show_indexing = ## Complete here

# In Python, the first element of a list is always a 0, instead of 1 as in Matlab. 
# The last element of a list is a -1. Negative indexes allow going through an iterable
# in inverse order.
first_element = ## Complete here
print(f"The first element is {first_element}")
last_element = ## Complete here
print(f"The last element is {last_element}")

# Slices of indexes can be used in Python to select a group of elements. For that you need
# to use ":" between the indices. 
elements_from_second_to_last = ## Complete here
print(f"Elements from the second to last are {elements_from_second_to_last}")
elements_from_third_to_one_to_last = ## Complete here
print(f"Elements from the third to the one to last are {elements_from_third_to_one_to_last}")

# Did you notice the fstrings used above? 

# %% Logic evaluation
# Python has and, or and not as logical operators.
# Additionally ==, !=, >, <, >= and <= are used as in other programming languages.

o = ## Complete here
if o == "a":
    print("Variable", o, "is a")
elif o == "b":
    print("Variable", o, "is b")
else:
    print("Variable", o, "is other thing")

# == is for value equality and "is" is for reference equality
## Complete something below
if  is not None:
    print("Variable", o, "is not None")
else:
    print("Variable", o, "is None")


## Create here a conditional using "and" in the evaluation


# Until Python 3.10, Python does not have a native way of implementing
# switch statements. If you need to do so, normally you create a function
# and inside create a if-elif tree with what you need.

# %% Iterations
# Python can use the typical for and while loops. The only difference comparing it with
# other languages is that Python requires a iterant of values.
# Create a for loop

## Complete here

# Create a while loop
## Complete here

# One handy option in Python is that it can iterate through the elements of a list, while
# it keeps track of the index at the same time. The keyword for this is enumerate

## Complete here

# %% Functions
# Functions are defined with the keyword def, then the name of the functions followed by
# the input arguments. After the operations, the keyword return is used to return any
# parameter from the function.
# Create a function with three input parameters and 2 outputs

## Complete here

output1, output2 = first_function_in_python(1, 2, 3)
print(output1)
print(output2)
output_1, _ = first_function_in_python(2, 2, 2)
print(output1)

# Optional parameters are indicated in the function definition indicating a default value,
# example_function(optional_input="")
# Create a function in python with at least one optional parameter

## Complete here

output3 = second_function_in_python()
print(output3)
output3 = second_function_in_python(1)
print(output3)

# %% Exceptions
# Exceptions/errors happen in all languages when the code is not able to be executed. 
# When your code could error in a section of it, what it is normally done is wrap it with
# a "try-catch" structure. In Python it is try-except. Wrap the following operation:

## Complete here

# You can use additionally try, except, else and finally to guide the execution of your
# code.

## Complete here

# %% Reading and writing from a file

string_to_print = "Hello world"
list_of_text = ["This is a\n", "test\n", "for storing text in a file\n"]
text_file_name = "testfile.txt"

## Print the contents of string_to_print
## Complete here

## Open a file with writing permissions and writelines from list_of_text
## Complete here

## Open a file with read permissions and read it
## Complete here

print(file_content)